import yt_dlp
import os
import tkinter
import customtkinter


# Functions
def start_download_video():
    try:
        finish_label.configure(text="")
        download_link = link.get()
        downloader_options = {
            "format": "best",
            "outtmpl": os.path.join("Downloads", "%(title)s.%(ext)s"),
        }
        downloader = yt_dlp.YoutubeDL(downloader_options)
        downloader.download([download_link])
        finish_label.configure(text="Downloaded!", text_color="black")
    except:
        finish_label.configure(text="Download Error", text_color="red")


def start_download_audio():
    try:
        finish_label.configure(text="")
        download_link = link.get()
        downloader_options = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join("Downloads", "%(title)s.%(ext)s"),
        }
        downloader = yt_dlp.YoutubeDL(downloader_options)
        downloader.download([download_link])
        finish_label.configure(text="Downloaded!", text_color="black")
    except:
        finish_label.configure(text="Download Error", text_color="red")


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("520x240")
app.title("yt-dlp")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert an URL")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# Download Buttons Frame
buttons_frame = customtkinter.CTkFrame(app)
buttons_frame.pack()

# Download Button
download_video = customtkinter.CTkButton(
    buttons_frame, text="Video", command=start_download_video
)
download_video.pack(side="left", padx=10, pady=10)
download_audio = customtkinter.CTkButton(
    buttons_frame, text="Audio", command=start_download_audio
)
download_audio.pack(side="right", padx=10, pady=10)

##################################
# Run app
app.mainloop()
