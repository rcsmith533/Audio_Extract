import moviepy.editor as mp
import sys 
import tkinter as tk
from tkinter.filedialog import askopenfilename

def extractAudio():
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

def runGUI():
    window = tk.Tk()
    window.geometry('300x100')
    window.wm_iconbitmap('Record_Icon.ico')
    window.configure(bg='#CA2A07')
    window.title('Audio Extractor')
    btn = tk.Button(window,text='Open File', command=lambda:openFile())
    btn.pack(pady=20,padx=20)
    window.mainloop()

def openFile():
    filename = askopenfilename()
    my_clip = mp.VideoFileClip(filename)
    my_clip.audio.write_audiofile(f'{filename.split(".")[0]}.mp3',verbose=False)
    

if __name__ == '__main__':
    runGUI()