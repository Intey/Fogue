import curses


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0


def init_window():  # move this in another module
    wnd = curses.initscr()
    curses.noecho()
    curses.cbreak()  # don't perform <Enter> after user input
    curses.start_color()  # enable colors
    curses.curs_set(0)  # hide cursor
    wnd.keypad(1)  # hz
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    return wnd


def nop(any):
    return


def reset():
    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)
    wnd.keypad(0)
    curses.endwin()


def moveUp(p):
    p.y -= 1


def moveDown(p):
    p.y += 1


def moveLeft(p):
    p.x -= 1


def moveRight(p):
    p.x += 1


def processInput(char):
    """ Convert char to function with parameter - player.
    made on map where key is inputed char, and value is action function.
    BUG: when char is not found in keys - it return string (WAT)
    """
    return {ord('w'): moveUp,
            ord('s'): moveDown,
            ord('a'): moveLeft,
            ord('d'): moveRight,
            ord(' '): nop
            }.get(char, ' ')  # this should replase not founded char with ' '


def gameLoop():
    """main loop with blackjack and hookers! """
    char = 'w'
    p = Player
    p.x = 40
    p.y = 10
    while char != ord('q'):
        wnd.erase()
        # addstr|addchar get in params (y, x,...). First is Y.
        wnd.addstr(0, 0, "x=" + str(p.x), curses.color_pair(1))
        wnd.addstr(1, 0, "y=" + str(p.y), curses.color_pair(1))
        wnd.addch(p.y, p.x,  "@", curses.color_pair(1))
        wnd.refresh()
        char = wnd.getch()
        move_func = processInput(char)
        move_func(p)


wnd = init_window()  # create color pair
gameLoop()
reset()
