import os
import requests
from dotenv import load_dotenv

# Load API token from .env
load_dotenv()

API_TOKEN = os.getenv("FOOTBALL_API_TOKEN")

BASE_URL = "https://api.football-data.org/v4"

headers = {
    "X-Auth-Token": API_TOKEN
}

    