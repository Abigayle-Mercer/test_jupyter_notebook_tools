import json
from jupyter_scheduler.scheduler import Scheduler
from jupyter_server.utils import ensure_async
from jupyter_server.serverapp import ServerApp
from jupyter_scheduler.environments import DefaultEnvironmentsManager

root_dir = ServerApp.instance().root_dir
env_mgr = DefaultEnvironmentsManager()
db_url = "sqlite:///scheduler-jobs.sqlite"

scheduler = Scheduler(root_dir=root_dir, environments_manager=env_mgr, db_url=db_url)
_scheduler_started = False

async def ensure_scheduler_started():
    global _scheduler_started
    if not _scheduler_started:
        await ensure_async(scheduler.start())
        _scheduler_started = True

async def scheduler_create_job(
    notebook_path: str,
    name: str = "Scheduled Job",
    cron_schedule: str = None
) -> str:
    """
    Schedule a notebook to be executed, optionally on a recurring basis using cron.
    """
    await ensure_scheduler_started()

    job_data = {
        "name": name,
        "path": notebook_path
    }
    if cron_schedule:
        job_data["cron_schedule"] = cron_schedule

    try:
        job = await ensure_async(scheduler.create_job(job_data))
        return f"✅ Job created with ID: {job['id']}"
    except Exception as e:
        return f"❌ Failed to create job: {str(e)}"

async def scheduler_list_jobs() -> str:
    """
    Return a list of all scheduled jobs.
    """
    await ensure_scheduler_started()

    try:
        jobs = await ensure_async(scheduler.list_jobs())
        return f"📋 Jobs:\n" + json.dumps(jobs, indent=2)
    except Exception as e:
        return f"❌ Failed to list jobs: {str(e)}"

async def scheduler_get_job(job_id: str) -> str:
    """
    Fetch metadata and status for a specific job.
    """
    await ensure_scheduler_started()

    try:
        job = await ensure_async(scheduler.get_job(job_id))
        return f"🔍 Job {job_id}:\n" + json.dumps(job, indent=2)
    except Exception as e:
        return f"❌ Failed to get job {job_id}: {str(e)}"

async def scheduler_cancel_job(job_id: str) -> str:
    """
    Cancel a scheduled job by ID.
    """
    await ensure_scheduler_started()

    try:
        await ensure_async(scheduler.cancel_job(job_id))
        return f"❌ Job {job_id} cancelled."
    except Exception as e:
        return f"❌ Failed to cancel job {job_id}: {str(e)}"
