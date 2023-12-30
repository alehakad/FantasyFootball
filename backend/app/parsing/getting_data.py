import requests
import dotenv
import os

base_url = "https://api.sportmonks.com/v3/football"

dotenv.load_dotenv()

r = requests.get(
    f"{base_url}/fixtures",
    headers={"Authorization": os.environ.get("sportmonks_token")},
)

print(r.json())
