from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class Protocol:
  def __init__(self) -> None:
    pass

  def work(self, text, window):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
      IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(currentVolumeDb + 6.0, None)

    # self.window.send_answer("Protocol 'Work' has activated.")

    window.send_answer("Volume has changed!")

  def sum(self):
    pass