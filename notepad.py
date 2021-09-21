from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
import pyttsx3

def newfile():
    global file
    root.title("untitled - Notepad")
    file = None
    textarea.delete(1.0, END)
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    file = asksaveasfilename(initialfile = 'Untitle.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()
def cut():
    textarea.event_generate("<<Cut>>")
def copy():
    textarea.event_generate("<<Copy>>")
def paste():
    textarea.event_generate("<<Paste>>")
def about():
    showinfo("Notepad", "NOTEPAD BY SANTOSH")
def quitapp():
    root.quit()
def hear():
    speak = textarea.get(1.0, END)
    return pyttsx3.speak(speak)
def red():
    global textarea
    textarea.destroy()
    textarea = Text(root,font="Lucida 12", fg="red")
    textarea.pack(expand=True, fill=BOTH)
    Scroll = Scrollbar(textarea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)

def blue():
    global textarea
    textarea.destroy()
    textarea = Text(root, font="Lucida 12 ", fg="blue")
    textarea.pack(expand=True, fill=BOTH)
    Scroll = Scrollbar(textarea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)

def green():
    global textarea
    textarea.destroy()
    textarea = Text(root, font="Lucida 12 ", fg="green")
    textarea.pack(expand=True, fill=BOTH)
    Scroll = Scrollbar(textarea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)

def yellow():
    global textarea
    textarea.destroy()
    textarea = Text(root, font="Lucida 12", fg="yellow")
    textarea.pack(expand=True, fill=BOTH)
    textarea.grid_info()
    Scroll = Scrollbar(textarea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)


root = Tk()
root.title("Untitle - NOTEPAD")
root.geometry("440x640")
file = None
textarea = Text(root)
textarea.pack(expand=True, fill=BOTH)


menubar= Menu(root)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New File", command=newfile)
filemenu.add_separator()
filemenu.add_command(label="open File", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="save File", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quitapp)
menubar.add_cascade(label="FILE", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="CUT", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="paste", command=paste)
menubar.add_cascade(label="EDIT", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="about notepad", command= about)
helpmenu.add_command(label="hear notepad", command= hear)
menubar.add_cascade(label="HELP", menu=helpmenu)

dizinemenu = Menu(menubar, tearoff=0)
dizinemenu.add_command(label="BLUE",command=blue)
dizinemenu.add_command(label="RED",command=red)
dizinemenu.add_command(label="YELLOW",command=yellow)
dizinemenu.add_command(label="GREEN",command=green)
menubar.add_cascade(label=" COLOR", menu=dizinemenu)

root.config(menu=menubar)

# # adding scroolbar
Scroll = Scrollbar(textarea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command= textarea.yview)
textarea.config(yscrollcommand=Scroll.set)




root.mainloop()