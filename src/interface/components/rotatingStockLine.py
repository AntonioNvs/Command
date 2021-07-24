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

    self.stocks = ["ABEV3"]
    self.add_stocks("ABEV3", 3.54)
    self.add_stocks("VIVR4", -0.54)
    self.add_stocks("ITUB4", 0.24)
    self.add_stocks("USIM5", 1.21)
    self.add_stocks("MULT4", -0.24)
    self.add_stocks("BBDR4", 4.50)
    self.add_stocks("MGL3", 8.54)

    self.ind = 0
    self.window = window

    self.animation()

  def add_stocks(self, text: str, value: float):
    frame = tk.Frame(
      self,
      bg=self.bg,
      name=f"stockFrame{len(self.labels_of_stocks)}"
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

  def animation(self):
    self.limit = 5

    assert len(self.labels_of_stocks) > self.limit

    # Ocultando as ações do atual self.limite
    for stock in self.select_stocks():
      stock[0].grid_forget()

    # Definindo as ações que serão visíveis
    self.ind = self.ind + 1 if (self.ind+1)*self.limit < len(self.labels_of_stocks) else 0

    for i, stock in enumerate(self.select_stocks()):
      frame = stock[0]
      frame.grid(column=i, row=0, padx=8)

    self.window.after(2000, self.animation)

  def select_stocks(self):
    if (self.ind+1)*self.limit > len(self.labels_of_stocks):
      end = len(self.labels_of_stocks)
    else:
      end = (self.ind+1)*self.limit

    return self.labels_of_stocks[self.limit*self.ind: end]