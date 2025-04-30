from jupyter_ydoc import YNotebook  # assuming you're using this YNotebook
import asyncio
import json






async def delete_cell(ynotebook: YNotebook, index: int) -> str:
    """Remove the cell at the specified index and return its contents."""
    try:
        cell = ynotebook.get_cell(index)
        ynotebook._ycells.pop(index)
        return f"✅ Cut cell {index} :\n{cell['source']}"
    except Exception as e:
        return f"❌ Error cutting cell {index}: {str(e)}"



async def write_to_cell(ynotebook: YNotebook, index: int, content: str, stream=True) -> str:
    """Overwrite the source of a cell in the notebook at given path."""
    try:
        ycell = ynotebook.get_cell(index)

        # Streaming cell changes... so it looks like an AI is typing.
        if stream:
            for item in list(content):
                ycell["source"] += item
                ynotebook.set_cell(index, ycell)
                await asyncio.sleep(.01)
        else:
            ycell["source"] = content
        
        return f"✅ Updated cell {index}."
    except Exception as e:
        return f"❌ Error writing to cell {index}: {str(e)}"


async def add_cell(ynotebook: YNotebook, index: int, cell_type: str = "code") -> str:
    """Insert a blank cell at the specified index in the notebook at given path."""
    try:
        new_cell = {
            "cell_type": cell_type,
            "source": "",
            "metadata": {},
        }
        if cell_type == "code":
            new_cell["outputs"] = [] 
            new_cell["execution_count"] = None
            
        ycell = ynotebook.create_ycell(new_cell)
        ynotebook._ycells.insert(index, ycell)
        
        
        return f"✅ Added {cell_type} cell at index {index}."
    except Exception as e:
        return f"❌ Error adding cell at index {index}: {str(e)}"


async def get_max_cell_index(ynotebook: YNotebook) -> int:
    """Return the index of the last cell in the notebook."""
    try:
        return len(ynotebook._ycells) - 1
    except Exception as e:
        raise RuntimeError(f"❌ Error getting max cell index: {str(e)}")



async def read_cell(ynotebook: YNotebook, index: int) -> str:
    """
    Reads the full content of a specific cell in a YNotebook,
    including its type, execution count, metadata, outputs, and source.
    """
    try:
        if 0 <= index < len(ynotebook._ycells):
            cell_data = ynotebook.get_cell(index)
            return json.dumps(cell_data, indent=2)
        else:
            return f"❌ Invalid cell index: {index}"
    except Exception as e:
        return f"❌ Error reading cell {index}: {str(e)}"



async def read_notebook(ynotebook: YNotebook) -> str:
    """
    Returns the full notebook content as a JSON-formatted list of cells.
    """
    try:
        cells = [ynotebook.get_cell(i) for i in range(len(ynotebook._ycells))]
        return json.dumps(cells, indent=2)
    except Exception as e:
        return f"❌ Error reading notebook: {str(e)}"