from src.functionalities.process.analysis_process import AnalysisProcess
from src.database.querys.process_database import ProcessDatabase
from threading import Thread
import time

class ControllProcess(AnalysisProcess):
  def __init__(self) -> None:
    super().__init__(ProcessDatabase())

    self.name_state = "get_process"
    self.is_thread = True
    self.state = False
    self.th = Thread(target=self.loop_process)

    time.clock()

  # Thread do processo de looping
  def loop_process(self):
    while self.state:
      self.fill_info_about_process()
      time.sleep(1)

  def execute(self):
    # Instanceando a thread do loop de análise de processos
    self.th.start()

  def finish(self):
    self.end_process()

