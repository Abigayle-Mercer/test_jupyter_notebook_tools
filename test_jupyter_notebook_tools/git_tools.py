# git_tools.py
from jupyterlab_git.git import Git
import os

git = Git()

# Clone a repo
async def git_clone(path: str, url: str) -> str:
    res = await git.clone(None, {"current_path": path, "repo_url": url})
    if res["code"] == 0:
        return f"✅ Cloned repo into {res['path']}"
    return f"❌ Clone failed: {res.get('message', 'Unknown error')}"

# Get repo status
async def git_status(path: str) -> str:
    res = await git.status(None, {"current_path": path})
    return f"📋 Status:\n{res}"

# Get Git log
async def git_log(path: str, history_count: int = 10) -> str:
    res = await git.log(None, {"current_path": path, "history_count": history_count})
    return f"🕓 Recent commits:\n{res}"

# Pull changes
async def git_pull(path: str) -> str:
    res = await git.pull(None, {"current_path": path})
    return "✅ Pulled latest changes." if res["code"] == 0 else f"❌ Pull failed: {res.get('message', 'Unknown error')}"

# Push changes
async def git_push(path: str) -> str:
    res = await git.push(None, {"current_path": path})
    return "✅ Pushed changes." if res["code"] == 0 else f"❌ Push failed: {res.get('message', 'Unknown error')}"

# Commit staged changes
async def git_commit(path: str, message: str) -> str:
    res = await git.commit(None, {"current_path": path, "commit_msg": message})
    return "✅ Commit successful." if res["code"] == 0 else f"❌ Commit failed: {res.get('message', 'Unknown error')}"

# Stage files
async def git_add(path: str, add_all: bool = True, filename: str = "") -> str:
    files = "ALL" if add_all else filename
    res = await git.add(None, {"current_path": path, "add_all": add_all, "filename": filename})
    return f"✅ Staged: {files}" if res["code"] == 0 else f"❌ Add failed: {res.get('message', 'Unknown error')}"

async def git_get_repo_root(path: str) -> str:
    """
    Given the path of a file, return the path to the Repo root, if any. 
    """
    dir_path = os.path.dirname(path)
    res = await git.show_top_level(dir_path)
    if res["code"] == 0 and res.get("path"):
        return f"📁 Repo root: {res['path']}"
    return f"❌ Not inside a Git repo. {res.get('message', '')}"
