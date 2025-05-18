from . import ynotebook_tools
from . import git_tools
from . import jupyter_scheduler_tools




def jupyter_server_extension_tools() -> dict:
    return {
        "delete_cell": {
            "metadata": {
                "name": "delete_cell",
                "description": "Remove the cell at the specified index and return its contents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "index": {"type": "integer", "description": "The index of the cell to delete"}
                    },
                    "required": ["index"]
                }
            },
            "callable": ynotebook_tools.delete_cell
        },
        "add_cell": {
            "metadata": {
                "name": "add_cell",
                "description": "Insert a blank cell at the specified index.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "index": {"type": "integer", "description": "The index to insert at"},
                        "cell_type": {"type": "string", "description": "The type of cell", "default": "code"},
                    },
                    "required": ["index"]
                }
            },
            "callable": ynotebook_tools.add_cell
        },
        "write_to_cell": {
            "metadata": {
                "name": "write_to_cell",
                "description": "Overwrite the source of a cell with content at the given index in the notebook.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "index": {"type": "integer", "description": "The index to write at"},
                        "content": {"type": "string", "description": "The content to write into the cell"},
                    },
                    "required": ["index", "content"]
                }
            },
            "callable": ynotebook_tools.write_to_cell
        },
        "get_max_cell_index": {
            "metadata": {
                "name": "get_max_cell_index",
                "description": "Return the highest valid cell index in the current notebook.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            },
            "callable": ynotebook_tools.get_max_cell_index
        },
        "read_cell": {
            "metadata": {
                "name": "read_cell",
                "description": "Read the full content of a specific cell, including outputs, source, and metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "index": {"type": "integer", "description": "The index of the cell to read"}
                    },
                    "required": ["index"]
                }
            },
            "callable": ynotebook_tools.read_cell
        },
        "read_notebook": {
            "metadata": {
                "name": "read_notebook",
                "description": "Return all cells in the notebook as a JSON-formatted list.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            },
            "callable": ynotebook_tools.read_notebook
        },
         "git_clone": {
            "metadata": {
                "name": "git_clone",
                "description": "Clone a Git repo into the specified path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Target path"},
                        "url": {"type": "string", "description": "Repository URL"}
                    },
                    "required": ["path", "url"]
                }
            },
            "callable": git_tools.git_clone
        },
        "git_status": {
            "metadata": {
                "name": "git_status",
                "description": "Get the current Git status in the specified path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Repo path"},
                    },
                    "required": ["path"]
                }
            },
            "callable": git_tools.git_status
        },
        "git_log": {
            "metadata": {
                "name": "git_log",
                "description": "Get the last N Git commits.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Repo path"},
                        "history_count": {"type": "integer", "default": 10, "description": "Number of commits"}
                    },
                    "required": ["path"]
                }
            },
            "callable": git_tools.git_log
        },
        "git_pull": {
            "metadata": {
                "name": "git_pull",
                "description": "Pull the latest changes from the remote.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Repo path"}
                    },
                    "required": ["path"]
                }
            },
            "callable": git_tools.git_pull
        },
        "git_push": {
            "metadata": {
                "name": "git_push",
                "description": "Push local changes to the remote.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Repo path"}, 
                        "branch": {"type": "string", "description": "REpo branch"}
                    },
                    "required": ["path"]
                }
            },
            "callable": git_tools.git_push
        },
        "git_commit": {
            "metadata": {
                "name": "git_commit",
                "description": "Commit staged changes with a message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Repo path"},
                        "message": {"type": "string", "description": "Commit message"}
                    },
                    "required": ["path", "message"]
                }
            },
            "callable": git_tools.git_commit
        },
        "git_add": {
            "metadata": {
                "name": "git_add",
                "description": "Stage files for commit. Optionally add all files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Repo path"},
                        "add_all": {"type": "boolean", "default": True, "description": "Stage all files"},
                        "filename": {"type": "string", "description": "File to add (used if add_all is false)"}
                    },
                    "required": ["path"]
                }
            },
            "callable": git_tools.git_add
        },
        "git_get_repo_root_from_notebookpath": {
            "metadata": {
                "name": "git_get_repo_root_from_notebookpath",
                "description": "Given the path of a file, return the path to the Repo root, if any.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "notebook path"},
                    },
                    "required": ["path"]
                }
            },
            "callable": git_tools.git_get_repo_root
        },
                "scheduler_create_job": {
            "metadata": {
                "name": "scheduler_create_job",
                "description": "Create a new scheduled job to run a notebook, optionally with a cron schedule.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "notebook_path": {
                            "type": "string",
                            "description": "Path to the notebook to schedule (e.g., '/path/to/notebook.ipynb')"
                        },
                        "name": {
                            "type": "string",
                            "description": "A name for the job",
                            "default": "Scheduled Job"
                        },
                        "cron_schedule": {
                            "type": "string",
                            "description": "Optional cron schedule string for recurrence (e.g., '0 * * * *')"
                        }
                    },
                    "required": ["notebook_path"]
                }
            },
            "callable": jupyter_scheduler_tools.scheduler_create_job
        },
        "scheduler_list_jobs": {
            "metadata": {
                "name": "scheduler_list_jobs",
                "description": "List all scheduled jobs.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            },
            "callable": jupyter_scheduler_tools.scheduler_list_jobs
        },
        "scheduler_get_job": {
            "metadata": {
                "name": "scheduler_get_job",
                "description": "Get details about a specific job.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {
                            "type": "string",
                            "description": "The unique ID of the job to look up"
                        }
                    },
                    "required": ["job_id"]
                }
            },
            "callable": jupyter_scheduler_tools.scheduler_get_job
        },
        "scheduler_cancel_job": {
            "metadata": {
                "name": "scheduler_cancel_job",
                "description": "Cancel a scheduled job by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {
                            "type": "string",
                            "description": "The unique ID of the job to cancel"
                        }
                    },
                    "required": ["job_id"]
                }
            },
            "callable": jupyter_scheduler_tools.scheduler_cancel_job
        },
        "scheduler_run_job": {
            "metadata": {
                "name": "scheduler_run_job",
                "description": "Run a job immediately by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {
                            "type": "string",
                            "description": "The unique ID of the job to run"
                        }
                    },
                    "required": ["job_id"]
                }
            },
            "callable": jupyter_scheduler_tools.scheduler_run_job
        }



    }

