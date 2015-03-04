import io
import random

# like interface
class Drawable:
    def draw(self, context):
        pass #nothing doing there.
    
    
class Item(Drawable):
    def __init__(self, x, y):
        self.name="unknown"
        self.x = x
        self.y = y
        self.color = io.BLACK
    def draw(self, context):
        context.char(self.x, self.y, self.color)


class Room(Drawable):
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


class Map:
    def __init__(self, width, height):
        self.tiles = [["#" for _ in range(0, width)] for _ in range(0, height)]
        self.rooms = []

    def mkVertCorridor(self, x, top, bottom):
        for y in range(top, bottom):
            self.tiles[y][x] = "."

    def addRoom(self, room):
        self.rooms.append(room)
        for x in range(room.x, room.width):
            for y in range(room.y, room.height):
                self.tiles[y][x] = "."