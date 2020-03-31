#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
	os.system('pip install youtube_dl')
	from tkinter import * # Python 2
except ImportError : from Tkinter import * # Python 3

window = Tk() ; window.title('UTube-Loader')
window.geometry('200x90') ; window.configure(background='#FF0000')

def as_video() : os.system(f"youtube-dl {usr_input.get()}")
def as_audio() : os.system(f"youtube-dl -x --audio-format mp3 --audio-quality 0 {usr_input.get()}")

# Create Elements
usr_input = Entry(window)
btn1 = Button(text="Download Mp4",command=as_video)
btn2 = Button(window, text="Download Mp3",command=as_audio)

# Add Elements to View
for item in [usr_input, btn1, btn2]:
	item.pack()

if __name__ == "__main__":
	mainloop()
