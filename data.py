# import gameio
import random


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
class Map():
    def __init__(self, width, height):
        self.points = [["#" for _ in range(0, 80)] for _ in range(0, 25)]
        self.rooms = []
        self.corridors = []
        self.tiles = [[x for x in range(1, 8)] for y in range(1,5)]


    def createTiles(self):
        self.tiles = []
        
        
        
    def mkVertCorridor(self, x, start_y, end_y):
        for y in range(start_y, end_y):
            self.points[y][x] = "."


    def mkHoriCorridor(self, start_x, y, end_x):
        for x in range(start_x, end_x):
            self.points[y][x] = "."


    
    def mkCornCorridor(self, x, y, width, height, corner="LU"):
        if corner == "LU":
            self.mkVertCorridor(x, y, y+height)
            self.mkHoriCorridor(x, y, x+width)
        if corner == "LB":
            self.mkVertCorridor(x+width-1, y, y+height)
            self.mkHoriCorridor(x, y+height-1, x+width)
        if corner == "RU":
            self.mkVertCorridor(x+width-1, y, y+height)
            self.mkHoriCorridor(x, y+height-1, x+width)
        if corner == "RB":
            self.mkVertCorridor(x+width-1, y, y+height)
            self.mkHoriCorridor(x, y+height-1, x+width)


    def addRoom(self, room):
        self.rooms.append(room)
        for x in range(room.x, room.x+room.width):
            for y in range(room.y, room.y+room.height):
                self.points[y][x] = "."


    def printMap(self):
        for row in self.points:
                print("".join(y for y in row))


    def draw(self, context):
        for r in self.rooms:
            r.draw(context)
        for crd in self.corridors:
            crd.draw(context)
