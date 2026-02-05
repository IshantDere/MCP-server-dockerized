# app/server.py
from fastmcp import FastMCP

mcp = FastMCP("add-server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers and return the result
    """
    return a + b

# Expose as ASGI app for uvicorn
app = mcp.app
