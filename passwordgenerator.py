# -*- coding: utf-8 -*-
from tkinter import *
import random

root=Tk()
root.title("password generator")
root.geometry("400x400")

label= Label(root)

array_3d= [[['1','2','3','4','5','6'], ["heads", "tails"], ["A","B","C","D","E","F","G"]]]
print(array_3d[0][2][5])

def password():
    random_no1= random.randint(0,5)
    random_no2= random.randint(0,1)
    random_no3= random.randint(0,6)
    
    letter1= str(array_3d[0][0][random_no1])
    letter2= (array_3d[0][1])[random_no2]
    letter3= (array_3d[0][2][random_no3])
    label["text"]= letter1 + "" + letter2 + "" + letter3
    
btn = Button(root, text= "generate password", command = password)
btn.place(relx=0.5, rely=0.5, anchor= CENTER)
label.place(relx=0.5, rely=0.6, anchor= CENTER)

root.mainloop()