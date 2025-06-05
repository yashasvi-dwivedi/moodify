import os
import requests
import time

UNSPLASH_ACCESS_KEY = "YOUR_ACCESS_KEY"  # ← replace this with your actual key

headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}

mood_keywords = {
    "chill": ["cozy room lighting", "ambient lights"],
    "focus": ["study desk light", "minimalist workspace"],
    "party": ["neon party lights", "led room party"],
    "romantic": ["romantic room lighting", "candle light bedroom"],
    "energetic": ["vibrant colorful room", "bright neon lights"],
}

BASE_FOLDER = "images"
os.makedirs(BASE_FOLDER, exist_ok=True)


def download_images_for_mood(mood, keywords, total_images=30):
    per_query = total_images // len(keywords)
    mood_folder = os.path.join(BASE_FOLDER, mood)
    os.makedirs(mood_folder, exist_ok=True)
    img_count = 0

    for keyword in keywords:
        page = 1
        while img_count < total_images:
            url = "https://api.unsplash.com/search/photos"
            params = {"query": keyword, "per_page": min(per_query, 10), "page": page}

            response = requests.get(url, headers=headers, params=params)
            data = response.json()

            for result in data.get("results", []):
                img_url = result["urls"]["regular"]
                try:
                    img_data = requests.get(img_url).content
                    filename = f"{mood}_{img_count}.jpg"
                    filepath = os.path.join(mood_folder, filename)

                    with open(filepath, "wb") as f:
                        f.write(img_data)

                    print(f"[{mood}] Saved: {filepath}")
                    img_count += 1

                    if img_count >= total_images:
                        break

                except Exception as e:
                    print(f"[{mood}] Failed to save image: {e}")

            page += 1
            time.sleep(1)


print("Starting download...")
for mood, keywords in mood_keywords.items():
    download_images_for_mood(mood, keywords, total_images=50)

print("Download complete.")
