import tkinter as tk

class RotatingStockLine(tk.Frame):
  def __init__(self, window: tk.Tk) -> None:
    self.bg = "#0f0f0f"

    super().__init__(
      window,
      bg=self.bg,
      height=32
    )

    self.pack(side=tk.TOP, fill=tk.X)

    self.labels_of_stocks = []

    self.stocks = [
      "ABEV3", "B3SA3", "BBDC3", "CMIG4", "CSMG3",
      "ELET6", "GGBR4", "GOLL4", "ITSA4", "ITUB4", 
      "LREN3", "MGLU3", "MULT3", "PETR4", "USIM5", 
      "VALE3", "WEGE3", "BIDI11", "OIBR3", "VIVR3"]

      
    self.ind = 0
    self.window = window

    self.animation()

  def add_stocks(self, text: str, value: float) -> None:
    frame = tk.Frame(
      self,
      bg=self.bg
    )

    stock_lbl = tk.Label(
      frame,
      text=text,
      bg=self.bg,
      font=("Arial", 14),
      fg="#FFFFFF"
    )

    color = "#00FF00" if value > 0 else "#FF0000"

    value_lbl = tk.Label(
      frame,
      bg=self.bg,
      text=f'{value}%',
      font=("Arial", 14),
      fg=color
    )

    # Posicionamento dos elementos com 'grid'
    stock_lbl.grid(column=0, row=0, padx=2)
    value_lbl.grid(column=1, row=0)
    
    self.labels_of_stocks.append((frame, stock_lbl, value_lbl))

  def destroy_widgets(self):
    # Eliminando os elementos
    for stock in self.labels_of_stocks:
      stock[0].destroy() 

    self.labels_of_stocks = []

  def updated_stocks_values(self, stocks_values: list) -> None:
    self.destroy_widgets()

    for stock in stocks_values:
      self.add_stocks(stock[0], stock[1])


  def animation(self) -> None:
    self.limit = 5

    # Caso nenhuma ação tenha sido coletada ainda
    if len(self.labels_of_stocks) != 0:
      # Ocultando as ações do atual self.limite
      for stock in self.select_stocks():
        stock[0].grid_forget()

      # Definindo as ações que serão visíveis
      self.ind = self.ind + 1 if (self.ind+1)*self.limit < len(self.labels_of_stocks) else 0

      for i, stock in enumerate(self.select_stocks()):
        frame = stock[0]
        frame.grid(column=i, row=0, padx=8)

    self.window.after(4000, self.animation)

  def select_stocks(self):
    if (self.ind+1)*self.limit > len(self.labels_of_stocks):
      end = len(self.labels_of_stocks)
    else:
      end = (self.ind+1)*self.limit

    return self.labels_of_stocks[self.limit*self.ind: end]