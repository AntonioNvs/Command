from webbrowser import open_new

from src.error.classError import Error

# Links das playlists
playlist = {
  'eletronic': ''
}


def open_a_playlist_with_type(_type: str) -> Error or None:
  if not _type in playlist.keys():
    return Error('There is no playlist determined.')

  open_new(playlist[_type])

def access_lofi() -> None:
  open_new('https://www.youtube.com/watch?v=5qap5aO4i9A')