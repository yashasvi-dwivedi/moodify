# 🎧 Moodify – Mood-Based Lighting & Spotify Music Control

Moodify is a Python-based application that detects your mood using a webcam, adjusts the lighting in your room, and plays mood-appropriate music on Spotify. It leverages deep learning for emotion recognition, smart lighting control, and seamless Spotify integration—making your environment match your feelings.

---

## 🌟 Features

- 🧠 **Mood Detection** using webcam + ResNet18 deep learning model
- 💡 **Smart Lighting** that matches your current emotion
- 🎵 **Spotify Integration** for auto-playing mood-matching playlists
- 📊 **Confusion Matrix & Accuracy Evaluation** for model performance
- 🖥️ Optional GUI or Web App (Flask or Tkinter)

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yashasvi-dwivedi/moodify.git
   cd moodify
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   **Main dependencies:**
   - Python 3.8+
   - torch, torchvision
   - opencv-python
   - pillow
   - spotipy
   - requests

4. **Download/prepare a trained model:**
   - Place your `model.pth` (ResNet18 trained on mood images) in the root directory.

5. **Spotify API setup:**
   - Register your app on [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Replace `client_id`, `client_secret`, and `redirect_uri` in `spotify_auth.py` with your credentials.
   - Ensure your Spotify app has the correct redirect URI.

6. **Unsplash API setup (for dataset preparation):**
   - Get an Unsplash Access Key at [Unsplash Developers](https://unsplash.com/developers).
   - Replace it in `download_images.py`.

---

## 🚀 Usage

### 1. Download images for training (optional)
```bash
python download_images.py
```

### 2. Capture your mood via webcam and predict
```bash
python predict_mood.py
```
- Press `SPACE` to capture an image.
- The predicted mood will be displayed in the terminal.

### 3. Play mood-based music on Spotify
```bash
python spotify_auth.py
```
- Opens Spotify on your device and plays a playlist matching your mood.
- Make sure Spotify is running and a device is active.

---

## 📁 Folder Structure

```
moodify/
│
├── download_images.py         # Download dataset images from Unsplash
├── predict_mood.py            # Webcam capture + mood detection
├── spotify_auth.py            # Spotify authentication & playback
├── model.pth                  # Trained ResNet18 model (not included)
├── requirements.txt           # Python dependencies
├── images/                    # Downloaded images for training
├── README.md                  # Project readme
└── ...
```

---

## 🤖 How it Works

1. **Image Capture:** Uses OpenCV to capture an image from your webcam.
2. **Mood Prediction:** ResNet18 model predicts one of: `chill`, `focus`, `party`, `romantic`, `energetic`.
3. **Lighting Control:** (Optional, requires integration with smart lights, e.g., Philips Hue).
4. **Spotify Playback:** Authenticates with Spotify and plays a playlist matching your mood.

---

## 📝 Customization

- **Add more moods:** Add new class labels in `predict_mood.py`, retrain your model, and update `mood_to_playlist` in `spotify_auth.py`.
- **Smart Lights:** Integrate your preferred smart lighting API for full automation.

---

## ⚠️ Notes

- You must have a webcam and an active Spotify account.
- The trained model (`model.pth`) is not included for copyright/privacy.
- API keys (Spotify, Unsplash) must be kept secure and are rate-limited.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- [PyTorch](https://pytorch.org/)
- [Spotipy](https://spotipy.readthedocs.io/)
- [Unsplash](https://unsplash.com/developers)
- [OpenCV](https://opencv.org/)

---

**Happy Moodifying! 🎶💡**
