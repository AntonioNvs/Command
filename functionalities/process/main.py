from functionalities.process.analysis_process import AnalysisProcess
from database.querys.process_database import ProcessDatabase
from threading import Thread
import time

class ControllProcess(AnalysisProcess):
  def __init__(self) -> None:
    super().__init__(ProcessDatabase())

    time.clock()

    self.init_program()

  # Thread do processo de looping
  def loop_process(self):
    while not self.is_exit:
      self.fill_info_about_process()

  def init_program(self):
    self.is_exit = False

    # Instanceando a thread do loop de análise de processos
    self._th_process = Thread(target=self.loop_process)
    self._th_process.start()

  def close_program(self):
    self.is_exit = True
    self.end_process()

