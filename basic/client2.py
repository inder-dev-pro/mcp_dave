from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def run():
    # Launch the MCP server defined in first.py via stdio so both run together
    server_script = Path(__file__).with_name("first.py").resolve()

    server_params = StdioServerParameters(
        command="python",
        args=[str(server_script)],
        env=None,
    )

    async with stdio_client(server_params) as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [t.name for t in tools.tools])

            result = await session.call_tool("sum", {"a": 3, "b": 6})
            print("Result from sum tool:", result.content[0])


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())