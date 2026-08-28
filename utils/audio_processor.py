import yt_dlp
from pydub import AudioSegment
import os

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_audio_from_youtube(url, output_format="mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': output_format,
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        title = info_dict.get('title', None)
        filename = f"{title}.{output_format}"
        return os.path.join(DOWNLOAD_DIR, filename)

data = download_audio_from_youtube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def convert_audio_format(input_file, output_format="wav"):
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_channels(1).set_frame_rate(16000)  # Convert to mono and set frame rate
    output_file = os.path.splitext(input_file)[0] + f".{output_format}"
    audio.export(output_file, format=output_format)
    return output_file

converted_file = convert_audio_format(data, "wav")
print(f"Converted file saved as: {converted_file}")

