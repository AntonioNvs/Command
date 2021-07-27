from src.interface.index import Interface
from src.functionalities.school.info_of_school import get_info_of_absences
from src.error.actions import error_ocured

class School:
  def __init__(self, window: Interface) -> None:
    self.window = window

  def absences(self, text):
    frequency = error_ocured(get_info_of_absences(), lambda e: self.window.send_answer(e.message))
    
    if frequency is not False:
      self.window.send_answer(f'Frequency: {frequency}')

