# 🎵 YouTube to MP3 Downloader

A simple Python project that downloads YouTube videos and automatically converts them into high-quality MP3 audio files.

Built using:
- Python
- yt-dlp
- FFmpeg

---

# ✨ Features

✅ Download YouTube videos as MP3  
✅ Automatic audio conversion  
✅ High quality audio (192kbps)  
✅ Fast downloading using yt-dlp  
✅ Simple terminal interface  
✅ Auto creates downloads folder  
✅ Supports most YouTube links  

---

# 📁 Project Structure

```bash
youtube_mp3_downloader/
│
├── main.py
├── requirements.txt
├── README.md
└── downloads/
```

---

# ⚙️ Requirements

Install:

- Python 3.9+
- FFmpeg
- yt-dlp

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/youtube_mp3_downloader.git
cd youtube_mp3_downloader
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔥 Install FFmpeg (IMPORTANT)

This project requires FFmpeg for MP3 conversion.

## Windows

### Step 1:
Download FFmpeg:

https://ffmpeg.org/download.html

### Step 2:
Extract ZIP file

### Step 3:
Add FFmpeg `bin` folder to PATH

Example:

```bash
C:\ffmpeg\bin
```

### Step 4:
Verify installation

```bash
ffmpeg -version
```

If version appears → FFmpeg installed correctly ✅

---

# 🚀 Run Project

```bash
python main.py
```

Paste YouTube URL:

```bash
https://youtube.com/watch?v=xxxxx
```

MP3 file will be saved inside:

```bash
downloads/
```

---

# 🧠 Example Output

```bash
Enter YouTube URL:
https://youtu.be/example

[download] 100% completed
[ExtractAudio] Destination: downloads/song.mp3

✅ Download Complete!
```

---

# 🛠️ Main Technologies

| Technology | Purpose |
|---|---|
| Python | Core language |
| yt-dlp | Download YouTube videos |
| FFmpeg | Convert audio to MP3 |

---

# 📌 Tips

## 1. Always Update yt-dlp

YouTube changes frequently.

Update regularly:

```bash
pip install -U yt-dlp
```

---

## 2. Fix HTTP 403 Errors

If you get:

```bash
HTTP Error 403: Forbidden
```

Use:

```python
'cookiesfrombrowser': ('chrome',)
```

inside `ydl_opts`.

---

## 3. Use Chrome Login

Being logged into YouTube in Chrome helps avoid restrictions.

---

## 4. Keep FFmpeg in PATH

Without FFmpeg:
- Download works
- MP3 conversion fails ❌

---

## 5. Use Short Videos for Testing

Testing with:
- music videos
- podcasts
- short clips

is faster while developing.

---

# 🔒 Disclaimer

This project is for educational purposes only.

Please respect:
- YouTube Terms of Service
- Copyright laws
- Content creator rights

---

# 💡 Future Improvements

You can enhance this project with:

- GUI using Tkinter
- Playlist downloading
- Batch downloads
- Drag & drop support
- Download progress bar
- Flask/FastAPI web app
- Spotify metadata tagging
- Thumbnail downloading
- Subtitle downloading

---

# ⭐ Recommended Libraries

## yt-dlp

Modern and actively maintained downloader.

GitHub:
https://github.com/kunal-rajput-317/song-downloader-

---

# 👨‍💻 Author - kunal-rajut-317

Made with Python ❤️