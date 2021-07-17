import tkinter as tk

class LabelCommand(tk.Label):
  def __init__(self, main: tk.Frame, text):
    super().__init__(main,
                     text=text,
                     bg="#000000",
                     font=("Arial", 12),
                     fg="#F8F8F8",
                     justify=tk.LEFT,
                     anchor=tk.W,
                     padx=16)

    self.pack(side=tk.TOP, fill=tk.BOTH)
    
