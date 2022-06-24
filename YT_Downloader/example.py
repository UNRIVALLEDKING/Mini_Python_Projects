from pytube import YouTube

yt = YouTube('https://youtu.be/Bpbgc6hcXE0')

print(yt.title)
print(yt.thumbnail_url)
print(yt.streams)
