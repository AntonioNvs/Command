import tkinter as tk
from interface.components.labelCommand import LabelCommand
from interface.components.inputCommands import InputCommands
from command.controllCommands import ControllCommands

class Interface(tk.Tk):
  def __init__(self) -> None:
      # Iniciando a interface
      super().__init__()

      self.geometry("800x600")
      self.configure(background="#000000")
      self.resizable(width=False, height=False)
      
      self.inputCommands = InputCommands(self)
      self.inputCommands.bind("<Return>", self.send_command)

      self.labels = []
      self.limitLabels = 3
      
      self.controllCommands = ControllCommands(self)

      self.mainloop()

  def send_command(self, _event) -> None:
    text = self.inputCommands.get()

    self.inputCommands.delete(0, len(text))

    label = LabelCommand(self, text, type="command")
    
    # Para não sobrecarregar a tela de labels e atrapalhar a interface, é posto um limite.
    if len(self.labels) >= self.limitLabels:
      for lbl in self.labels:
        lbl.destroy()

      self.labels = []

    self.controllCommands.execute_a_command(text)

    self.labels.append(label)

  def send_answer(self, textAnswer: str) -> None:
    label = LabelCommand(self, textAnswer, type="answer")

    self.labels.append(label)
