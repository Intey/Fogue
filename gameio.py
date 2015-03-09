import sys
import os

__name__ = "gameio"


# window = curses.initscr()

RESET_COLOR      = "0"
BLACK            = "30"
RED              = "31"
GREEN            = "32"
YELLOW           = "33"
BLUE             = "34"
MAGENTA          = "35"
CYAN             = "36"
WHITE            = "37"
BRIGHT_BLACK     = "90"
BRIGHT_RED       = "91"
BRIGHT_GREEN     = "92"
BRIGHT_YELLOW    = "93"
BRIGHT_BLUE      = "94"
BRIGHT_MAGENTA   = "95"
BRIGHT_CYAN      = "96"
BRIGHT_WHITE     = "97"
B_BLACK          = "40"
B_RED            = "41"
B_GREEN          = "42"
B_YELLOW         = "43"
B_BLUE           = "44"
B_MAGENTA        = "45"
B_CYAN           = "46"
B_WHITE          = "47"
B_BRIGHT_BLACK   = "100"
B_BRIGHT_RED     = "101"
B_BRIGHT_GREEN   = "102"
B_BRIGHT_YELLOW  = "103"
B_BRIGHT_BLUE    = "104"
B_BRIGHT_MAGENTA = "105"
B_BRIGHT_CYAN    = "106"
B_BRIGHT_WHITE   = "107"

ESC = "\x1b"

_RESET_COLOR = ESC + RESET_COLOR + "m"
_CLEAR_SCREEN = ESC + "[2J"
_RESET_TERMINAL = ESC + "c"

class Output:
    def __init__( self ):

        self.buffer = ""
        self.capturing = False

    def wr( self, s, forced=False ):
        """
        Write to sdtout, directly if `force` is True
        """
        if self.capturing and not forced:
            self.buffer += s
        else:
            sys.stdout.write( s )
            sys.stdout.flush()
        return
    def capture( self ):
        """
        Capture all output
        """
        self.capturing = True
        self.buffer = ""
        return
    def release( self, once=False ):
        """
        Release captured output
        if `once` is True, continue capturing
        """
        self.wr( self.buffer, True )
        if not once:
            self.capturing = False
        return
    def clear( self ):
        self.wr( ESC + "[2J" )
        return
    def reset( self ):
        """
        Reset everything!
        For grace clear screen exit
        """
        self.wr( RESET_COLOR + _CLEAR_SCREEN + _RESET_TERMINAL )
        return
    def size( self ):
        """
        Get terminal size, respectively
        Nix ony =P
        """
        rows, columns = os.popen( "stty size", "r" ).read().split()
        size = ( int(columns), int(rows) )
        return size
    def hideCursor( self ):
        # self.wr( '\x9B\x3F\x32\x35\x6C' )
        # self.wr( "\x9B\x3F\x32\x35\x6C" )
        self.wr( ESC + "[?25l" )
        # not working in this cloud IDE ={
        # also not work in *nix console
        return
    def page( self ):
        """
        Prepare fullscreen terminal layout
        Clear!
        Cursor at 1;1
        """
        ( _, height ) = self.size()
        self.clear()
        self.scroll( height )
        self.move( 1, 1 )
        return
    def scroll( self, n=1 ):
        """
        Scroll to `n` rows!
        """
        self.wr( ESC + "[" + str( n ) + "G" )
        return
    def move( self, x=0, y=0 ):
        """"""
        self.wr( ESC + "[" + str(y) + ";" + str(x) + "f" )
        return
    def char( self, char, x=1, y=1 ):
        self.move( x, y )
        self.wr( char )
        return

import tty
import termios
import select

global_aliases = {
    b'\x1b'   : "escape",
    b'\x1b[A' : "up",
    b'\x1b[B' : "down",
    b'\x1b[C' : "right",
    b'\x1b[D' : "left",
    b'\r'     : "enter",
    b' '      : "space"
}

class Input:

    def __init__( self ):
        self.aliases = {}
        return

    def alias( self, alias, *chars ):
        """
        Alias chars
        example:
            `alias( "up", "w", "W", "k" )`
            Now pressing 'w', 'W' and 'k' will return 'up'
        Note of `global_aliases`
        """
        if chars:
            for char in chars:
                self.aliases[ char ] = alias
        else:
            char = alias
            if char in global_aliases:
                char = global_aliases[ char ]
            if type( char ) is not str:
                char = char.decode( "utf-8" )
            if char in self.aliases:
                char = self.aliases[ char ]
            return char
        return

    def moreData( self ):
        """
        Checks sys.stdin for more input!
        """
        return select.select( [ sys.stdin ], [], [], 0 ) == ( [ sys.stdin ], [], [] )

    def char( self ):
        """
        Get char from stdin (bloking!)
        """
        # http://stackoverflow.com/questions/8757915/how-to-turn-console-echo-back-on-after-tty-setcbreak
        # http://www.darkcoding.net/software/non-blocking-console-io-is-not-possible/

        char = None
        old_settings = termios.tcgetattr( sys.stdin )
        try:
            # enable raw mode, read char
            tty.setraw( sys.stdin.fileno() )
            tty.setcbreak( sys.stdin.fileno() )
            char = sys.stdin.buffer.raw.read( 1 )
            while self.moreData():
                char += sys.stdin.buffer.raw.read( 1 )
        finally:
            # roll terminal setting back
            termios.tcsetattr( sys.stdin, termios.TCSADRAIN, old_settings )
        return self.alias( char )

    # def string( self ):
    #     """"""
    #     return ""

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
