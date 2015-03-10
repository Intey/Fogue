# import gameio
import random
import math


class YayMap():
    def __init__( self, width, height, debugContext=None ):
        self.regions = []
        self.width   = width
        self.height  = height
        
        self.dctx = debugContext
        
        self.generate()
        
    def generate( self ):
        
        ROOM_WIDTH  = [ 5, 5 ]
        ROOM_HEIGHT = [ 2, 2 ]
        TILE_EXPAND = 1.3
        TILE_BORDER = 1
        ROOM_RATIO  = 0.33
        
        tileWidth  = int( ( ROOM_WIDTH[ 0 ]  + ROOM_WIDTH[ 1 ]  + TILE_BORDER ) * TILE_EXPAND )
        tileHeight = int( ( ROOM_HEIGHT[ 0 ] + ROOM_HEIGHT[ 1 ] + TILE_BORDER ) * TILE_EXPAND )
        
        tilesX = self.width  // tileWidth
        tilesY = self.height // tileHeight
        
        tilesMap = {}
        tiles = []
        
        for x in range( 0, tilesX ):
            for y in range( 0, tilesY ):
                
                tile = dict(
                    room = None,
                    x = x * tileWidth,
                    y = y * tileHeight,
                    width  = tileWidth,
                    height = tileHeight
                )
                
                tiles.append( tile )
                tilesMap[ str( x ) + "_" + str( y ) ] = tile
        
        if self.dctx:
            for x in range( tilesX ):
                for y in range( tilesY ):
                    # self.dctx.__pushStyle__( [ random.choice( [ "41", "42", "43", "44", "45", "46", "47", "101", "102", "103", "104", "105", "106", "107" ] ) ] )
                    self.dctx.__pushStyle__( [ ( "47" if ( x + y ) % 2 else "46" ) ] )
                    self.dctx.__move__( x * tileWidth, y * tileHeight )
                    self.dctx.__drawRectRelative__( 0, 0, tileWidth, tileHeight, " " )
                    self.dctx.__popStyle__()
        
        roomsCount = int( len( tiles ) * ROOM_RATIO )
        
        unusedTiles = tiles.copy()
        random.shuffle( unusedTiles )
        
        rooms = []
        
        for i in range( roomsCount ):
            tile = unusedTiles.pop()
            
            # create room in free tile
            
            width  = ROOM_WIDTH[ 0 ]  + random.randint( 0, ROOM_WIDTH[ 1 ] )
            height = ROOM_HEIGHT[ 0 ] + random.randint( 0, ROOM_HEIGHT[ 1 ] )
            
            x = tile[ "x" ] + random.randint( 0, tile[ "width" ] - TILE_BORDER  - width ) 
            y = tile[ "y" ] + random.randint( 0, tile[ "height" ] - TILE_BORDER - height )
            
            room = dict(
                width  = width,
                height = height,
                x = x,
                y = y
            )
            
            tile[ "room" ] = room
            rooms.append( room )
        
        if self.dctx:
            self.dctx.__pushStyle__( [ "37", "43" ] )
            for room in rooms:
                self.dctx.__move__( room[ "x" ], room[ "y" ] )
                self.dctx.__drawRectRelative__( 0, 0, room[ "width" ], room[ "height" ], "." )
            self.dctx.__popStyle__()
        
        return


    def draw( self, ctx ): pass




class PeeMap():
    
    ROOM_WIDTH  = [ 5, 5 ]
    ROOM_HEIGHT = [ 2, 2 ]
    DIRECTIONS = dict(
        up    = [ 0, -1 ],
        down  = [ 0, 1 ],
        right = [ 1, 0 ],
        left  = [ -1, 0 ]
    )
    
    def __init__( self, width, height, dctx ):
        self.width  = width
        self.height = height
        self.dctx   = dctx
        
        self.generate()
        
    def generate( self ):
        
        buff = {}
        
        room = self.createRoom( ( 0, 0, self.width, self.height ) )
        roomToBuffer( room, buff )
        
        rooms = []
        
        return

    def getAreaFromBuffer( self, room, startx, starty, direction, buff ):
        
        modx = PeeMap.DIRECTIONS[ direction ][ 0 ]
        mody = PeeMap.DIRECTIONS[ direction ][ 1 ]
        
        x = startx
        y = starty
        
        
        spaceBefore = ( 0 if modx is  1 or mody is -1 else ( self.width if mody is  1 else self.height ) )
        spaceAfter  = ( 0 if modx is -1 or mody is  1 else ( self.width if mody is -1 else self.height ) )
        spaceAhead  = ( 0 if modx is -1 or mody is -1 else ( self.width if modx is  1 else self.height ) )
        
        while spaceAhead:
            
            spaceAhead -= 1
            
            x += modx
            y += mody
            
            # check ahead
            
            if str( x ) + "_" + str( y ) in buff:
                break
            
            
            
            # check sides
            
            sidex = x
            sidey = y
            
            if modx:
                # horizontal
            else:
                # vertical
                i = sidex
                while i <= self.width:
                    i += 1
                    if str( i ) + "_" + str( y ) in buff:
                        break
        #####
        #   #
        # @ #
        #   #
        #####
        
        return
    
    def roomToBuffer( self, room, buff ):
        for x in range( 0, room[ "width" ] ):
            for y in range( 0, room[ "height" ] ):
                buf[ str( x + room[ "x" ] ) + "_" + str( y + room[ "y" ] ) ] = room
        return

    def createRoom( self, area ):
        
        ( areaX, areaY, areaWidth, areaHeight ) = area
        
        width  = PeeMap.ROOM_WIDTH[ 0 ]  + random.randint( 0, PeeMap.ROOM_WIDTH[ 1 ] )
        height = PeeMap.ROOM_HEIGHT[ 0 ] + random.randint( 0, PeeMap.ROOM_HEIGHT[ 1 ] )
        
        x = areaX + random.randint( 0, areaWidth  - width ) 
        y = areaY + random.randint( 0, areaHeight - height )        
        
        room = dict(
            width  = width,
            height = height,
            x = x,
            y = y
        )
        
        return room
        
        




class Item():
    def __init__(self, x, y):
        self.name = "unknown"
        self.x = x
        self.y = y

    def draw(self, context):
        context.char(self.x, self.y, self.color)


class Room():
    def __init__(self, x, y, w, h):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.creatures = []
        self.items = []

    def draw(self, context):
        for self.x in range(self.x, self.width):
            for self.y in range(self.y, self.height):
                context.char(self.x, self.y, ".")
        for creature in self.creatures:
            creature.draw(context)
        for item in self.items:
            item.draw(context)
        # return

    def addCreature(self, creature):
        self.creatures.append(creature)  # ok

    def getConnection(self, room):
        """Connect 2 rooms by nearest path.
        TODO: Determine nearest sides: check horizontal check vertical.
        """
        for x in range(room.x, room.width):
            if range(self.x, self.width).__contains__(x):
                corrX = random.randint(x, self.width)
                return (corrX,
                        max(self.y, room.y),
                        min(self.y + self.height, room.y + room.height))

        for y in range(room.y, room.height):
            if range(self.y, self.height).__contains__(y):
                corrY = random.randint(y, self.height)
                return (corrY,
                        max(self.x, room.x),
                        min(self.x + self.width, room.x + room.widht))


class Map():
    def __init__(self, width, height, tiles_count=16):
        self.points = {}
        self.rooms = []
        self.width = width
        self.height = height
        self.tiles_count = tiles_count
        # no need for self, __init__ runtime only
        tiles = self.getTiles(tiles_count)
        self.fillTileWithRooms(tiles, 1)  # (random.randrange(4, 11) / 10))
        # self.connectRooms()

    def getTiles(self, count):
        """On init we know screenx, screeny - width, and height.
        Should create count of tiles."""
        rows, cols = getMaxDividers(count)

        # assert((rows >= 2),
        #        "%s too few rows for tiles count %s" % (rows, count))
        # assert((cols >= 2),
        #        "%s too few cols for tiles count %s" % (cols, count))

        # tiles sizes
        width = self.width // cols
        height = self.height // rows
        # TODO: needs debug screen. or log file writing
        # print("screen w:h :: %s:%s" % (self.width, self.height))
        # print("tiles w:h :: %s:%s" % (width, height))
        # print("tiles rows:cols :: %s:%s" % (rows, cols))
        # cols = self.width // width
        # rows = self.height // height
        # prepare return
        # nums = rows * cols
        unused = []
        for r in range(0, rows):
            for c in range(0, cols):
                unused.append(Tile(c * width, r * height, width, height))
        return unused

    def fillTileWithRooms(self, tiles, room_ratio=1):
        """Generate rooms fitted to tiles.
        room_ratio - count of rooms. 1 - each tile."""
        # use 11 because upper bound not included in randrange
        rooms_count = math.floor(tiles.__len__() * room_ratio)
        random.shuffle(tiles)
        for i in range(0, rooms_count):
            tile = tiles.pop()
            self.createRoom(tile)
        return

    def createRoom(self, tile):
        """Create room fitted to tile."""
        width = random.randint(3, tile.width)
        height = random.randint(3, tile.height)

        assert((width <= tile.width),
               "room width(%s) should be less or equals tile.width(%s)"
               % (width, tile.width))
        assert((height <= tile.height),
               "room height(%s) should be less or equals tile.height(%s)"
               % (height, tile.height))

        r_x = random.randint(tile.x, tile.x + tile.width - width)
        r_y = random.randint(tile.y, tile.y + tile.height - height)
        for x in range(r_x, r_x + width - 1):
            for y in range(r_y, r_y + height - 1):
                self.points[str(x) + "_" + str(y)] = "."
        # return None

    def draw(self, context):
        """Main draw function, for use with drawing context(IO)."""
        for key in self.points:
            (x, y) = [int(n) for n in key.split("_")]
            x += 1  # hack
            y += 1  # hack
            # assert(x != 0, "x should not be 0")
            # assert(y != 0, "y should not be 0")
            char = self.points[key]
            context.char(char, x, y)

    def connectTiles(self):
        pass  # not ready yet


class Tile():
    def __init__(self, x, y, w=4, h=4):
        self.x = x
        self.y = y
        self.rooms = []
        self.width = w   # minimal for room
        self.height = h  # also


def getMaxDividers(num):
    """Return max dividers of num."""
    devider = 1
    rest = num
    outdev = devider
    while (rest > devider):
        if num % devider == 0:
            rest = num // devider
            outdev = devider
        devider += 1
    return sorted([rest, outdev])
