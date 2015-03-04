import curses

window = curses.initscr()

class Output:
    def __init__( self ):
        
        # Init curses
        self.window = window #!!!!!
        curses.noecho()
        curses.cbreak()         # don't perform <Enter> after user input
        curses.start_color()    # enable colors
        curses.curs_set(0)      # hide cursor
        self.window.keypad(1)           # hz
        # curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    def char(x, y, color, char="."):
        wnd.addch( y, x, char, color )
        return

class Input:
    
    def __init__( self ):
        self.window = window #!!!!!
        self.aliases = {}
        ""
    # chars....
    def alias( self, *chars, alias ):
        for char in chars:
            self.aliases[ char ] = alias
    
    def char():
        ch = self.window.getch()
        if ch in self.aliases:
            return 0