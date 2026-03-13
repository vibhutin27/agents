import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

print("Using base_url:", os.environ.get("base_url"))
print("Using api_key:", "SET" if os.environ.get("GENERATIVE_ENGINE_API_KEY") else "NOT SET")

llm = ChatOpenAI(
    model="gpt-4",
    base_url=os.environ.get("base_url"),
    api_key=os.environ.get("GENERATIVE_ENGINE_API_KEY")
)

try:
    response = llm.invoke("Hello, who are you?")
    print("SUCCESS!")
    print(response.content)
except Exception as e:
    print("FAILED!")
    print(e)
