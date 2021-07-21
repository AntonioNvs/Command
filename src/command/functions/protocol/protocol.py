from src.functionalities.volume import change_volume
from src.functionalities.music import access_lofi
from src.functionalities.open import open_a_url, execute_a_program
from src.interface.index import Interface
from src.error.actions import error_ocured

class Protocol:
  def __init__(self, window: Interface) -> None:
    self.window = window

  def school(self, text):
    change_volume(4.0) # Aumentando o volume

    access_lofi() # Acessando lofi

    open_a_url('https://drive.google.com/drive/my-drive') # Acessando o drive

    open_a_url('https://descomplica.com.br/') # Acessando descomplica

    self.window.send_answer("Protocol 'school' activeted!")

  def programming(self, text):
    error_ocured(execute_a_program('vscode'), lambda e: self.window.send_answer(e.message))
    # error_ocured(execute_a_program('notion'), lambda e: self.window.send_answer(e.message))

    self.window.send_answer("Protocol 'programming' activeted!")

