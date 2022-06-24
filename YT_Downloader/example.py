from pytube import YouTube

# get details of video and stream files here

yt = YouTube('https://youtu.be/Bpbgc6hcXE0')

print(yt.title)
print(yt.thumbnail_url)
print(yt.streams)
