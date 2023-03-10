# Importing Required Modules & libraries
from tkinter import *
import pygame
import os

class MusicPlayer:

  def __init__(self,root):
    self.root = root
    self.root.title("JMAR Music Box")
    self.root.geometry("1000x500+500+500")
    pygame.init()
    pygame.mixer.init()
    self.track = StringVar()
    self.status = StringVar()

    trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=1000,height=1000)
    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="black",fg="blue").grid(row=0,column=0,padx=20,pady=5)
    trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="black",fg="blue").grid(row=0,column=1,padx=20,pady=5)

    buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
    buttonframe.place(x=0,y=100,width=1000,height=1000)
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="white",bg="blue").grid(row=0,column=0,padx=20,pady=5)
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="white",bg="blue").grid(row=0,column=1,padx=20,pady=5)
    playbtn = Button(buttonframe,text="RESUME",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="white",bg="blue").grid(row=0,column=2,padx=20,pady=5)
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="white",bg="blue").grid(row=0,column=3,padx=20,pady=5)

    songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
    songsframe.place(x=600,y=0,width=1000,height=1000)
    scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="#40e0d0",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)
    os.chdir("C:/Users/Rutvik Shah/Desktop/python/music_app/music_database")
    songtracks = os.listdir()
    for track in songtracks:
      self.playlist.insert(END,track)

  def playsong(self):
    self.track.set(self.playlist.get(ACTIVE))
    self.status.set("-Playing")
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    pygame.mixer.music.play()

  def stopsong(self):
    self.status.set("-Stopped")
    pygame.mixer.music.stop()

  def pausesong(self):
    self.status.set("-Paused")
    pygame.mixer.music.pause()

  def unpausesong(self):
    self.status.set("-Playing")
    pygame.mixer.music.unpause()
  def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

root = Tk()
MusicPlayer(root)
root.mainloop()
