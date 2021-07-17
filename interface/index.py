import tkinter as tk
from interface.components.labelCommand import LabelCommand
from interface.components.inputCommands import InputCommands

class Interface(tk.Tk):
  def __init__(self) -> None:
      # Iniciando a interface
      super().__init__()

      self.geometry("800x600")
      self.configure(background="#000000")
      self.resizable(width=False, height=False)
      
      self.inputCommands = InputCommands(self)
      self.inputCommands.bind("<Return>", self.pressure_enter)

      self.labels = []
      self.limitLabels = 3

      self.mainloop()

  def pressure_enter(self, _event):
    text = self.inputCommands.get()

    self.inputCommands.delete(0, len(text))

    label = LabelCommand(self, text)
    
    
    if len(self.labels) >= self.limitLabels:
      for lbl in self.labels:
        lbl.destroy()

      self.labels = []

    self.labels.append(label)
