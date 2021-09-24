import tkinter
from tkinter import *
from tkinter import ttk

from history import History


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.text = ""
        self.history = History()

    def start(self):
        self.pack()
        self.setup()
        self.mainloop()

    def setup(self):
        self.render_screen()
        self.set_title("Editor de texto")
        self.set_dimensions("1200x710")

    def set_title(self, title=''):
        self.master.title(title)

    def set_dimensions(self, dimension):
        self.master.geometry(dimension)

    def on_entry_click(self, event):
        text = event.widget.get("1.0", "end-1c")

        self.history.add(text)
        print(self.history.get_text())

    def set_input_value(self, value=""):
        print(value)
        self.text_area.delete(1.0, "end")
        self.text_area.insert(1.0, value)
    
    def execute_undo(self):
        self.history.undo()

        self.set_input_value(self.history.get_text())

    def execute_redo(self):
        self.history.redo()

        self.set_input_value(self.history.get_text())

    def render_screen(self):
        frame = Frame(self.master)
        frame.pack(pady=5)

        undo_button = ttk.Button(frame, text="Desfazer", command=self.execute_undo).pack()
        redo_button = ttk.Button(frame, text="Refazer", command=self.execute_redo).pack()

        text_scroll = Scrollbar(frame)
        text_scroll.pack(side=RIGHT, fill=Y)

        hor_scroll = Scrollbar(frame, orient='horizontal')
        hor_scroll.pack(side=BOTTOM, fill=X)

        self.text_area = Text(frame, width=97, height=25, font=("Helvetica", 16), selectbackground="gray",
                         selectforeground="black", yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
        self.text_area.bind("<KeyRelease>", self.on_entry_click)
        self.text_area.pack()

        text_scroll.config(command=self.text_area.yview)
        hor_scroll.config(command=self.text_area.xview)

app = Application(master=tkinter.Tk())
app.start()
