pip3 install uv
uv add fastmcp dotenv mcp
cd BuildFirstMCPServer/demo-server/
uv run ./server.py
uv run ./client_mcp.py
uv run ./client_fastmcp.py
cd ../weather-server
uv run ./server.py
uv run ./client_fastmcp.py