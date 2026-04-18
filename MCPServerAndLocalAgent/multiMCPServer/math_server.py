from fastmcp import FastMCP

mcp = FastMCP(name="CalculatorServer")

@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integers together."""
    return a + b

@mcp.tool
def subract(a: int, b: int) -> int:
    """Subtracts two integers."""
    return abs(a - b)

@mcp.tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

@mcp.tool
def divide(a: int, b: int) -> int:
    """Division of first from the second."""
    return a // b

@mcp.tool
def expo(a: int, b: int) -> int:
    """Exponential of first integer."""
    return a ** b

if __name__ == "__main__":
    # mcp.run(transport="stdio")
    mcp.run(transport="streamable-http", port=8002)