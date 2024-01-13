import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
import random

music_player = tkr.Tk()
music_player.title("PythonJams")
music_player.geometry("500x350")  # Increased width to accommodate new buttons
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Arial 12 bold", bg='black', selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def shuffle():
    shuffled_list = list(song_list)
    random.shuffle(shuffled_list)
    play_list.delete(0, tkr.END)
    for item in shuffled_list:
        play_list.insert(tkr.END, item)


def loop():
    current_song = play_list.get(tkr.ACTIVE)
    play_list.delete(0, tkr.END)
    for _ in range(3):  # Loop the current song three times
        play_list.insert(tkr.END, current_song)


def next_song():
    current_index = play_list.curselection()
    if current_index:
        next_index = (current_index[0] + 1) % play_list.size()
        play_list.selection_clear(0, tkr.END)
        play_list.selection_set(next_index)
        play()
    else:
        play_first_song()


def prev_song():
    current_index = play_list.curselection()
    if current_index:
        prev_index = (current_index[0] - 1) % play_list.size()
        play_list.selection_clear(0, tkr.END)
        play_list.selection_set(prev_index)
        play()
    else:
        play_last_song()


def play_first_song():
    play_list.selection_clear(0, tkr.END)
    play_list.selection_set(0)
    play()


def play_last_song():
    play_list.selection_clear(0, tkr.END)
    play_list.selection_set(play_list.size() - 1)
    play()


Button1 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="PLAY", command=play, bg="red",
                     fg="black")
Button2 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="STOP", command=stop, bg="black",
                     fg="black")
Button3 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="PAUSE", command=pause, bg="gold",
                     fg="black")
Button4 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="UNPAUSE", command=unpause,
                     bg="silver", fg="black")
Button5 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="SHUFFLE", command=shuffle, bg="green",
                     fg="black")
Button6 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="LOOP", command=loop, bg="cyan",
                     fg="black")
Button7 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="PREV", command=prev_song, bg="blue",
                     fg="black")
Button8 = tkr.Button(music_player, width=5, height=3, font="Arial 12 bold", text="NEXT", command=next_song, bg="orange",
                     fg="black")

var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Arial 12 bold", textvariable=var)

song_title.pack()
Button1.pack(side="left")
Button2.pack(side="left")
Button3.pack(side="left")
Button4.pack(side="left")
Button5.pack(side="left")
Button6.pack(side="left")
Button7.pack(side="left")
Button8.pack(side="left")
play_list.pack(fill="both", expand="yes")

music_player.mainloop()
