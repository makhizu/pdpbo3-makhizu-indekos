# from tkinter import *

# root = Tk()
# btn_column = Button(root, text="This is column 2")
# btn_column.grid(column=2)

# btn_columnspan = Button(root, text="With columnspan of 4")
# btn_columnspan.grid(columnspan=4)

# btn_ipadx = Button(root, text="padding horizontally ipadx of 3")
# btn_ipadx.grid(ipadx=3)

# btn_ipady = Button(root, text="padding vertically ipady of 3")
# btn_ipady.grid(ipady=3)

# btn_padx = Button(root, text="padx 2")
# btn_padx.grid(padx=4)

# btn_pady = Button(root, text="pady of 2")
# btn_pady.grid(padx=4)

# btn_row = Button(root, text="This is row 2")
# btn_row.grid(row=2)

# btn_rowspan = Button(root, text="With Rowspan of 3")
# btn_rowspan.grid(rowspan=3)

# btn_sticky = Button(root, text="Sticking to north-east")
# btn_sticky.grid(sticky=NE)

# root.mainloop()

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('100x100')
 
l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()
 
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not anything')
    else:
        l.config(text='I love both')
 
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
 
window.mainloop()