from functionalities.open import open_a_url
from interface.index import Interface

class Open:
  def __init__(self, window: Interface) -> None:
    self.window = window

  def teams(self, text):
    url = "https://teams.microsoft.com/_#/school//?ctx=teamsGrid"

    open_a_url(url)

    self.window.send_answer("Teams was opened")


  