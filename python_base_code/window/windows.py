#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import tkinter

def my_window(w, h):
 ws = root.winfo_screenwidth()
 hs = root.winfo_screenheight()
 x = (ws/2) - (w/2)
 y = (hs/2) - (h/2)
 root.geometry("%dx%d+%d+%d" % (w, h, x, y))

root = tkinter.Tk(className='python windows app')
my_window(100, 100)
root.mainloop()