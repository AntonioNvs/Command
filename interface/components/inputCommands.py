import tkinter as tk

class InputCommands(tk.Entry):
  def __init__(self, main: tk.Tk) -> None:
    width = main.winfo_screenwidth()

    super().__init__(main,
                     width=width,
                     font=("Arial", 14), 
                     bd=0, 
                     fg="#F8F8F8", 
                     bg="#202020")

    self.pack(side=tk.BOTTOM)