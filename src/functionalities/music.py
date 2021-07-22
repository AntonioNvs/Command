from webbrowser import open_new
from src.error.classError import Error
from youtubesearchpython import VideosSearch

# Links das playlists
playlist = {
  'eletronic': ''
}

def search_and_open_music(textSearch):
  resultSearch = VideosSearch(textSearch, limit = 2)

  url = resultSearch.result()["result"][0]["link"]

  open_new(url)

def open_a_playlist_with_type(_type: str) -> Error or None:
  if not _type in playlist.keys():
    return Error('There is no playlist determined.')

  open_new(playlist[_type])

def access_lofi() -> None:
  open_new('https://www.youtube.com/watch?v=5qap5aO4i9A')