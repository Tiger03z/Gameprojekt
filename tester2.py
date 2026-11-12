import os
from taster import les_tast

def tøm_skjerm():
    print("\033[H\033[2J\033[3J", end="", flush=True)
def meny(valg):
    valgt = 0
    while True:
        tøm_skjerm()
        print("=== HOVEDMENY ===\n")
        for i, tekst in enumerate(valg): #0 Start spill 1 Last inn 2 Avslutt) exepel på hvordan det prites ut
            if i == valgt:
                print(f"> {tekst} <")
            else:
                print(f"  {tekst}")
                
        tast = les_tast()
        if tast == "opp":
            valgt = (valgt - 1) % len(valg)
        elif tast == "ned":
            valgt = (valgt + 1) % len(valg)
        elif tast == "enter":
            return valg[valgt]
print("\033[?25l", end="", flush=True)
try:
    resultat = meny(["Start spill", "Last inn", "Innstillinger", "Avslutt"])
finally:
    print("\033[?25h", end="", flush=True)

print("Du valgte:", resultat)