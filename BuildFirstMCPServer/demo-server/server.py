from fastmcp import FastMCP

mcp = FastMCP(name="CalculatorServer")

@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b

@mcp.tool
def sub(a: int, b: int) -> int:
    """Subtracts two integer numbers together."""
    return abs(a - b)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")