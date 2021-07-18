from error.classError import Error

def get_a_specific_value_in_a_command(text: str, position: int) -> str or Error:
  # Tenta achar a devida posição no comando, se não existir, retorne um erro
  try: 
    return text.split(' ')[position]
  except:
    return Error("It was not possible to obtain information from the given command")