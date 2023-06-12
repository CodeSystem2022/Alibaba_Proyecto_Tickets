import curses
from curses import wrapper

def LimpiarPantalla(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.getch()

wrapper(LimpiarPantalla)