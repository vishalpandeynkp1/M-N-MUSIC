import os
from pyrogram import Client, filters
import youtube_dl

from BADMUSIC import app

# Function to download audio from YouTube
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        return f"{info_dict['title']}.mp3"

@app.on_message(filters.command("song"))
def download_song(client, message):
    if len(message.command) < 2:
        message.reply("Please provide a YouTube link.")
        return

    url = message.command[1]
    try:
        audio_file = download_audio(url)
        app.send_audio(chat_id=message.chat.id, audio=audio_file)
        os.remove(audio_file)  # Clean up the downloaded file
    except Exception as e:
        message.reply(f"An error occurred: {str(e)}")
