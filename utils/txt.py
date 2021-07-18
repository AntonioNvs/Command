path_to_file = 'database/variable.txt'

def read(file) -> list:
  with open(file, 'r') as source:
    return source.read().split('\n')


def get_variable(variable):
  with open(path_to_file, 'r') as source:
    # Encontrando a linha com a variável especificada
    line_with_variable = [line for line in source.read().split('\n') if variable in line]

  return line_with_variable[0].split(" ")[1]


def set_variable(variable, value):
  lines = read(path_to_file)

  for i, line in enumerate(lines):
    if variable in line:
      lines[i] = variable + " " + str(value)

  with open(path_to_file, 'w') as source:
    for line in lines:
      source.write(line)

if __name__ == "__main__":
  print(set_variable('get_process', True))

