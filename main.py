import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Open_AI_Key=", os.getenv("OPENAI_API_KEY"))
    print("Claude_AI_Key=", os.getenv("CLAUDE_API_KEY"))
    print("LangSmith_AI_Key=", os.getenv("LANGSMITH_API_KEY"))
    print("Hello from mcp-server-setup!")


if __name__ == "__main__":
    main()
