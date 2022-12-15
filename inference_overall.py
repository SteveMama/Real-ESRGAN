import cv2
import os
import numpy as np
import glob
from os.path import isfile, join
import subprocess


# assign directory
directory = 'Real-ESRGAN/videos/'  # PATH_WITH_INPUT_VIDEOS
zee = 0

# deletes frames from previous video
for f in os.listdir(upload_folder):
    os.remove(os.path.join(upload_folder, f))

# deletes upscaled frames from previous video
for f in os.listdir(result_folder):
    os.remove(os.path.join(result_folder, f))

# clearing previous .avi files
for f in os.listdir(video_result_folder):
    os.remove(os.path.join(video_result_folder, f))

# clearing .mp4 result files
for f in os.listdir(video_mp4_result_folder):
    os.remove(os.path.join(video_mp4_result_folder, f))


def convert_frames_to_video(pathIn, pathOut, fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    # for sorting the file names properly
    files.sort(key=lambda x: int(x[5:-4]))
    size2 = (0, 0)

    for i in range(len(files)):
        filename = pathIn + files[i]
        # reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        size2 = size
        print(filename)
        # inserting the frames into an image array
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size2)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()


for filename in os.listdir(directory):

    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):

        print("PROCESSING :" + str(f) + "\n")
        # Read the video from specified path

        # video to frames
        cam = cv2.VideoCapture(str(f))

        try:

            # PATH TO STORE VIDEO FRAMES
            if not os.path.exists('Real-ESRGAN/upload/'):
                os.makedirs('/content/Real-ESRGAN/upload/')

        # if not created then raise error
        except OSError:
            print('Error: Creating directory of data')

        # frame
        currentframe = 0

        # clear all folders

        # deletes upscaled frames from previous video
        # for f in os.listdir(result_folder):
        #  os.remove(os.path.join(result_folder, f))

        while (True):

            # reading from frame
            ret, frame = cam.read()

            if ret:
                # if video is still left continue creating images
                name = 'Real-ESRGAN/upload/frame' + str(currentframe) + '.jpg'

                # writing the extracted images
                cv2.imwrite(name, frame)

                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
            else:
                # deletes all the videos you uploaded for upscaling
                # for f in os.listdir(video_folder):
                #  os.remove(os.path.join(video_folder, f))

                break

        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()

        # apply super-resolution on all frames of a video
        # scale factor is by 3.5x

        !python inference_realesrgan.py - n RealESRGAN_x4plus - i upload --outscale 2 --face_enhance --tile 64

        # after upscaling just delete the source frames
        for f in os.listdir(upload_folder):
            os.remove(os.path.join(upload_folder, f))

            # rename all frames in "results" to remove the 'out' substring from the processing results
        paths = (os.path.join(root, filename)
                 for root, _, filenames in os.walk('Real-ESRGAN/results/')
                 for filename in filenames)
        for path in paths:
            newname = path.replace('_out', '')
            if newname != path:
                os.rename(path, newname)

                # convert super res frames to .avi
        pathIn = 'Real-ESRGAN/results/'

        zee = zee + 1
        fName = "video" + str(zee)
        filenameVid = f"{fName}.avi"

        pathOut = "Real-ESRGAN/results_videos/" + filenameVid

        fps = 50  # change this to FPS of your source video

        convert_frames_to_video(pathIn, pathOut, fps)

        # after processing frames converted to .avi video , delete upscaled frames from previous video
        for f in os.listdir(result_folder):
            os.remove(os.path.join(result_folder, f))

        # convert .avi to .mp4
        src = 'Real-ESRGAN/results_videos/'
        dst = 'results_mp4_videos/'

        for root, dirs, filenames in os.walk(src, topdown=False):
            # print(filenames)
            for filename in filenames:
                print('[INFO] 1', filename)
                try:
                    _format = ''
                    if ".flv" in filename.lower():
                        _format = ".flv"
                    if ".mp4" in filename.lower():
                        _format = ".mp4"
                    if ".avi" in filename.lower():
                        _format = ".avi"
                    if ".mov" in filename.lower():
                        _format = ".mov"

                    inputfile = os.path.join(root, filename)
                    print('[INFO] 1', inputfile)
                    outputfile = os.path.join(dst, filename.lower().replace(_format, ".mp4"))
                    subprocess.call(['ffmpeg', '-i', inputfile, outputfile])
                except:
                    print("An exception occurred")

        clear_output(wait=True)

        # clearing previous .avi files
        for f in os.listdir(video_result_folder):
            os.remove(os.path.join(video_result_folder, f))

        # deletes frames from previous video
        # for f in os.listdir(upload_folder):
        #  os.remove(os.path.join(upload_folder, f))

        # if it is out of memory, try to use the `--tile` option
# We upsample the image with the scale factor X3.5

# Arguments
# -n, --model_name: Model names
# -i, --input: input folder or image
# --outscale: Output scale, can be arbitrary scale factore.