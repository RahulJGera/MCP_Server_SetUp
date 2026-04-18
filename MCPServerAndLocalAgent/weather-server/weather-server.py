import httpx
from fastmcp import FastMCP

# Create Fast MCP Server
mcp = FastMCP(name="Weather Server")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get Current weather for a location"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://wttr.in/{location}?format=j1")
        data = response.json()

        current = data.get("current_condition")[0]
        city = data.get("nearest_area")[0].get("areaName")[0].get("value")
        state = data.get("nearest_area")[0].get("region")[0].get("value")
        country = data.get("nearest_area")[0].get("country")[0].get("value")

        return f"Weather in {city}, {state}, {country}: {current.get("temp_F")}°F, {current.get("weatherDesc")[0].get("value")}"

@mcp.tool()
async def get_forecast(location: str) -> str:
    """Get 3-day weather forecast"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://wttr.in/{location}?format=j1")
        data = response.json()

        result = f"3-day forecast for {location}:\n"
        for day in data.get("weather")[:3]:
            result += f"{day.get("date")}: {day.get("mintempF")}-{day.get("maxtempF")}°F\n"
        return result

if __name__ == "__main__":
    # mcp.run(transport="stdio")
    mcp.run(transport="streamable-http", port=8001)