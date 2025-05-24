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

def watch_for_new_input():
    last_query = ""

    print("Waiting for new input in input.txt...")

    while True:
        if os.path.exists(INPUT_FILE):
            with open(INPUT_FILE, 'r') as f:
                query = f.read().strip()

            # Check for new entry
            if query and query != last_query:
                print(f"New input detected: {query}")
                image_url = search_unsplash_image(query)

                if image_url:
                    with open(OUTPUT_FILE, 'w') as f:
                        f.write(image_url)
                    print(f"Image URL written to {OUTPUT_FILE}")
                else:
                    print("No image found.")

                last_query = query

        time.sleep(2)  # Check every 2 seconds


# TESTING
if __name__ == "__main__":
    print("Put a mood or genre into input.txt and run this script.")
    run_once()
