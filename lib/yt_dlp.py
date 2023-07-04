import yt_dlp
import os


def start():
    exit = False

    while not exit:
        choice = input("1. Download Video\n2. Download Audio\n\n0. Exit\n> ")
        if choice == "0":
            exit = True
            break
        elif choice == "1":
            link = input("Enter a URL to download video: ")
            downloader_options = {
                "format": 'best',
                "outtmpl": os.path.join("Downloads", "%(title)s.%(ext)s"),
            }
            downloader = yt_dlp.YoutubeDL(downloader_options)
            downloader.download([link])
        elif choice == "2":
            link = input("Enter a URL to download audio: ")
            downloader_options = {
                "format": "bestaudio/best",
                "outtmpl": os.path.join("Downloads", "%(title)s.%(ext)s"),
            }
            downloader = yt_dlp.YoutubeDL(downloader_options)
            downloader.download([link])
