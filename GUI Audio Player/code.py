#import the libraries 
import os
import pygame
import tkinter as tk
from tkinter import filedialog

#class to play audio
class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")

        # create UI elements
        self.play_button = tk.Button(master, text="Play", command=self.play_music)
        self.play_button.pack()

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.import_button = tk.Button(master, text="Import Song", command=self.import_music)
        self.import_button.pack()

        # initialize pygame mixer
        pygame.mixer.init()

        # set up music variables
        self.music_file = None

    def import_music(self):
        filepath = filedialog.askopenfilename()
        self.music_file = filepath

    def play_music(self):
        if self.music_file:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
