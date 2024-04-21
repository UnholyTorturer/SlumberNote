"""
SlumberNote v1.0
April 20, 2024
"""

import os
from tkinter import *
from tkinter import filedialog

# get the current working directory
cur_dir = os.getcwd()

# open main config file
with open("conf","r") as f:
    lines = [lines.split() for lines in f]
    last = [last[-1] for last in lines]
    ui_path = last[0].strip()
    save_path = last[1].strip()

# open the UI config file
ui_txt = os.path.join(cur_dir,'img',ui_path,'ui.txt')
with open(ui_txt,"r") as g:
    ui = [ui.split() for ui in g]
    params = [params[-1] for params in ui]
    bg_color = params[0].strip()
    tx_color = params[1].strip()
    font = params[2].strip()
    font_size = params[3].strip()
    font_size = int(font_size)

# set our saved folder path
saves = os.path.join(cur_dir, save_path)
hlp = os.path.join(saves, "Help.txt")

# define our clickhandler so we can do things with stuff
def click_handler(event, flag):
    match flag:
        case "tab":
            xpos = root.winfo_x()
            if xpos == 1403:
                root.geometry("550x400+1895+340")
            else:
                root.geometry("550x400+1403+340")
        case "close":
            root.destroy()
        case "opts":
            with open(hlp, "r") as f:
                data = f.read()
                text_box.delete('1.0', END)
                text_box.insert(END, data)
            pass
        case "load":
            filename = filedialog.askopenfilename(initialdir=saves)
            if filename == "": pass
            else:
                with open(filename, "r") as f:
                    data = f.read()
                    text_box.delete('1.0', END)
                    text_box.insert(END, data)
        case "save":
            contents = text_box.get("1.0","end-1c")
            filename = filedialog.asksaveasfilename(initialdir=saves)
            if filename == "": pass
            else:
                with open(filename, "w") as f:
                    f.write(contents)
        case "delete":
            text_box.delete('1.0', END)

# move the moused-over object slightly just to be fancy
def mouseover(even, flag):
    match flag:
        case "onclose":
            close_label.place(x=473, y=33, width=35, height=35)
        case "offclose":
            close_label.place(x=470, y=35, width=35, height=35)
        case "onopts":
            opts_label.place(x=473, y=83, width=35, height=35)
        case "offopts":
            opts_label.place(x=470, y=85, width=35, height=35)
        case "onsave":
            save_label.place(x=473, y=133, width=35, height=35)
        case "offsave":
            save_label.place(x=470, y=135, width=35, height=35)
        case "onload":
            load_label.place(x=473, y=183, width=35, height=35)
        case "offload":
            load_label.place(x=470, y=180, width=35, height=35)
        case "ondelete":
            del_label.place(x=473, y=223, width=35, height=35)
        case "offdelete":
            del_label.place(x=470, y=225, width=35, height=35)

# init the root window and set up some parameters
root = Tk()
root.geometry("550x400+1895+340")
root["bg"] = "magenta"
root.attributes("-transparentcolor", "magenta")
root.attributes("-topmost", True)
root.overrideredirect(True)

# let's use some strings and variables to make some paths
border_loc = os.path.join(cur_dir, "img", ui_path, "frame.png")
tab_loc = os.path.join(cur_dir, "img", ui_path, "tab.png")
close_loc = os.path.join(cur_dir, "img", ui_path, "close.png")
opts_loc = os.path.join(cur_dir, "img", ui_path, "opt.png")
save_loc = os.path.join(cur_dir, "img", ui_path, "save.png")
load_loc = os.path.join(cur_dir, "img", ui_path, "load.png")
del_loc = os.path.join(cur_dir, "img", ui_path, "delete.png")
    
# load our ui images
bg_img = PhotoImage(file=border_loc)
tab_img = PhotoImage(file=tab_loc)
close_img = PhotoImage(file=close_loc)
opts_img = PhotoImage(file=opts_loc)
save_img = PhotoImage(file=save_loc)
load_img = PhotoImage(file=load_loc)
del_img = PhotoImage(file=del_loc)

# use a transparent label as a container for our background
bg_label = Label(root, bg="magenta", image=bg_img)
# and one for our tab
tab_label = Label(root, bg="magenta", image=tab_img)
# and some for our buttons
close_label = Label(root, bg="magenta", image=close_img)
opts_label = Label(root, bg="magenta", image=opts_img)
save_label = Label(root, bg="magenta", image=save_img)
load_label = Label(root, bg="magenta", image=load_img)
del_label = Label(root, bg="magenta", image=del_img)

# let's make our button-like labels clickable and pass a flag
# to our click handler, so that we know what was clicked
tab_label.bind("<Button-1>", lambda event: click_handler(event, flag="tab"))
close_label.bind("<Button-1>", lambda event: click_handler(event, flag="close"))
opts_label.bind("<Button-1>", lambda event: click_handler(event, flag="opts"))
save_label.bind("<Button-1>", lambda event: click_handler(event, flag="save"))
load_label.bind("<Button-1>", lambda event: click_handler(event, flag="load"))
del_label.bind("<Button-1>", lambda event: click_handler(event, flag="delete"))

# let's make the labels have a mouseover event, so that they
# look super fancy.
close_label.bind("<Enter>", lambda event: mouseover(event, flag="onclose"))
close_label.bind("<Leave>", lambda event: mouseover(event, flag="offclose"))
opts_label.bind("<Enter>", lambda event: mouseover(event, flag="onopts"))
opts_label.bind("<Leave>", lambda event: mouseover(event, flag="offopts"))
save_label.bind("<Enter>", lambda event: mouseover(event, flag="onsave"))
save_label.bind("<Leave>", lambda event: mouseover(event, flag="offsave"))
load_label.bind("<Enter>", lambda event: mouseover(event, flag="onload"))
load_label.bind("<Leave>", lambda event: mouseover(event, flag="offload"))
del_label.bind("<Enter>", lambda event: mouseover(event, flag="ondelete"))
del_label.bind("<Leave>", lambda event: mouseover(event, flag="offdelete"))

# set up our text box with no border, word wrap and option for font
# I need to convert the font_size variable to an integer
text_box = Text(root, bg=bg_color, fg=tx_color, bd=0, wrap=WORD, font=(font, font_size))
# make the caret match the text color
text_box.config(insertbackground=tx_color)
# give focus to the text box
text_box.focus_set()

# place our ui elements
bg_label.place(x=20, y=0)
tab_label.place(x=9, y=130, width=20, height=140)
close_label.place(x=470, y=35, width=35, height=35)
opts_label.place(x=470, y=85, width=35, height=35)
save_label.place(x=470, y=135, width=35, height=35)
load_label.place(x=470, y=180, width=35, height=35)
del_label.place(x=470, y=225, width=35, height=35)
text_box.place(x=40, y=30, width=420, height=345)

root.mainloop()