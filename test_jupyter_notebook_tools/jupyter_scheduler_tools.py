async def scheduler_create_job(
    notebook_path: str,
    name: str = "Scheduled Job",
    cron_schedule: str = None
) -> str:
    """
    Schedule a notebook to be executed, optionally on a recurring basis using cron.

    Parameters:
        notebook_path (str): Path to the notebook in the Jupyter file system.
        name (str): A name for the job.
        cron_schedule (str): Optional cron string for recurrence (e.g., "0 * * * *").

    Returns:
        str: Job ID or error message.
    """
    job_data = {
        "name": name,
        "path": notebook_path
    }
    if cron_schedule:
        job_data["cron_schedule"] = cron_schedule

    try:
        job_request = JobRequest(**job_data)
        job = await ensure_async(scheduler.create_job(job_request))
        return f"✅ Job created with ID: {job.id}"
    except Exception as e:
        return f"❌ Failed to create job: {str(e)}"



async def scheduler_list_jobs() -> str:
    """
    Return a list of all scheduled jobs.

    Returns:
        str: A JSON-formatted list of jobs or error message.
    """
    try:
        jobs = await ensure_async(scheduler.list_jobs())
        return f"📋 Jobs:\n" + json.dumps([job.dict() for job in jobs], indent=2)
    except Exception as e:
        return f"❌ Failed to list jobs: {str(e)}"



async def scheduler_get_job(job_id: str) -> str:
    """
    Fetch metadata and status for a specific job.

    Parameters:
        job_id (str): The job's unique ID.

    Returns:
        str: A JSON-formatted string of job info or error message.
    """
    try:
        job = await ensure_async(scheduler.get_job(job_id))
        return f"🔍 Job {job_id}:\n" + json.dumps(job.dict(), indent=2)
    except Exception as e:
        return f"❌ Failed to get job {job_id}: {str(e)}"



async def scheduler_cancel_job(job_id: str) -> str:
    """
    Cancel a scheduled job by ID.

    Parameters:
        job_id (str): The job's unique ID.

    Returns:
        str: Success or error message.
    """
    try:
        await ensure_async(scheduler.cancel_job(job_id))
        return f"❌ Job {job_id} cancelled."
    except Exception as e:
        return f"❌ Failed to cancel job {job_id}: {str(e)}"

