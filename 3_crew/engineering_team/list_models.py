import os
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = os.environ.get("base_url")
api_key = os.environ.get("GENERATIVE_ENGINE_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    response = requests.get(f"{base_url}/models", headers=headers)
    response.raise_for_status()
    models = response.json()
    print("Available models:")
    if "data" in models:
        for model in models["data"]:
            print(f"- {model.get('id')}")
    else:
        print(models)
except Exception as e:
    print("Error fetching models:")
    print(e)
    if hasattr(e, 'response') and e.response is not None:
        print(e.response.text)
