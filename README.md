# jupyter_ydoc_tools

**A Jupyter Server Extension for Real-Time Notebook Manipulation with YNotebook and AI Personas**

This extension exposes a collection of tools for manipulating live Jupyter notebooks using [YNotebook](https://github.com/jupyter/ydoc). It is designed for use with AI personas and LLM agents (e.g. LangGraph, CrewAI, or Jupyter AI v3) that need to read from or write to notebooks collaboratively and in real time.

> ✨ Supports character-by-character streaming edits, cell creation, and full notebook inspection — all with awareness of Yjs CRDTs.

---

## 🚀 Features

- 📌 **`write_to_cell`**: Streams character-level diffs into notebook cells to simulate real-time typing  
- ✂️ **`delete_cell`**: Deletes a cell and returns its contents  
- ➕ **`add_cell`**: Inserts a new blank cell at any index  
- 🔍 **`read_cell`**: Reads the full JSON structure of a cell, including source, outputs, metadata  
- 📖 **`read_notebook`**: Dumps the full notebook as a list of cell JSON objects  
- 🔢 **`get_max_cell_index`**: Returns the last valid cell index in the current notebook  

These tools are useful for LLM-powered workflows that aim to *collaborate* with users, not just autocomplete for them.

---

## 🧩 How it Works

The extension uses the standard Jupyter server extension discovery mechanism (`jupyter_server_extension_tools`) to expose a dictionary of callable tools along with metadata and parameter schemas.

Each tool accepts a live `YNotebook` instance (injected at runtime) and performs operations using Yjs-compatible APIs. Some tools stream their actions using `asyncio.sleep` to simulate AI typing behavior.

---

## 🛠 Example Tool

```python
await write_to_cell(ynotebook, index=1, content="print('Hello world')", stream=True)
```

This will:
* Diff the existing content vs. the new content
* Simulate deletions (in reverse)
* Stream insertions character-by-character


## 📦 Installation

```bash
pip install jupyter-ydoc-tools
jupyter server extension enable jupyter_ydoc_tools
```

## 🧠 Use with AI Personas

If you're building an AI persona using LangGraph, LangChain, or Agno that operates inside JupyterLab, this extension enables your agent to:
* Discover tools at runtime (via list_ai_tools())
* Access live notebook state
* Modify cells interactively

## 📚 License
MIT © 2024 Your Name


## 🙋 Contributing
PRs welcome! Open an issue if you find a bug or want to suggest a new tool.
Let me know if you'd like a matching `pyproject.toml`, GitHub Actions workflow, or usage examples in LangGraph or Agno.

