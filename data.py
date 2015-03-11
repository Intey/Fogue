# import gameio
import random
import math


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


