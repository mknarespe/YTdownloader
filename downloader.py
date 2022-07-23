import string

from pytube import YouTube
from defs import merge, available_res, create_path

downloaded = False
file_type = "webm"
# Desktop path
path = create_path()

print('Hey! This program helps you to download youtube audio/video by the link\n')
link = input('First, enter the link: ')
video = YouTube(link)

# Title of video
title = video.title
print('Title: ', title)
# Number of views of video
print('Number of views: ', video.views)
# Length of the video
print('Length of video: ', video.length, 'seconds')
# Choose what to do
choice = int(input('Enter 1 to download only Audio or enter 2 for both audio and video \n: '))


Streams = video.streams

while not downloaded:
    if choice == 1:
        aud = Streams.filter(only_audio=True, file_extension='webm').first().download(path)
        downloaded = True

    elif choice == 2:

        # Available resolutions
        print('Available resolutions: ' + available_res(video))
        resol = str(input("Video with 720p resolution or less will download much faster\n"
                          "you still can download video in FullHD or higher, but it`ll take some time\n"
                          "Choose the resolution, for instance - '240' or '1080'\n"))

        if int(resol) < 1080:
            video.streams.get_by_resolution(resol+'p').download(path)
        else:
            vid = Streams.filter(res=resol+'p', file_extension=file_type).first().download(path, filename='video.webm')
            aud = Streams.filter(only_audio=True).first().download(path, filename='audio.webm')

            new_title = title.translate(str.maketrans('', '', string.punctuation))
            output_path = path + new_title + '.webm'

            print(output_path)
            merge(vid.title(), aud.title(), output_path)

        downloaded = True
    else:
        print('Invalid Selection')
