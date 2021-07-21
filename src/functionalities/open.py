from webbrowser import open_new
from src.error.classError import Error
import subprocess


executables = {
  'vscode': 'C:\\Users\\tonim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
  'notion': 'C:\\Users\\tonim\\AppData\\Local\\Programs\\Notion\\Notion.exe'
}

def open_a_url(url: str) -> None:
  open_new(url)

def execute_a_program(program: str) -> Error or None:
  assert program in executables.keys() # Se o programa existe na lista de executáveis

  try:
    subprocess.call(executables[program]) 
  except FileNotFoundError:
    return Error(f'Unable to open program {program}')
