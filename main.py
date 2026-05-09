import os
from yt_dlp import YoutubeDL

DOWNLOAD_FOLDER = "downloads"

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_mp3(url):

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',

        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),

        'quiet': False,

        'noplaylist': True,

        'extractaudio': True,

        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],

        # IMPORTANT FIXES
        'http_headers': {
            'User-Agent': 'Mozilla/5.0'
        },

        'extractor_args': {
            'youtube': {
                'player_client': ['android']
            }
        }
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("\n✅ MP3 Downloaded Successfully!")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    youtube_url = input("Enter YouTube Video URL: ")
    download_mp3(youtube_url)