from pytube import Playlist
import os 
import re 



#link = input("Please, Enter the Playlist link: ")
link = "https://www.youtube.com/watch?v=djDcVWbEYoE&list=PLXLYwvNGGPoUzjKiGvuXm8qeiOYMnFria"

yt_playlist = Playlist(link)
path = "D:\git\Youtube_Video_Downloader\playlist"
print(re.sub('[^A-Za-z0-9]+', '', yt_playlist.title))
i = 1
for video in yt_playlist.videos :
    # Download Normally
    #video.streams.get_highest_resolution().download(output_path=path)
    # Download videos in series
    title = " ".join([str(i), re.sub('[^A-Za-z0-9]+', ' ', video.title), ".mp4"])
    #video.streams.get_highest_resolution().download(output_path=None, filename=title)
    #title = video.title
    print("Video Downloaded: ", title)
    #title =re.sub('[^A-Za-z0-9]+', ' ', title)
    #os.rename(str(i)+".mp4", " ".join([str(i), title, ".mp4"]))
    i=i+1

print("\nAll videos are downloaded.")