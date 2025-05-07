from . import tools

def jupyter_server_extension_points():
    return [{
        "module": "test_jupyter_notebook_tools"
    }]

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
            "callable": tools.delete_cell
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
            "callable": tools.add_cell
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
            "callable": tools.write_to_cell
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
            "callable": tools.get_max_cell_index
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
            "callable": tools.read_cell
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
            "callable": tools.read_notebook
        }
    }


def _load_jupyter_server_extension(serverapp):
    serverapp.log.info("✅ test_jupyter_notebook_toolss extension loaded.")