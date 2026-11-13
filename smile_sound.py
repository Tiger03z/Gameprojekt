import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import sys, subprocess

def spill_lyd(fil):
    if sys.platform == "win32":
        import winsound
        winsound.PlaySound(fil, winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        subprocess.Popen(["afplay", fil])

spill_lyd("smile.wav")
