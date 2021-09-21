from tkinter import *


def age():

    if uservar.get() < 100:
        b = 2021
        a = (b - uservar.get())
        outputvar.set(a)


    elif uservar.get() > 1921:
        a = 2021 - uservar.get()
        outputvar.set(a)

    elif uservar.get() < 1921:
        outputvar.set("You are older person")
    else:
        outputvar.set(int("try again"))
def totalvalue():

    if uservar.get() > 1900:
        a = finalvar.get() - uservar.get()
        totalvar.set(a)
    else:
        a = 2021 - uservar.get()
        b = finalvar.get() - a
        totalvar.set(b)
def clear():
    uservar.set("")
    finalvar.set("")
    outputvar.set("")
    totalvar.set("")

if __name__ == '__main__':

    root = Tk()

    root.geometry("420x320")
    root.title("AGE CALCULATOR")
    fram = Frame(root, relief=SUNKEN,bg="black")
    user = Label(fram,text="Enter age or year of birth")
    output = Label(fram,text="your age/year of birth")
    final = Label(fram,text="Enter year you want to\n know how much you old in that")
    total = Label(fram,text="Total")

    user.grid()
    output.grid(row=1)
    final.grid(row=2)
    total.grid(row=3)

    uservar = IntVar()
    outputvar = IntVar()
    finalvar = IntVar()
    totalvar = IntVar()

    userentry = Entry(fram, textvariable=uservar)
    outputentry = Entry(fram,textvariable=outputvar)
    final = Entry(fram, textvariable=finalvar)
    totalentry = Entry(fram, textvariable=totalvar)

    userentry.grid(row=0, column=1, padx=8,pady=8)
    outputentry.grid(row=1, column=1,padx=8,pady=8)
    final.grid(row=2,column=  1,padx=8,pady=8)
    totalentry.grid(row=3,column=1,padx=8,pady=8)
    fram.grid()
    Button(text="submit", command=age).grid()
    Button(text="final",command=totalvalue).grid()
    Button(text="clear",command=clear).grid()


    root.mainloop()