from os import startfile as os_startfile, listdir as os_listdir, path as os_path

music_dir = "C:\\Users\\arksi\\Music\\"
songs = os_listdir(music_dir) 
for song in songs : 
    if song.endswith(".mp3") :
        path = os_path.join(music_dir, song)
        os_startfile(path)
        break