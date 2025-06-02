import requests
import os
import time

ACCESS_KEY = (
    "ei694l_gFOCG6q-IEXXaGxWM42bPst2WGa1KG3piYHg"  # Replace with your actual key
)


def download_unsplash_images(keyword, count, label):
    headers = {"Authorization": f"Client-ID {ACCESS_KEY}"}
    search_url = "https://api.unsplash.com/search/photos"
    params = {"query": keyword, "per_page": count}

    image_folder = f"images/{label}"
    os.makedirs(image_folder, exist_ok=True)

    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Search failed for {keyword}: {response.status_code}, {response.text}")
        return []

    data = response.json()
    results = data.get("results", [])
    metadata = []

    for i, item in enumerate(results):
        img_url = item["urls"]["regular"]
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img_path = os.path.join(image_folder, f"{label}_{i}.jpg")
            with open(img_path, "wb") as f:
                f.write(img_response.content)
            metadata.append({"filename": img_path, "label": label, "keyword": keyword})
            print(f"Downloaded: {img_path}")
            time.sleep(1)
        else:
            print(f"Failed to download image {i} for keyword {keyword}")

    return metadata


# Example mood categories
mood_keywords = {
    "chill": "cozy room lighting",
    "focus": "minimalist desk setup",
    "party": "led room lights",
    "romantic": "warm bedroom lights",
    "energetic": "bright colorful room",
}

import pandas as pd

all_metadata = []

for mood, keyword in mood_keywords.items():
    meta = download_unsplash_images(keyword, count=10, label=mood)
    all_metadata.extend(meta)

df = pd.DataFrame(all_metadata)
df.to_csv("moodify_image_labels.csv", index=False)
print("✅ All images downloaded and labeled.")
