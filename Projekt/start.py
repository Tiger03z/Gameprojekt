import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from custum_meny import velg
from smile import smiling_time
from smile_sound import spill_lyd

def hovedmeny():
    valg = velg([["Start"], ["Innstillinger"], ["Quit"]])
    if valg == "Start":
        return "spill"
    if valg == "Innstillinger":
        return "innstillinger"
    return "quit"

def innstillinger():
    valg = velg([["Lyd: på/av"], ["Tilbake"]])
    if valg == "Lyd: på/av":
        return "innstillinger"
    if valg == "Tilbake":
        return "hovedmeny"
    return "innstillinger"

def spill():
    valg = velg([["New save"], ["Lode save"],["Tilbake"]])
    if valg =="New save":
        return "new save"
    if valg =="Lode save":
        return "lode save"
    return "hovedmeny"

sider = {
    "hovedmeny": hovedmeny,
    "innstillinger": innstillinger,
    "spill": spill,
}

side = "hovedmeny"
while side != "quit":
    side = sider[side]()

spill_lyd("smile.wav")
smiling_time()