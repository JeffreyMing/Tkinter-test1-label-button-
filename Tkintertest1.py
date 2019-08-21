#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tkinter as tk


# In[11]:


def clickme():
    global count
    count += 1
    labeltext.set("你按我" + str(count) + "次了!")
    if(btntext.get() == "按我!"):
        btntext.set("回復原來文字!")
    else:
        btntext.set("按我!")


# In[23]:


win = tk.Tk()
win.geometry("320x80")
win.title("這是主視窗")
labeltext = tk.StringVar()
btntext = tk.StringVar()
count=0

labeltext.set("歡迎光臨tkinter!")
label1 = tk.Label(win, fg="red", font=("新細明體", 20),textvariable=labeltext)
label1.pack()

btntext.set("按我!")
butten1 = tk.Button(win, textvariable=btntext, command = clickme)
butten1.pack()

win.mainloop()

