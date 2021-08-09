import tkinter as tk
from tkinter import filedialog

import util.tkinterext as tkext

import util.timeutil as tu
import trimmer.trimmer as trimmer


def open_file():
    path_to_file = tk.filedialog.askopenfilename()
    if not path_to_file:
        return
    var_input_path.set(path_to_file)
    dry_var.set(1)


def trim():
    input_path = var_input_path.get()
    start_time = tu.time_only(ent_start_time.get())
    seek_from = tu.seek(ent_seek_from.get())
    seek_to = tu.seek(ent_seek_to.get())
    dry = dry_var.get()

    trimmer.trim(dry, input_path, start_time, seek_from, seek_to)


window = tk.Tk()
window.iconbitmap("trimmer.ico")
window.title("Offset Trimmer")
window.geometry("640x160")
window.rowconfigure([0, 1, 2, 3], pad=10)

btn_open = tk.Button(window, text="Choose a file...", command=open_file)
var_input_path = tk.StringVar()
lbl_input_path = tk.Label(window, textvariable=var_input_path)

btn_open.grid(row=0, column=0, sticky="nsw")
lbl_input_path.grid(row=0, column=1, sticky="nsw")

lbl_start_time = tk.Label(window, text="Scheduled At")
ent_start_time = tkext.EntryWithPlaceholder(window, placeholder="00:00")

lbl_start_time.grid(row=1, column=0, sticky="nsw")
ent_start_time.grid(row=1, column=1, sticky="nsw")

lbl_seek_from = tk.Label(window, text="Start Trimming From")
ent_seek_from = tkext.EntryWithPlaceholder(window, placeholder="00:00:00.000")

lbl_seek_from.grid(row=2, column=0, sticky="nsw")
ent_seek_from.grid(row=2, column=1, sticky="nsw")

lbl_seek_to = tk.Label(window, text="Stop Trimming At")
ent_seek_to = tkext.EntryWithPlaceholder(window, placeholder="00:00:00.000")

lbl_seek_to.grid(row=3, column=0, sticky="nsw")
ent_seek_to.grid(row=3, column=1, sticky="nsw")

frm_trim = tk.Frame(window)
frm_trim.grid(row=4, sticky="nsw")
btn_trim = tk.Button(frm_trim, text="Trim", command=trim)
dry_var = tk.IntVar(frm_trim)
dry_var.set(1)
chk_dry_run = tk.Checkbutton(
    frm_trim,
    text="Dry run?",
    variable=dry_var,
    onvalue=1,
    offvalue=0
)

btn_trim.pack(side=tk.LEFT)
chk_dry_run.pack(side=tk.LEFT)

window.mainloop()
