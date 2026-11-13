from taster import les_tast

def tøm_skjerm():
    print("\033[H\033[2J\033[3J", end="", flush=True)

def tegn_grid(grid, x, y):
    tøm_skjerm()
    for rad in range(len(grid)):
        linje = ""
        for kolonne in range(len(grid[rad])):
            ord = grid[rad][kolonne]
            if kolonne == x and rad == y:
                linje += f"[{ord:^9}]"
            else:
                linje += f" {ord:^9} "
        print(linje)

def velg(grid):
    høyde = len(grid)
    bredde = len(grid[0])
    x, y = 0, 0
    print("\033[?25l", end="", flush=True)
    try:
        while True:
            tegn_grid(grid, x, y)
            tast = les_tast()
            if tast == "opp":
                y = max(0, y - 1)
            elif tast == "ned":
                y = min(høyde - 1, y + 1)
            elif tast == "venstre":
                x = max(0, x - 1)
            elif tast == "høyre":
                x = min(bredde - 1, x + 1)
            elif tast == "enter":
                return grid[y][x]
    finally:
        print("\033[?25h", end="", flush=True)

if __name__ == "__main__":
    test = [
        ["Start", "Load", "Help", "Kill"],
        ["Sound", "Music", "Keys", "Quit"],
    ]
    print("You picked:", velg(test))