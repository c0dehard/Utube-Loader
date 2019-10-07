# -*- coding: utf-8 -*-
'''
Es wird youtube-dl
benötigt um dieses Fontend nutzen zu können!
Es lädt die Datei in den pwd/chdir in welchem das Skript gestartet wurde.
'''
import os
try:
    # für Python2
    #!/usr/bin/env python
    from tkinter import *
except ImportError:
    # für Python3
    #!/usr/bin/env python3
    from Tkinter import *

fenster = Tk()
fenster.title('UTube-Loader')
fenster.geometry('200x90')
fenster.configure(background='#FF0000')

eingabe = Entry(fenster)
eingabe.pack()



def alsVideo():
    os.system("youtube-dl " +eingabe.get())
knopf1 = Button(text="Download Mp4",command=alsVideo)
knopf1.pack()


def alsAudio():
    os.system("youtube-dl -x --audio-format mp3 --audio-quality 0 " +eingabe.get())
knopf2 = Button(fenster, text="Download Mp3",command=alsAudio)
knopf2.pack()




mainloop()
