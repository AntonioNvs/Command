from src.command.functions.controllFunctions import ControllFunctions

class ControllCommands:
  def __init__(self, window = None) -> None:
    self.controllFunctions = ControllFunctions(window)

    self.window = window
    self.all_commands = self.controllFunctions.get_all_commands()

  def set_window(self, window):
    self.window = window

  def execute_a_command(self, text):
    list_arguments = text.split(' ')

    def recursive_command(index, actualVariable) -> None:
      if type(actualVariable) is not dict:
        actualVariable(text)
        return

      # Caso o comando(classe) tenha uma função com seu nome, ela é executada
      if list_arguments[index] in actualVariable.keys():
        key = list_arguments[index]
        new_dict = actualVariable[key]

        try:
          # Se o comando tiver uma função com mesmo nome e o próximo argumento não estiver como método, execute.
          if key in new_dict.keys() and type(new_dict[key]) is not dict and not list_arguments[index+1] in new_dict.keys():
            new_dict[key](text)
            return
        except:
          pass

      if index == len(list_arguments):
        self.window.send_answer("This command does not exist")
        return

      _index = index
      index += 1

      for key in actualVariable:
        if key == list_arguments[_index]:
          recursive_command(index, actualVariable[key])
          break

    recursive_command(0, self.all_commands)


if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))