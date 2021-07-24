import tkinter as tk
from tkinter.constants import VERTICAL

class LabelCommand(tk.Label):
  def __init__(self, main: tk.Tk, text: str, type: str) -> None:
    fg, anchor = ("#F8F8F8", tk.W) if type == "command" else ("#9f1a1b", tk.E)

    super().__init__(main,
                     text=text,
                     bg="#000000",
                     font=("Arial", 12),
                     fg=fg,
                     justify=tk.LEFT,
                     anchor=anchor,
                     padx=16,
                     )

    self.pack(side=tk.TOP, fill=tk.BOTH)
    
