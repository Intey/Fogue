import gameio

directions = {
    "up"   : [  0, -1 ],
    "down" : [  0,  1 ],
    "right": [  1,  0 ],
    "left" : [ -1,  0 ]
}

def move( creature, direction ):
    creature[ "x" ] += directions[ direction ][ 0 ]
    creature[ "y" ] += directions[ direction ][ 1 ]
    return

def dothemagic():
    # 1. draw
    # 2. input
    # 3. login
    
    player = {
        "x"    : 10,
        "y"    : 1,
        "char" : "@"
    }
    
    o.page()
    o.hideCursor()
    
    while 1:
        ch = i.char()
        if ch in directions:
            move( player, ch )
        
        o.clear()
        o.char(
            player[ "char" ],
            player[ "x" ],
            player[ "y" ]
        )
        o.move( 1, 1 )
        
        if ch is "escape":
            o.reset()
            break
    
    return
    
o = gameio.Output()
i = gameio.Input()

dothemagic()

# o.reset()