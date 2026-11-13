import os
import sys
import subprocess

MAPPE = os.path.dirname(os.path.abspath(__file__))



def spill_lyd(fil):
    sti = os.path.join(MAPPE, "lyder", fil)
    if sys.platform == "win32":
        import winsound
        winsound.PlaySound(sti, winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        subprocess.Popen(["afplay", sti])


if __name__ == "__main__":
    import time
    spill_lyd("smile.wav")
    time.sleep(3)
