from src.database.querys.process_database import ProcessDatabase
import pandas as pd

class GetDataProcess(ProcessDatabase):
  def __init__(self) -> None:
    super().__init__()

    self.process_names = self._read_name_of_tasks()
    
  def _read_name_of_tasks(self) -> list:
    with open('src/functionalities/process/process_names.txt', 'r') as src:
      return src.read().split('\n')

  def get_info_of_a_task(self, task: str) -> tuple:
    name_exists = ""
    for name in self.process_names:
      if task.lower() in name.lower():
        name_exists = name
        break

    if name_exists != "":
      data = self.find_all_data_of_a_process(name_exists)

      columns = ["data_process_id", "memory", "cpu", "process_id", "date_created", "id_process", "name", "date_init", "date_end"]

      data = pd.DataFrame(data, columns=columns)
      
      data["memory"] = data["memory"].astype(float)
      data["cpu"] = data["cpu"].astype(float)


      mean_memory = round(data["memory"].mean(), 2)
      mean_cpu = round(data["cpu"].mean(), 2)
      max_memory = round(data["memory"].max(), 2)
      max_cpu = round(data["cpu"].max(), 2)

      return (("Média de memória (MB)", mean_memory),
              ("Média de CPU (%)", mean_cpu),
              ("Máximo de memória (MB)", max_memory),
              ("Máximo de CPU (%)", max_cpu))

    else: return ()