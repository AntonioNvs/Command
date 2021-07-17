import os
import re
from importlib import import_module
from inspect import isclass

class ControllFunctions:
  def __init__(self, window) -> None:
    actual_path = os.path.dirname(os.path.realpath(__file__))

    all_folders = list(os.walk(actual_path))[1:]

    self.all_commands = {}

    for folder in all_folders:
      # Transformando o caminho em componentes de uma lista
      path_to_directory = re.sub("[^a-zA-Z]+", "-", folder[0].replace(actual_path, "")[1:]).split("-")
      
      # Caso tenha a pasta de cachê do python, ignore-a
      if "pycache" in path_to_directory:
        continue
      
      info_class = tuple()

      # Listando todos os arquivos da pasta
      for file in folder[2]:
        path_to_file = "command.functions." + ".".join(path_to_directory) + f".{file.replace('.py', '')}"

        module = import_module(path_to_file)
        
        # Obtendo a classe principal e separando cada módulo
        for attribute_name in dir(module):
          attribute = getattr(module, attribute_name)

          if isclass(attribute):
            _class = attribute()

            all_methods = [method for method in dir(_class) if method.startswith('__') is False]

            info_class = (_class, all_methods)

      # Função de recursividade para todas as formas de comando com sua respectiva função
      def recursive_commands(index, actual):
        if index == len(path_to_directory):
          _class, all_methods = info_class

          for method in all_methods:
            actual[method] = getattr(_class, method)

          return

        try:
          if len(actual[path_to_directory[index]]) != 0:
            pass
        except:
          actual[path_to_directory[index]] = {}

        index += 1

        recursive_commands(index, actual[path_to_directory[index-1]])

      if len(info_class) != 0:
        recursive_commands(0, self.all_commands)

  def get_all_commands(self):
    return self.all_commands

if __name__ == "__main__":
  ControllFunctions()