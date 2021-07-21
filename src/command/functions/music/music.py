from src.interface.index import Interface
from src.functionalities.music import open_a_playlist_with_type
from src.error.classError import Error
from src.utils.manipulating_command import get_a_specific_value_in_a_command
from src.functionalities.open import open_a_url
from src.error.actions import error_ocured

class Open:
  def __init__(self, window: Interface) -> None:
    self.window = window

  def playlist(self, text):
    playlist = get_a_specific_value_in_a_command(text, 2)

    if error_ocured(playlist, lambda e: self.window.send_answer(e.message)):
      return

    if 'http' in playlist:
      open_a_url(playlist)
    else:
      result = open_a_playlist_with_type(playlist)

      if error_ocured(result, lambda e: self.window.send_answer(e.message)):
        return

    self.window.send_answer('Playlist open of success!')