from jupyterlab_git.git import Git
import os
import json

git = Git()

# Clone a repo
async def git_clone(path: str, url: str) -> str:
    res = await git.clone(path, repo_url=url)
    if res["code"] == 0:
        return f"✅ Cloned repo into {res['path']}"
    return f"❌ Clone failed: {res.get('message', 'Unknown error')}"

# Get repo status
async def git_status(path: str) -> str:
    res = await git.status(path)
    if res["code"] == 0:
        return f"📋 Status:\n{json.dumps(res, indent=2)}"
    return f"❌ Git status failed: {res.get('message', 'Unknown error')}"

# Get Git log
async def git_log(path: str, history_count: int = 10) -> str:
    res = await git.log(path, history_count=history_count)
    if res["code"] == 0:
        return f"🕓 Recent commits:\n{json.dumps(res, indent=2)}"
    return f"❌ Git log failed: {res.get('message', 'Unknown error')}"

# Pull changes
async def git_pull(path: str) -> str:
    res = await git.pull(path)
    return "✅ Pulled latest changes." if res["code"] == 0 else f"❌ Pull failed: {res.get('message', 'Unknown error')}"

# Push changes
async def git_push(path: str) -> str:
    # jupyterlab_git expects remote and branch args for push
    # assuming defaults: origin and current branch
    res = await git.push(remote="origin", branch="", path=path)
    return "✅ Pushed changes." if res["code"] == 0 else f"❌ Push failed: {res.get('message', 'Unknown error')}"

# Commit staged changes
async def git_commit(path: str, message: str) -> str:
    res = await git.commit(commit_msg=message, amend=False, path=path)
    return "✅ Commit successful." if res["code"] == 0 else f"❌ Commit failed: {res.get('message', 'Unknown error')}"

# Stage files
async def git_add(path: str, add_all: bool = True, filename: str = "") -> str:
    if add_all:
        res = await git.add_all(path)
    elif filename:
        res = await git.add(filename=filename, path=path)
    else:
        return "❌ No file specified and add_all is False."

    files = "ALL" if add_all else filename
    return f"✅ Staged: {files}" if res["code"] == 0 else f"❌ Add failed: {res.get('message', 'Unknown error')}"

# Get Git repo root
async def git_get_repo_root(path: str) -> str:
    dir_path = os.path.dirname(path)
    res = await git.show_top_level(dir_path)
    if res["code"] == 0 and res.get("path"):
        return f"📁 Repo root: {res['path']}"
    return f"❌ Not inside a Git repo. {res.get('message', '')}"
