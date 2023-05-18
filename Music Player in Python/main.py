
from tkinter import Tk, Listbox, PhotoImage, Frame, Button, Menu, filedialog, END
from pygame import mixer
import os 


root = Tk() 
root.title("Music Player") 
root.geometry("500x300") 

mixer.init() 
 
menubar = Menu(root) 
root.config(menu=menubar)

songs = [] 
current_song = '' 
paused = False 

def load_music(): 
    global current_song
    root.directory = filedialog.askdirectory() 
    
    for song in os.listdir(root.directory) : 
        name, ext = os.path.splitext(song) 
        if ext == '.mp3': 
            songs.append(song)  
        
    for song in songs : 
        songList.insert('end', song) 
    
    songList.selection_set(0) 
    current_song = songs[songList.curselection()[0]] 
    
def play_music() : 
    global current_song, paused 
    
    if not paused : 
        
        mixer.music.load(os.path.join(root.directory, current_song)) 
        mixer.music.play() 
    else : 
        mixer.music.unpause() 
        paused = False 

def pause_music() : 
    global paused 
    mixer.music.pause() 
    paused = True 

def next_music() : 
    global current_song, paused 
    
    try : 
        songList.selection_clear(0, END) 
        songList.selection_set(songs.index(current_song)+1) 
        current_song = songs[songList.curselection()[0]] 
        play_music() 
    except: 
        pass 
    
def prev_music() : 
    global current_song, paused 
    
    try : 
        songList.selection_clear(0, END) 
        songList.selection_set(songs.index(current_song)-1) 
        current_song = songs[songList.curselection()[0]] 
        play_music() 
    except : 
        pass 
    
    
    
    
menubar = Menu(root) 
root.config(menu=menubar)

organize_menu = Menu(menubar) 
organize_menu.add_command(label='Select_Folder', command=load_music)
menubar.add_cascade(label="Organise", menu=organize_menu)

songList = Listbox(root, bg='black', fg='white', width=100, height=15) 
songList.pack() 

#,height = 10, width = 10
play_btn_image = PhotoImage(file="./png/play.png").subsample(13, 13) 
pause_btn_image=PhotoImage(file="./png/pause.png").subsample(8, 8) 
next_btn_image = PhotoImage(file="./png/next.png").subsample(13, 13) 
prev_btn_image = PhotoImage(file="./png/prev.png").subsample(13, 13)

control_frame = Frame(root) 
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music) 
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music) 
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music) 
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0, command=prev_music) 

prev_btn.grid(row=0, column=0, padx=7, pady=10) 
play_btn.grid(row=0, column=1, padx=7, pady=10) 
pause_btn.grid(row=0, column=2, padx=7, pady=10) 
next_btn.grid(row=0, column=3, padx=7, pady=10) 

root.mainloop() 
