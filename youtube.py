import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube

window = tk.Tk()
window.title("YouTube Video Downloader:")

url_label = tk.Label(text="URL:")
url_entry = tk.Entry(width=50)
quality_label = tk.Label(text="quality (example, 720):")
quality_entry = tk.Entry(width=10)

url_label.grid(row=0, column=0)
url_entry.grid(row=0, column=1)
quality_label.grid(row=1, column=0)
quality_entry.grid(row=1, column=1)

def download_video():
    url = url_entry.get()
    quality = quality_entry.get()

    yt = YouTube(url)
    yt = yt.streams.filter(resolution=quality+"p").first()
    
    yt.download()
    
    messagebox.showinfo("Important!", "Video Downloaded Successfully!")

download_button = tk.Button(text="Download", command=download_video)
download_button.grid(row=2, column=1)

window.mainloop()