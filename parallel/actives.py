"""
  As atividades deverão possuir as determinadas propriedades:

  Funções

  __init__: prepara o programa para execução

  execute: começa a realizar o programa
  finish: termine de executar o programa

  state: retorna o estado 

  Variáveis
  name_state: nome da variável do estado
  state: tem que estar em execução ou não (somente thread)
  th: thread
  is_thread: o programa precisa ser executado em thread

"""

from time import sleep
from src.functionalities.process.main import ControllProcess
from src.utils.txt import get_variable, set_variable

class ParallelActivities:
  def __init__(self) -> None:
    self.classActivities = {
      'process': ControllProcess()
    }

    self.program_is_running = True
    self.interval = 2

    # Verificação se todas as classes possuem as funções e os atributos
    for _class in self.classActivities.values():
      getattr(_class, 'execute')
      getattr(_class, 'finish')
      getattr(_class, 'name_state')
      getattr(_class, 'is_thread')

      if _class.is_thread:
        getattr(_class, 'state')
        getattr(_class, 'th')


  # Executar as atividades que não são em threads
  def loop_execute(self):
    while self.program_is_running:
      for _class in self.classActivities.values():
        if _class.is_thread is False and get_variable(_class.name_state):
          _class.execute()

      sleep(self.interval)

  # Executar todas as funcionalidades permitidas, sendo threads ou não
  def execute_all(self):
    for _class in self.classActivities.values():
      if get_variable(_class.name_state) and _class.state is False:
        _class.state = True
        _class.execute()

  # Executar uma determinada atividade em thread (por comando)
  def execute(self, activity):
    _class = self.classActivities[activity]

    set_variable(_class.name_state, True)

    if _class.state is False and _class.is_thread is True:
      _class.state = True
      _class.execute()

  # Terminar uma determinada atividade em thread (por comando)
  def finish(self, activity):
    _class = self.classActivities[activity]

    if _class.state is True and _class.is_thread is True:
      _class.state = False
      _class.finish()

  # Ativar o estado da variável de estado (por comando)
  def active(self, activity):
    _class = self.classActivities[activity]

    set_variable(_class.name_state, True)

  # Desativar o estado da variável de estado (por comando)
  def disable(self, activity):
    _class = self.classActivities[activity]

    set_variable(_class.name_state, False)

  def state(self, activity):
    _class = self.classActivities[activity]

    return f"Activity state: {_class.state}"