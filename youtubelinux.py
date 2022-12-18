from pytube import YouTube

url = input("URL: ")
quickly = input("Write video quality. Example 720p:  ")


yt = YouTube(url)

video = yt.streams.filter(res=quickly).first()


video.download()
print("Download Succesful!")
