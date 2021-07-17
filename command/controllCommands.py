from command.functions.controllFunctions import ControllFunctions

class ControllCommands:
  def __init__(self, window = None) -> None:
    self.controllFunctions = ControllFunctions(window)

    self.window = window
    self.all_commands = self.controllFunctions.get_all_commands()

  def set_window(self, window):
    self.window = window

  def execute_a_command(self, text):
    list_arguments = text.split(' ')

    def recursive_command(index, actualVariable):
      if type(actualVariable) is not dict:
        actualVariable(text, self.window)
        return

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