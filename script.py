import sys
import curses
char = ""
wnd = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
curses.curs_set(0)
wnd.keypad(1)
while char != 'q':
    char = sys.stdin.read(1)
    wnd.erase()
    wnd.addch(char)
    wnd.refresh()

# reseting
curses.nocbreak(); wnd.keypad(0); curses.echo()
curses.curs_set(1)
curses.endwin()


class Myown:
    def act():
        print("act")
