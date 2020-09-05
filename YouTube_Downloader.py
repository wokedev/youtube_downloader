from pytube import YouTube

video_link = input("Enter Video Link: ")

try:
    yt = YouTube(video_link)
    stream = yt.streams.first()
    stream.download()

except Exception as e:
    print("Download Failed!")
    print(e)
