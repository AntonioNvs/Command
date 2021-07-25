# Desabilitando a criação do __pycache__
import sys
sys.dont_write_bytecode = True

from src.interface.index import Interface

Interface()

