import requests
import time
import os

UNSPLASH_ACCESS_KEY = '-5c124BZyGqc6wr5E2bY-xj3PkeGGGG0Eb-UgxzGLs0'  # Replace with your access key if needed

INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'

def search_unsplash_image(query):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "client_id": UNSPLASH_ACCESS_KEY,
        "per_page": 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "results" in data and data["results"]:
        return data["results"][0]["urls"]["regular"]
    else:
        return None

def run_once():
    if not os.path.exists(INPUT_FILE):
        print("Waiting for input.txt to be created...")
        return

    with open(INPUT_FILE, 'r') as f:
        query = f.read().strip()

    if not query:
        print("No query found in input.txt.")
        return

    print(f"Searching Unsplash for: {query}")
    image_url = search_unsplash_image(query)

    if image_url:
        with open(OUTPUT_FILE, 'w') as f:
            f.write(image_url)
        print(f"Image URL written to {OUTPUT_FILE}")
    else:
        print("No image found.")

# TESTING
    print("Put a mood or genre into input.txt and run this script.")
    run_once()
