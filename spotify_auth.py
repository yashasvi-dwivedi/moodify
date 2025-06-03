# spotify_auth.py
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

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
