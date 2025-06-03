# spotify_auth.py
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from predict_mood import predicted_mood

sp = Spotify(
    auth_manager=SpotifyOAuth(
        client_id="b82f472dc67c4fac8d959873093708ae",
        client_secret="7e6d741868f647d88d31ca33eade47c8",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-modify-playback-state user-read-playback-state",
    )
)

# Test: Get current playback
current = sp.current_playback()
if current and current["is_playing"]:
    print("Currently playing:", current["item"]["name"])
else:
    print("No music playing.")

mood_to_playlist = {
    "chill": "spotify:playlist:37i9dQZF1DX4WYpdgoIcn6",
    "focus": "spotify:playlist:37i9dQZF1DX8NTLI2TtZa6",
    "party": "spotify:playlist:37i9dQZF1DXaXB8fQg7xif",
    "romantic": "spotify:playlist:37i9dQZF1DWXbttAJcbphz",
    "energetic": "spotify:playlist:37i9dQZF1DX1g0iEXLFycr",
}

playlist_uri = mood_to_playlist[predicted_mood]

# Find active device
devices = sp.devices()
if devices["devices"]:
    device_id = devices["devices"][0]["id"]  # Use the first available device
    sp.transfer_playback(device_id=device_id, force_play=True)
    sp.start_playback(device_id=device_id, context_uri=playlist_uri)
else:
    print(
        "No active Spotify device found. Please open Spotify on your computer or phone and try again."
    )
