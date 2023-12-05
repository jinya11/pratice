# 예시 실행안됨.

import os
from pytube import YouTube

url = input("추가할 노래의 URL을 입력해 주세요")
yt = YouTube(url)
DownLoad=r"C:\Users\SAMSUNG\OneDrive\바탕 화면\schoolproject\music\musicdir"
filePath = yt.streams.filter(only_audio=True).first().download(DownLoad)
mp3FilePath = filePath.replace('mp4', 'mp3')
os.rename(filePath, mp3FilePath)

song_title = yt.title

txt_file_path = r"C:\Users\SAMSUNG\OneDrive\바탕 화면\schoolproject\music\musicinfo.txt"
with open(txt_file_path, 'a') as txt_file:
    txt_file.write(f"Title: {song_title}\nURL: {current_song_url}\n\n")

# Check if the file exists, and create it if not
if not os.path.exists(mp3_file_path):
    with open(mp3_file_path, 'w'):  # Create an empty file
        pass

dir = r"/music/musicdir"

