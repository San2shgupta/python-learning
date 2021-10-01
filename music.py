from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import pygame

pygame.init()
pygame.mixer.init()

music_file = None
i= []
def add_music():
    global music_file
    music_file = askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3")])
    if music_file != "":
        songs_list.insert(END, os.path.basename(str(music_file)))

def delete_music():
    current_selection = songs_list.curselection()
    if current_selection:
        songs_list.delete(current_selection)
    else:
        songs_list.delete(1)

def callback(event):
    global music_file
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)

    if music_file != None:
        a = music_file.split(os.path.basename(music_file))[0]
        pygame.mixer.music.load(os.path.join(str(a), value))
        pygame.mixer.music.play()

def play_music():
    global music_file

    if music_file != None:
        a = music_file.split(os.path.basename(music_file))[0]
        pygame.mixer.music.load(os.path.join(str(a), os.path.basename(music_file) ))
        pygame.mixer.music.play()
def volup():
    default_volume = pygame.mixer.music.get_volume()
    up_volume = default_volume + 0.08
    pygame.mixer.music.set_volume(up_volume)

def voldown():
    default_volume = pygame.mixer.music.get_volume()
    down_volume = default_volume - 0.08
    pygame.mixer.music.set_volume(down_volume)

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()


if __name__ == '__main__':

    root = Tk()
    root.geometry("400x400")
    root.minsize(400, 400)
    root.maxsize(400, 400)
    root.title("Simple Music Player By Santosh")

    # Add ScrollBar to ListBox

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    # ListBox
    songs_list = Listbox(root, name='songs_list', yscrollcommand = scrollbar.set)
    songs_list.pack(fill=BOTH, pady=15, padx=15)
    songs_list.insert(END, "Songs List")
    songs_list.bind("<<ListboxSelect>>", callback)
    scrollbar.config(command=songs_list.yview)

    # Add & Delete Button
    frame = Frame(root)
    Button(frame, text="Add", pady=8, padx=20, font="lucida 10", command=add_music).pack(side=LEFT)
    Button(frame, text="Delete", pady=8, padx=16, font="lucida 10", command=delete_music).pack(side=LEFT)
    Button(frame, text="vol+", pady=8, padx=16, font="lucida 10", command=volup).pack(side=LEFT)
    Button(frame, text="vol-", pady=8, padx=16, font="lucida 10", command=voldown).pack(side=LEFT)
    frame.pack(padx=20,fill=Y)

    # Play & others Button
    frame1 = Frame(root)
    Button(frame1, text="▶play", font="lucida 10 bold", pady=8, padx=16, bg="grey", fg="white", command=play_music).pack(side=LEFT,pady=10)
    Button(frame1, text="Pause", font="lucida 10 bold", pady=8, padx=16, bg="red", fg="white", command=pause_music).pack(side=LEFT,pady=10)
    Button(frame1, text="Resume", font="lucida 10 bold", pady=8, padx=16, bg="grey", fg="white", command=resume_music).pack(side=LEFT,pady=10)
    frame1.pack(padx=20)

    Label(root, text="Created By Santosh Gupta", font="lucida 10", bg="grey", fg="white").pack(fill=X, pady=25)
    Label(root, text="Santosh Gupta", font="lucida 10", bg="black", fg="white").pack()

    root.mainloop()
