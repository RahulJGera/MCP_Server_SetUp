import asyncio
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient

async def main():

    # Create MCPClient from configuration JSON file.
    client = MCPClient("/home/rj0402g/Documents/Learning/Practice/MCP_Server_SetUp/MCPServerforDataAnalysis/data/mcp-json.json")

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
        "Analyse the xlsx extension file located in /home/rj0402g/Documents/Learning/Practice/MCP_Server_SetUp/MCPServerforDataAnalysis/data/support_tickets_data.xlsx, and analyse the support_tickets_data sheet and generate a comprehensive analysis and save it into a content_data_analysis tab in the same excel file.",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())