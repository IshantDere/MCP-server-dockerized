from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Math MCP Server")

# Define a tool
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    # Run over stdio (default for MCP)
    mcp.run()
