import sys

if sys.platform == "win32":
    import msvcrt

    def les_tast():
        tast = msvcrt.getwch()
        if tast in ("\x00", "\xe0"):  # piltaster starter med en spesialkode
            tast = msvcrt.getwch()
            return {"H": "opp", "P": "ned", "K": "venstre", "M": "høyre"}.get(tast, "")
        if tast == "\r":
            return "enter"
        return tast
else:
    import termios, tty

    def les_tast():
        fd = sys.stdin.fileno()
        gammel = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            tast = sys.stdin.read(1)
            if tast == "\x1b":  # piltaster starter med ESC [
                tast += sys.stdin.read(2)
                return {"\x1b[A": "opp", "\x1b[B": "ned", "\x1b[D": "venstre", "\x1b[C": "høyre"}.get(tast, "")
            if tast in ("\r", "\n"):
                return "enter"
            return tast
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, gammel)