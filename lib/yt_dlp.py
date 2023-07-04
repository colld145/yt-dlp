import yt_dlp
import os


def start():
    exit = False

    while not exit:
        choice = input("1. Download Video\n2. Download Video with Format\n3. Download Audio\n\n0. Exit\n> ")
        if choice == "0":
            exit = True
            break

        elif choice == "1":
            link = input("Enter a URL to download video: ")
            download_video(link)

        elif choice == "2":
            link = input("Enter a URL to download video: ")
            get_formats(link)
            format = input("Enter a video format: ")
            download_video_with_format(link, format)

        elif choice == "3":
            link = input("Enter a URL to download audio: ")
            download_audio(link)


def download_video(link):
    downloader_options = {
        "format": "best",
        "outtmpl": os.path.join("Downloads", "%(title)s.%(ext)s"),
     }
    downloader = yt_dlp.YoutubeDL(downloader_options)
    downloader.download([link])


def download_video_with_format(link, format):
    downloader_options = {
        "format": format,
        "outtmpl": os.path.join("Downloads", "%(title)s.%(ext)s"),
    }
    downloader = yt_dlp.YoutubeDL(downloader_options)
    downloader.download([link])


def download_audio(link):
    downloader_options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join("Downloads", "%(title)s.%(ext)s"),
    }
    downloader = yt_dlp.YoutubeDL(downloader_options)
    downloader.download([link])


def get_formats(link):
    downloader_options =  { 'listformats' : True,}
    downloader = yt_dlp.YoutubeDL(downloader_options)
    info = downloader.extract_info(link, download = False)
    formats = info.get('formats', [])
    for format in formats:
        format_code = format['format_id']
        format_description = format.get('format_note', 'none')
        acodec = format.get('acodec')
        vcodec = format.get('vcodec')
        is_audio = acodec is not None
        if format_description == 'none':
            continue
        if not is_audio:
            continue
        print(f"Code: {format_code}, Format: {format_description}")
        print("-----------------------------")
