# import gameio
import random
import math
# like interface
#class Drawable:
#    def draw(self, context):
#        pass #nothing doing there. Just mean, that childs should realize this


class Item():
    def __init__(self, x, y):
        self.name="unknown"
        self.x = x
        self.y = y
        self.color = gameio.BLACK
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
            creature.draw( context )
        for item in self.items:
            item.draw( context )
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
                return corrX, max(self.y, room.y), min(self.y + self.height, room.y + room.height)

        for y in range(room.y, room.height):
            if range(self.y, self.height).__contains__(y):
                corrY = random.randint(y, self.height)
                return corrY, max(self.x, room.x), min(self.x + self.width, room.x + room.widht)


# split map in tiles. Each tile can contains 1+ rooms. 
# Between tiles, we have(withount rooms borders) 1 char spacer for corridors.
# firstly we fill tiles with rooms, then creating connections between tiles.
# For determine which tiles should be connected, we generate random pairs 
# of nums, that points to tiles. Nums should point to neighbors rooms.
#     n # n # n
#     # # # # #
#     n # r # n
#     # # # # #
#     n # n # n
# May use unique pairs list for connections - one pair will connect once.


# Madic numbers

ROOM_WIDTH  = [ 3, 5 ] # const + random
ROOM_HEIGHT = [ 3, 5 ]
CORRIDOR_MIN_SPACE = 3
ROOM_RATIO = 0.8

class Map():
    def __init__(self, width, height):
        self.points = {}
        self.rooms = []
        self.width = width
        self.height = height
        
        
        
        # no need for self, __init__ runtime only
        tiles = self.getTiles( width, height )
        self.fillTiles( tiles )
        # self.connectRooms()
    
    def getTiles(self, screenx, screeny):
        # tile size
        width  = ROOM_WIDTH[0]  + ROOM_WIDTH[1] 
        height = ROOM_HEIGHT[0] + ROOM_HEIGHT[1]
        # print( "Screen size [" + str(screenx) + "," + str(screeny) + "]" )
        # print( "Tile size [" + str(width) + "," + str(height) + "]" )
        # tiles count
        # print( screenx // width )
        
        # there i get devide by  ))
        # 170 % 10 == 0
        #'couze screenx % widht == 0
        cols = screenx // width
        rows = screeny // height
        
        # print( "Tiles count [" + str(rows) + "," + str(cols) + "]" )
        # prepare return
        nums = rows * cols
        unused = []
        for r in range(0, rows):
            for c in range(0, cols):
                unused.append(Tile( c * width, r * height, width, height ))
        return { "nums": nums, "width": width, "height": height, "unused": unused }
    
    def fillTiles( self,tiles ):
        roomsCount = math.floor( tiles[ "nums" ] * ROOM_RATIO )
        random.shuffle( tiles[ "unused" ] )
        for i in range( 0, roomsCount ):
            tile = tiles[ "unused" ].pop()
            self.createRoom( tile )
        return
    
    def fitTiles(self):
        """ calc max tiles that can fit on map"""
        # save it! for dragons! D @ -- gg wp
        # -_- :%s///g - not works there. 
        rows = ROOM_WIDTH[0] + ROOM_WIDTH[1] + CORRIDOR_MIN_SPACE
        cols = ROOM_HEIGHT[0] + ROOM_HEIGHT[1] + CORRIDOR_MIN_SPACE
       
        # равновато ты их в rows пишешь
        
        return rows * cols
        
    def createRoom(self, tile):
        # tile instanceof class Tile
        width  = ROOM_WIDTH[ 0 ]  + random.randint(0, ROOM_WIDTH[ 1 ] )
        height = ROOM_HEIGHT[ 0 ] + random.randint(0, ROOM_HEIGHT[ 1 ] )
        r_x = random.randint(tile.x, tile.x + tile.width  - width)
        r_y = random.randint(tile.y, tile.y + tile.height - height)
        for x in range(r_x, r_x + width - 1):
            for y in range(r_y, r_y + height - 1):
                self.points[ str(x) + "_" +  str(y) ] = "."
        # return None
        
    def printMap(self):
        for row in self.points:
                print("".join(y for y in row))

    def draw(self, context):
        
        for key in self.points:
            ( x, y ) = key.split( "_" )
            char = self.points[ key ]
            x = int(x) + 1
            y = int(y) + 1
            if x is 0 or y is 0:
                print( "PIDAR!!!" )
            context.char( char, x, y )
        # return
            
    def connectTiles(self):
        pass #not ready yet
        for i in tiles.__len__():
            # get neighbor index. Neighbor index is in this tile index + or - 4
            conn_idx = i
            while (conn_idx == i): # without self
                conn_idx = random.randint(tiles[i]-4, tiles[i]+4)
            return conn_idx
            

class Tile():
    def __init__(self, x, y, w=4, h=4):
        self.x = x
        self.y = y
        self.rooms = []
        self.width = w # minimal for room
        self.height = h # also
        self.unused = True