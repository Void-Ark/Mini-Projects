import pyperclip 
import pyshorteners 
from tkinter import * 
# from tkinter import Tk, StringVar

root = Tk()
root.geometry("400x200") 
root.title("URL Sortener") 
root.configure(bg="#262929") 
url = StringVar()
url_address = StringVar()

def urlShortener() : 
    urladdress = url.get() 
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress) 
    url_address.set(url_short) 
    
def copyurl() : 
    url_short = url_address.get() 
    pyperclip.copy(url_short) 
    
background = "#6f8171"
Label(root, text="MY URL SHORTENER", font="poppins", background=background).pack(pady=10) 
Entry(root, textvariable=url, background=background).pack(pady=5) 
Button(root, text="Gentrate short URL", command=urlShortener, background=background).pack(pady=7) 
Entry(root, textvariable=url_address, background=background).pack(pady=5) 
Button(root, text="Copy URL", command=copyurl, background=background).pack(pady=5) 

root.mainloop()