from pyperclip import copy as pyperclip_copy

from pyshorteners import Shortener as pyshorteners_Shortener

from tkinter import Tk as tkinter_Tk
from tkinter import StringVar as tkinter_StringVar
from tkinter import Label as tkinter_Label
from tkinter import Entry as tkinter_Entry 
from tkinter import Button as tkinter_Button

root = tkinter_Tk()
root.geometry("400x200") 
root.title("URL Sortener") 
root.configure(bg="#262929") 
url = tkinter_StringVar()
url_address = tkinter_StringVar()

def urlShortener() : 
    urladdress = url.get() 
    url_short = pyshorteners_Shortener().tinyurl.short(urladdress) 
    url_address.set(url_short) 
    
def copyurl() : 
    url_short = url_address.get() 
    pyperclip_copy(url_short) 
    
background = "#6f8171"
tkinter_Label(root, text="MY URL SHORTENER", font="poppins", background=background).pack(pady=10) 
tkinter_Entry(root, textvariable=url, background=background).pack(pady=5) 
tkinter_Button(root, text="Generate short URL", command=urlShortener, background=background).pack(pady=7) 
tkinter_Entry(root, textvariable=url_address, background=background).pack(pady=5) 
tkinter_Button(root, text="Copy URL", command=copyurl, background=background).pack(pady=5) 

root.mainloop()