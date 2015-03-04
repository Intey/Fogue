import random


class Room:
    def __init__(self, x, y, w, h):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        
    def draw(context):
        for x in range(x, width):
            for y in range(y, height):
                context.char(x, y, ".")
        # creature.draw( context ) for creature in creatures !!!
        # return
        
    def getConnection(self, room):
        """Connect 2 rooms by nearest path.
        TODO: Determine nearest sides: check horizontal check vertical.

        """
        for x in range(room.x, room.width):
            print("in xs %s search room x:%s" % (range(self.x, self.width), x))
            if range(self.x, self.width).__contains__(x):
                print("overlap on x")
                corrX = random.randint(x, self.width)
                return corrX
                # return corrX, max(self.y, room.y), min(self.y + self.height, room.y + room.height)

        print()
        for y in range(room.y, room.height):
            print("in ys %s search room y:%s" % (range(self.x, self.width), y))
            if range(self.y, self.height).__contains__(y):
                print("overlap on y")
                print("random position for corridor: %s" % (random.randint(y, self.height)))
                return


class Map:
    def __init__(self, width, height):
        self.tiles = [["#" for x in range(0, width)] for y in range(0, height)]
        self.rooms = []

    def mkVertCorridor(self, x, top, bottom):
        for y in range(top, bottom):
            self.tiles[y][x] = "."

    def addRoom(self, room):
        self.rooms.append(room)
        for x in range(room.x, room.width):
            for y in range(room.y, room.height):
                self.tiles[y][x] = "."


def printTiles(m):
    global row, y
    for row in m.tiles:
        print("".join(y for y in row))


def roomConnecting():
    global r1, r2
    r1 = Room(1, 1, 10, 10)
    r2 = Room(5, 5, 9, 9)
    r1.getConnection(r2)
    r2 = Room(0, 0, 3, 10)
    r1 = Room(5, 5, 10, 10)
    r1.getConnection(r2)


