import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from custum_meny import velg
from smile import smiling_time

start_meny =[
    ["Start"],
    ["Options"],
    ["Quit"]
]
valg = velg(start_meny)
if valg == "Quit":
    smiling_time()