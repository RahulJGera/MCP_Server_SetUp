import asyncio
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient

async def main():

    # Create MCPClient from configuration JSON file.
    client = MCPClient("/home/rj0402g/Documents/Learning/Practice/MCP_Server_SetUp/RAGusingMCP/mcp-json.json")

    # Create LLM
    llm =ChatOllama(base_url="http://localhost:11434", model="qwen3.5")

    # Create agent with restricted tools
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=30,
        disallowed_tools=["file_system", "network"]  # Restrict potentially dangerous tools
        # use_server_manager=True,
    )

    # Run the query
    result = await agent.run(
        "how many collections are in my RAG DB",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())