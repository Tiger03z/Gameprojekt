import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from custum_meny import velg
grid =[
    ["hallo"],
    ["hei"]
]
valg = velg(grid)