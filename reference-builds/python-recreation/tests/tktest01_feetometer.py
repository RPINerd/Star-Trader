#!/usr/bin/env python3
# coding: utf-8
#
# $Id: tktest01_feetometer.py 1303 $
# SPDX-License-Identifier: BSD-2-Clause

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky='NEWS')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky='EW')

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky='EW')
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky='W')

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky='W')
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky='E')
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky='W')

image = PhotoImage(file='test.gif')
label = ttk.Label(mainframe, text='Full name:')
label['image'] = image

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
