import os
import ffmpeg


def create_path():
    username = os.getlogin()
    path = f'C:\\Users\\{username}\\Desktop\\'
    return path


def merge(video_path, audio_path, output_path):
    input_video = ffmpeg.input(video_path)

    input_audio = ffmpeg.input(audio_path)

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(output_path).run(
        overwrite_output=True)

    os.remove(video_path)
    os.remove(audio_path)


def available_res(yt):
    resolutions = []

    for i in yt.streams:
        if i.resolution:
            r = int(str(i.resolution).replace('p', ''))
            if r not in resolutions:
                resolutions.append(r)

    resolutions.sort()
    res_string = ''

    for i in range(len(resolutions)):
        res_string += str(resolutions[i]) + 'p ; '

    return res_string
