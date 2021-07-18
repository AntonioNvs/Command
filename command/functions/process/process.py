from error.classError import Error
from interface.index import Interface
from functionalities.process.get_data_process import GetDataProcess
from utils.manipulating_command import get_a_specific_value_in_a_command

class Process:
  def __init__(self, window: Interface) -> None:
    self.window = window
    self.get_info_data = GetDataProcess()

  def info(self, text: str) -> None:
    task = get_a_specific_value_in_a_command(text, 2)

    if isinstance(task, Error):
      self.window.send_answer(task.message)
      return

    info_task = self.get_info_data.get_info_of_a_task(task)

    if len(info_task) != 0:
      for line in info_task:
        self.window.send_answer(f"{line[0]}: {line[1]}")

    else:
      self.window.send_answer("This task does not exist in the list!")

