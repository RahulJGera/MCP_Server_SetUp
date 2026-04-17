pip3 install uv
uv add fastmcp dotenv mcp
cd BuildFirstMCPServer/demo-server/
uv run ./server.py
uv run ./client_mcp.py
