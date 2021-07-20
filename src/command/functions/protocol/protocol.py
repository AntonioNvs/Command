from src.functionalities.volume import change_volume
from src.interface.index import Interface

class Protocol:
  def __init__(self, window: Interface) -> None:
    self.window = window

  def work(self, text):
    change_volume(6.0)
    self.window.send_answer("Volume has changed!")