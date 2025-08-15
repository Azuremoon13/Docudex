import os
import aiosqlite
import aiohttp
import asyncio
import re
import ast
from dotenv import load_dotenv

load_dotenv()

DB_NAME = "docudex.db3"

class ModDatabase:
	def __init__(self, db_path=DB_NAME):
		self.db_path = db_path

	async def setup(self):
		self.conn = await aiosqlite.connect(self.db_path)
		await self.conn.execute("""
			CREATE TABLE IF NOT EXISTS latest_files (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				mod_id TEXT UNIQUE,
				file_id TEXT
			)
		""")
		await self.conn.commit()

	async def create_mod_table(self, mod_id: int):
		await self.conn.execute(f"""
			CREATE TABLE IF NOT EXISTS "{mod_id}" (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				version TEXT,
				changelog TEXT
			)
		""")
		await self.conn.commit()

	async def get_latest_file_id(self, mod_id: int):
		async with self.conn.execute("SELECT file_id FROM latest_files WHERE mod_id = ?", (mod_id,)) as cursor:
			result = await cursor.fetchone()
		return result[0] if result else None

	async def update_latest_file_id(self, mod_id: int, file_id: int):
		await self.conn.execute("""
			INSERT INTO latest_files (mod_id, file_id)
			VALUES (?, ?)
			ON CONFLICT(mod_id) DO UPDATE SET file_id = excluded.file_id
		""", (mod_id, file_id))
		await self.conn.commit()

	async def update_mod_changelog(self, mod_id: int, version: str, changelog: str):
		await self.conn.execute(f"""
			INSERT INTO "{mod_id}" (version, changelog)
			VALUES (?, ?)
		""", (version, changelog))
		await self.conn.commit()

	async def close(self):
		await self.conn.close()


class CurseForgeAPI:
	def __init__(self, api_key: str):
		self.api_key = api_key
		self.base_url = "https://api.curseforge.com/v1"
		self.headers = {"x-api-key": self.api_key, "Accept": "application/json"}

	async def get_latest_file(self, mod_id: int, session: aiohttp.ClientSession):
		async with session.get(f"{self.base_url}/mods/{mod_id}", headers=self.headers) as resp:
			data = (await resp.json()).get("data", {})
			latest_files = data.get("latestFiles", [])
			if latest_files:
				return str(latest_files[0]["id"]), latest_files[0].get("displayName")
		return None, None

	async def fetch_all_mod_files(self, mod_id: int, session: aiohttp.ClientSession):
		page_index = 0
		all_files = {}
		while True:
			async with session.get(
				f"{self.base_url}/mods/{mod_id}/files",
				headers=self.headers,
				params={"pageSize": 50, "index": page_index}
			) as resp:
				data = (await resp.json()).get("data", [])
				if not data:
					break
				for file_info in data:
					if file_info.get("displayName") != "5.5-":
						all_files[file_info["id"]] = file_info
				page_index += 1

		all_files_list = list(all_files.values())
		return {(f["id"], f["displayName"]) for f in all_files_list if "windows " in f["displayName"].lower()}
	
	async def fetch_changelog(self, mod_id: int, file_id: int, session: aiohttp.ClientSession):
		async with session.get(f"{self.base_url}/mods/{mod_id}/files/{file_id}/changelog", headers=self.headers) as resp:
			data = await resp.json()
			return data.get("data", "")


async def process_mod(mod_id: int, db: ModDatabase, api: CurseForgeAPI, session: aiohttp.ClientSession):
	await db.create_mod_table(mod_id)
	stored_latest_id = await db.get_latest_file_id(mod_id)
	latest_file_id, display_name = await api.get_latest_file(mod_id, session)

	if latest_file_id is None:
		print(f"No files found for mod {mod_id}.")
		return

	if stored_latest_id == latest_file_id:
		print(f"Mod {mod_id}: Already up to date.")

	elif stored_latest_id is not None:
		changelog = await api.fetch_changelog(mod_id, latest_file_id, session)
		print(f"Mod {mod_id}: New changelog:\n{changelog}")
		await db.update_latest_file_id(mod_id, latest_file_id)
		version = re.search(r"\b\d+(?=\.zip)", display_name)
		version = version[0] if version else "Unknown"
		await db.update_mod_changelog(mod_id, version, changelog)
	else:
		all_files = await api.fetch_all_mod_files(mod_id, session)
		print(f"Mod {mod_id}: First run — found {len(all_files)} files.")
		await db.update_latest_file_id(mod_id, latest_file_id)
		for id, display_name in all_files:
			changelog = await api.fetch_changelog(mod_id, id, session)
			version = re.search(r"\b\d+(?=\.zip)", display_name)
			version = version[0] if version else "Unknown"
			await db.update_mod_changelog(mod_id, version, changelog)
		


async def main():
	cf_key = os.getenv("CF_API_KEY")
	if not cf_key:
		raise ValueError("CF_API_KEY not found in .env")

	db = ModDatabase()
	await db.setup()
	api = CurseForgeAPI(cf_key)

	async with aiohttp.ClientSession() as session:
		with open("tracked_mods.txt") as f:
			mod_ids = [int(line.strip()) for line in f if line.strip() and not line.startswith("#")]
		if mod_ids:
			tasks = [process_mod(mod_id, db, api, session) for mod_id in mod_ids]
			await asyncio.gather(*tasks)
		else:
			print("No tracked mod IDs")

	await db.close()


if __name__ == "__main__":
	asyncio.run(main())
