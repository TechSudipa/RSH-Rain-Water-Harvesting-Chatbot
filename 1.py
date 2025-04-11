from dotenv import load_dotenv
import os

load_dotenv()

mistral_api_key = os.getenv("MISTRAL_KEY")
print(f"MISTRAL_KEY: {mistral_api_key}")
