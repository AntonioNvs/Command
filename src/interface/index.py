import tkinter as tk

from src.interface.components.labelCommand import LabelCommand
from src.interface.components.inputCommands import InputCommands
from src.command.controllCommands import ControllCommands
from src.utils.manipulating_command import get_a_specific_value_in_a_command

class Interface(tk.Tk):  
  def __init__(self, parallelClass) -> None:
      # Iniciando a interface
      super().__init__()

      self.geometry("800x600")
      self.configure(background="#000000")
      self.resizable(width=False, height=False)
      
      self.inputCommands = InputCommands(self)
      self.inputCommands.bind("<Return>", self.send_command)

      self.protocol("WM_DELETE_WINDOW", self.on_close)


      self.labels = []
      self.limitLabels = 3
      
      self.controllCommands = ControllCommands(self)

      self.parallelClass = parallelClass
      self.keyForParallel = parallelClass.key

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

    # Chama um tipo de funcionalidade a partir da chave especificada
    if get_a_specific_value_in_a_command(text, 0) == self.keyForParallel:
      self.parallelClass.command_for_activity(text, self)
    else:
      self.controllCommands.execute_a_command(text)

    self.labels.append(label)

  def send_answer(self, textAnswer: str) -> None:
    label = LabelCommand(self, textAnswer, type="answer")

    self.labels.append(label)


  def on_close(self):
    self.parallelClass.finish_the_activities(self)

    self.destroy()