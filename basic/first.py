from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

mcp=FastMCP(
    name="Calculator"
)

@mcp.tool()
def sum(a:int, b:int) -> int:
    """Add the numbers together"""
    return a+b

if __name__=="__main__":
    mcp.run(transport="stdio")