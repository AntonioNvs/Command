from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def change_volume(db: float):
  devices = AudioUtilities.GetSpeakers()
  interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

  volume = cast(interface, POINTER(IAudioEndpointVolume))
   
  currentVolumeDb = volume.GetMasterVolumeLevel()
  volume.SetMasterVolumeLevel(currentVolumeDb + db, None)