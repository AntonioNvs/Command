"""
  Controle de todas as atividades em paralelo do programa
"""

from parallel.actives import ParallelActivities

class Parallel(ParallelActivities):
  def __init__(self, window) -> None:
    super().__init__(window)
    self.key = "p"

    self.execute_all()

  # Executando o comando para determinada atividade
  def command_for_activity(self, text: str, window) -> None:
    activity = ""
    try:
      _, activity, method = text.split(' ')
    except ValueError:
      window.send_answer("Missing more information in the command!")
      return

    try:
      self.classActivities[activity] # Atividade existe?
      retr = getattr(self, method)(activity) # Método existe? Sim execute
      
      # O retorno sendo 'str', quer dizer que emitiu uma resposta ao usuário
      if isinstance(retr, str):
        window.send_answer(retr)
      else:
        window.send_answer("Method executed successfully!")
    except KeyError:
      window.send_answer("This activity does not exist.")
    except AttributeError:
      window.send_answer("There is no such method.")

  # Terminando as atividades no caso de fechar a tela
  def finish_the_activities(self, window):
    window.send_answer("Terminando todas as atividades..")

    self.program_is_running = False

    # Finalizando as threads
    for _class in self.classActivities.values():
      _class.state = False

    # Estados falsos de todas as threads em execução
    threads_is_finished = [False for _class in self.classActivities.values() if _class.is_thread is True]
    
    # Verificando se todas as threads terminaram sua execução
    while not all(threads_is_finished):
      for i, _class in enumerate(self.classActivities.values()):
        if _class.is_thread is True:
          threads_is_finished[i] = not _class.th.is_alive()
          print(f'{_class.name} is finished!')
