import asyncio
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient

async def main():

    # Create MCPClient from configuration JSON file.
    # client = MCPClient("/home/rj0402g/Documents/Learning/Practice/MCP_Server_SetUp/MCPServerAndLocalAgent/weather-server/mcp-json.json")
    client = MCPClient("/home/rj0402g/Documents/Learning/Practice/MCP_Server_SetUp/MCPServerAndLocalAgent/weather-server/mcp-http.json")
    # client = MCPClient()

    # Create LLM
    llm =ChatOllama(base_url="http://localhost:11434", model="qwen3.5")

    # Create agent with restricted tools
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=30,
        use_server_manager=True,
        disallowed_tools=["file_system", "network"]  # Restrict potentially dangerous tools
    )

    # Run the query
    result = await agent.run(
        "What is the current weather in Santa Clara, California and the three day forecast, if possible. Also tell me the exponential of two with power of five.",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())