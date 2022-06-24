from pytube import YouTube
import ffmpeg

SAVE_PATH = "C:/Users/adity/Downloads/pytube"

link = "https://youtu.be/jH1RNk8954Q"
yt = YouTube(link)
title = yt.title

try:
    # print(yt.streams.filter(file_extension='webm', res='1080p'))
    # progressive_video = yt.streams.get_highest_resolution
    video_file = yt.streams.get_by_itag(248)
    audio_file = yt.streams.get_by_itag(251)
except:
    print("Connection Error")

try:
    video_file.download(SAVE_PATH, filename="input_video.webm")
    audio_file.download(SAVE_PATH, filename="input_audio.webm")
except:
    print("Some Error!")

# ffmpeg part
print("merging video")


input_video = ffmpeg.input('C:/Users/adity/Downloads/pytube/input_video.webm')

input_audio = ffmpeg.input('C:/Users/adity/Downloads/pytube/input_audio.webm')

ffmpeg.concat(input_video, input_audio, v=1,
              a=1).output('C:/Users/adity/Downloads/pytube/' + title + ".mkv").run()


print("Task Completed!")
