import asyncio
from fastmcp import Client

async def client_main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        if client.is_connected:
            print("Connected to MCP Server")
        
        tools = await client.list_tools()
        print("\n---- Available Tools ----")
        for tool in tools:
            print(f"\n{tool.name}: {tool.description}")
            
            # Call the tool
            response = await client.call_tool(tool.name, {"a": 21, "b": 7})
            print("---- Tool Response ----")
            print(response)

if __name__ == "__main__":
    asyncio.run(client_main())
