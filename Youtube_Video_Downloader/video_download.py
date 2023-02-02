from pytube import YouTube 
import re 


link = input("Please, enter the video url :")

yt = YouTube(link) 

title = yt.title
title = re.sub("[^a-zA-Z0-9]+", ' ', title) 
print(title)

yt.streams.first().download(filename=title+".mp4") 

print("video doenloaded")
