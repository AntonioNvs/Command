from src.error.classError import Error

def error_ocured(error, callback) -> bool:
  if isinstance(error, Error):
    callback(error)
    return True
  return False