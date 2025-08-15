import os
import hmac
import hashlib
from aiohttp import web
import subprocess

GITHUB_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")

async def handle_webhook(request):
    if request.method != "POST":
        return web.Response(status=405, text="Method not allowed")
    
    body = await request.read()
    signature = request.headers.get("X-Hub-Signature-256")
    if signature is None:
        return web.Response(status=400, text="Missing signature")

    expected_sig = "sha256=" + hmac.new(
        GITHUB_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()
    if not hmac.compare_digest(signature, expected_sig):
        return web.Response(status=403, text="Invalid signature")

    event = request.headers.get("X-GitHub-Event", "")
    if event != "push":
        return web.Response(status=200, text="Event ignored")

    payload = await request.json()
    if payload.get("ref") != "refs/heads/main":
        return web.Response(status=200, text="Not main branch")

    try:
        subprocess.run(["./build_mkdocs.sh"], check=True)
        return web.Response(status=200, text="MkDocs rebuild triggered")
    except subprocess.CalledProcessError as e:
        return web.Response(status=500, text=f"Build failed: {e}")

app = web.Application()
app.router.add_post("/git-rebuild", handle_webhook)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8000)
