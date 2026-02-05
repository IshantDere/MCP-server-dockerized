import asyncio
from fastmcp import Client


async def main() -> None:
    client = Client("http://136.111.109.186:8000/mcp")
    async with client:
        result = await client.call_tool("add", {"a": 20, "b": 33})
        print(result)


if __name__ == "__main__":
    asyncio.run(main())