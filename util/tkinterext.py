import tkinter as tk


class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master, placeholder):
        super().__init__(master=master)

        self.placeholder = placeholder
        self.placeholder_color = "grey"
        self.original_fg_color = self["fg"]

        self.bind("<FocusIn>", self.__on_focus_in)
        self.bind("<FocusOut>", self.__on_focus_out)

        self.__put_placeholder()

    def __on_focus_in(self, event):
        if self["fg"] == self.placeholder_color:
            self.delete(0, tk.END)
            self["fg"] = self.original_fg_color

    def __on_focus_out(self, event):
        if not self.get():
            self.__put_placeholder()

    def __put_placeholder(self):
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color
