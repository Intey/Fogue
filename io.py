import curses

window = curses.initscr()

BLACK   = curses.COLOR_BLACK
RED     = curses.COLOR_RED
GREEN   = curses.COLOR_GREEN
YELLOW  = curses.COLOR_YELLOW
BLUE    = curses.COLOR_BLUE
MAGENTA = curses.COLOR_MAGENTA
CYAN    = curses.COLOR_CYAN
WHITE   = curses.COLOR_WHITE

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

    def char( self, x, y, color, char="." ): 
        self.window.addch( y, x, char, color )
        return

class Input:
    
    def __init__( self ):
        self.window = window #!!!!!
        self.aliases = {}
        ""
    # chars....
    def alias( self, alias, *chars ):
        for char in chars:
            self.aliases[ char ] = alias
        return
    
    def char( self ):
        ch = self.window.getch()
        if ch in self.aliases:
            ch = self.aliases[ ch ]
        return ch