import json
from jupyter_server.utils import ensure_async

# ✅ REFACTORED versions of the scheduler tools.
# Each expects `scheduler` (a Scheduler instance) as the first argument

async def scheduler_create_job(
    scheduler,
    notebook_path: str,
    name: str = "Scheduled Job",
    cron_schedule: str = None
) -> str:
    """
    Create a new scheduled job using the Jupyter Scheduler extension.

    Parameters:
        scheduler: The Scheduler instance to use.
        notebook_path: The full path to the notebook to be scheduled.
        name: The name for the scheduled job.
        cron_schedule: Optional cron schedule string for recurring jobs.

    Returns:
        A string message indicating success or failure.
    """
    if not scheduler:
        return "❌ Scheduler not available."

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
    


async def scheduler_run_job(scheduler, job_id: str) -> str:
    """
    Trigger a scheduled job to run immediately.

    Parameters:
        scheduler: The Scheduler instance to use.
        job_id: The ID of the job to run.

    Returns:
        A string message indicating success or failure.
    """
    if not scheduler:
        return "❌ Scheduler not available."

    try:
        job = await ensure_async(scheduler.run_job(job_id))
        return f"🚀 Job `{job_id}` has been started."
    except Exception as e:
        return f"❌ Failed to run job {job_id}: {str(e)}"



async def scheduler_list_jobs(scheduler) -> str:
    """
    List all scheduled jobs.

    Parameters:
        scheduler: The Scheduler instance to use.

    Returns:
        A JSON-formatted string of all jobs or an error message.
    """
    if not scheduler:
        return "❌ Scheduler not available."

    try:
        jobs = await ensure_async(scheduler.list_jobs())
        return f"📋 Jobs:\n" + json.dumps(jobs, indent=2)
    except Exception as e:
        return f"❌ Failed to list jobs: {str(e)}"


async def scheduler_get_job(scheduler, job_id: str) -> str:
    """
    Get detailed information about a specific job.

    Parameters:
        scheduler: The Scheduler instance to use.
        job_id: The unique identifier for the job.

    Returns:
        A string containing JSON-formatted job information or an error message.
    """
    if not scheduler:
        return "❌ Scheduler not available."

    try:
        job = await ensure_async(scheduler.get_job(job_id))
        return f"🔍 Job {job_id}:\n" + json.dumps(job, indent=2)
    except Exception as e:
        return f"❌ Failed to get job {job_id}: {str(e)}"


async def scheduler_cancel_job(scheduler, job_id: str) -> str:
    """
    Cancel a job by its ID.

    Parameters:
        scheduler: The Scheduler instance to use.
        job_id: The unique identifier for the job to cancel.

    Returns:
        A string message indicating whether the job was successfully cancelled.
    """
    if not scheduler:
        return "❌ Scheduler not available."

    try:
        await ensure_async(scheduler.cancel_job(job_id))
        return f"❌ Job {job_id} cancelled."
    except Exception as e:
        return f"❌ Failed to cancel job {job_id}: {str(e)}"