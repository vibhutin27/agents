import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

base_url = os.environ.get("base_url")
api_key = os.environ.get("GENERATIVE_ENGINE_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(f"{base_url}/models", headers=headers)
models = response.json()
with open("available_models.json", "w") as f:
    json.dump(models, f, indent=2)
