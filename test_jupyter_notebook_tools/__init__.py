from .extension import jupyter_server_extension_tools

__all__ = ["jupyter_server_extension_tools"]

__version__ = "0.1.0"



def _load_jupyter_server_extension(serverapp):
    serverapp.log.info("[test_jupyter_notebook_tools] Server extension loaded (tool discovery only).")

def _jupyter_server_extension_points():
    return [{
        "module": "test_jupyter_notebook_tools.extension",
    }]