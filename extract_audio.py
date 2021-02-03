import moviepy.editor as mp
import sys 

if len(sys.argv) == 2:
    try:
        my_clip = mp.VideoFileClip(sys.argv[1])
        my_clip.audio.write_audiofile(f'{sys.argv[1].split(".")[0]}.mp3',verbose=False)
    except:
        print('Error!')
elif len(sys.argv) > 2:
    print('Too many arguments')
else:
    print('Please add the file path to the video')