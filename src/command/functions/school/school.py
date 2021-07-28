from src.interface.index import Interface
from src.functionalities.school.info_of_school import get_info_of_absences
from src.error.actions import error_ocured
from threading import Thread

class School:
  def __init__(self, window: Interface) -> None:
    self.window = window

  def absences(self, text):
    self.window.send_answer('Open the website.')
    Thread(target=self.execute).start()

  def execute(self):
    frequency = error_ocured(get_info_of_absences(), lambda e: self.window.send_answer(e.message))
    
    if frequency is not False:
      self.window.send_answer(f'Frequency: {frequency}%')