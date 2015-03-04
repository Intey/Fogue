# import curses
import sys

# window = curses.initscr()

RESET_COLOR		 = 0
BLACK 		     = 30
RED 			 = 31
GREEN 		     = 32
YELLOW 		     = 33
BLUE 			 = 34
MAGENTA 		 = 35
CYAN 			 = 36
WHITE 		     = 37
BRIGHT_BLACK 	 = 90
BRIGHT_RED 	     = 91
BRIGHT_GREEN 	 = 92
BRIGHT_YELLOW    = 93
BRIGHT_BLUE 	 = 94
BRIGHT_MAGENTA   = 95
BRIGHT_CYAN 	 = 96
BRIGHT_WHITE 	 = 97
B_BLACK 		 = 40
B_RED 			 = 41
B_GREEN 		 = 42
B_YELLOW 		 = 43
B_BLUE 			 = 44
B_MAGENTA 		 = 45
B_CYAN 			 = 46
B_WHITE 		 = 47
B_BRIGHT_BLACK 	 = 100
B_BRIGHT_RED 	 = 101
B_BRIGHT_GREEN 	 = 102
B_BRIGHT_YELLOW  = 103
B_BRIGHT_BLUE 	 = 104
B_BRIGHT_MAGENTA = 105
B_BRIGHT_CYAN 	 = 106
B_BRIGHT_WHITE 	 = 107

ESC = "\x1b"
CLEAR_SCREEN = ESC + "[2J"
HIDE_CURSOR = "\x9B\x3F\x32\x35\x6C"

class Output:
    def __init__( self ):
        
        self.buffer = ""
        self.currentStyle = []
        
        # Init curses
        # self.window = window #!!!!!
        # curses.noecho()
        # curses.cbreak()         # don't perform <Enter> after user input
        # curses.start_color()    # enable colors
        # curses.curs_set(0)      # hide cursor
        # self.window.keypad(1)           # hz
        # curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    def char( self, char, x, y, color ):
        
        # self.window.addch( y, x, char, color )
        
        if color != None:
            self.style( color )
            
        if x != None and y != None:
            self.move( x, y )
        
        self.buffer += char
        
        if color != None:
            self.style( None )
        
        return
    
    def move( self, x=0, y=0 ):
        self.buffer += ESC + "[" + x + ";" + "f"
        return
    
    def style( self, mods ):
        if mods is None:
            mods = [ RESET_COLOR ]
        self.buffer += ESC + ";".join( mods ) + "m"
        return
    
    def clearScreen( self ):
        self.buffer += CLEAR_SCREEN
        return
    
    def redraw( self, ):
        sys.stdout.write( self.buffer )
        self.buffer = ""
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