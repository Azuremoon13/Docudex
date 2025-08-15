import sqlite3
import os
import re

DB_NAME = "docudex.db3"

def define_env(env):

	@env.macro
	def generateChangelog(table_name):
		if not re.match(r'^[0-9]+$', f"{table_name}"):
			return "Invalid Mod ID"
		
		if not os.path.exists(DB_NAME):
			return "No Changelog Generated."
		
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()

		cursor.execute("""
			SELECT name FROM sqlite_master
			WHERE type='table' AND name=?
		""", (table_name,))
		if cursor.fetchone() is None:
			conn.close()
			return "No Changelog Generated."

		cursor.execute(f'SELECT version, changelog FROM "{table_name}" ORDER BY CAST(version AS INTEGER) DESC')
		rows = cursor.fetchall()
		conn.close()

		formatted_rows = []
		for version, changelog in rows:
			md_changelog = changelog.replace("<p>", "\n").replace("</p>", "\n").replace("<br>", "\n").strip()
			escaped_changelog = re.sub(r'^(\s*[-*]?\s*)(#+)', lambda m: m.group(1) + m.group(2).replace('#', r'\#'), md_changelog, flags=re.MULTILINE)

			formatted = f"####v{version}\n\n{escaped_changelog}"

			formatted_rows.append(formatted)
		return "\n".join(formatted_rows)