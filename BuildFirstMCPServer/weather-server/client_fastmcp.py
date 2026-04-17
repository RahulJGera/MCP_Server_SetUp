import asyncio
from fastmcp import Client

async def client_main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        if client.is_connected:
            print("Connected to MCP Server")
        
        # List of available tools
        tools = await client.list_tools()
        print("\n---- Available Tools ----")
        for tool in tools:
            print(f"\n{tool.name}: {tool.description}")
            
            # Call the tool
            response = await client.call_tool(tool.name, {"location": "Sunnyvale"})
            print("---- Tool Response ----")
            print(response)
            print(response.data)

if __name__ == "__main__":
    asyncio.run(client_main())
