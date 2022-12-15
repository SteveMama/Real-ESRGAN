import os
import shutil

upload_folder = 'upload'
result_folder = 'results'
video_folder = 'videos'
video_result_folder = 'results_videos'
video_mp4_result_folder = 'results_mp4_videos'

if os.path.isdir(upload_folder):
    print(upload_folder + " exists")
else:
    os.mkdir(upload_folder)

if os.path.isdir(video_folder):
    print(video_folder + " exists")
else:
    os.mkdir(video_folder)

if os.path.isdir(video_result_folder):
    print(video_result_folder + " exists")
else:
    os.mkdir(video_result_folder)

if os.path.isdir(video_mp4_result_folder):
    print(video_mp4_result_folder + " exists")
else:
    os.mkdir(video_mp4_result_folder)

if os.path.isdir(result_folder):
    print(result_folder + " exists")

else:
    os.mkdir(result_folder)


