# -*- coding: utf-8 -*-
import os
'''
import * only allowed at module level
Ain't important yet
'''
try:
    # for Python2
    #!/usr/bin/env python
    os.system('pip install youtube_dl')
    from tkinter import *
except ImportError:
    # for Python3
    #!/usr/bin/env python3
    os.system('pip3 install youtube_dl')
    from Tkinter import *

fenster = Tk()
fenster.title('UTube-Loader')
fenster.geometry('200x90')
fenster.configure(background='#FF0000')

eingabe = Entry(fenster)


def asVideo():
    os.system(f"youtube-dl {eingabe.get()}")
btn1 = Button(text="Download Mp4",command=asVideo)

def asAudio():
    os.system(f"youtube-dl -x --audio-format mp3 --audio-quality 0 {eingabe.get()}")
btn2 = Button(fenster, text="Download Mp3",command=asAudio)

# Add Elements to View
eingabe.pack()
btn1.pack()
btn2.pack()

if __name__ == "__main__":
    mainloop()
