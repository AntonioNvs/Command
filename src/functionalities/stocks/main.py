from src.functionalities.stocks.get_stocks import get_stocks_value
from threading import Thread
from time import clock


class StocksControll:
  name = "stocks"
  
  def __init__(self, window) -> None:
    self.name_state = "stocks_value"
    self.is_thread = True
    self.state = False
    self.th = Thread(target=self.loop_update)

    self.window = window

    self.interval = 900 # 15 minutos para cada atualização de ação

  def loop_update(self):
    first_time = -self.interval + 1

    while self.state:
      if clock() - first_time > self.interval:
        stocks = get_stocks_value(self.window.rotatingStockLine.stocks)
        self.window.rotatingStockLine.updated_stocks_values(stocks)

        first_time = clock()

  def execute(self):
    # Instanceando a thread do loop de captura de dados de ações
    self.th.start()

  def finish(self):
    self.window.rotatingStockLine.destroy_widgets()
    