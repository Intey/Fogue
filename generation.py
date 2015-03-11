# import random
# from data import Room, Item, Map

"""For what the fuck it's needs. In commonly, for creation. After this,
we just create map, and start to draw it in loop and change. Thats all. All
objects, generator - not needs.
Maybe in future, when we want something like this 'bless you the gift of vision
through walls (show nearest rooms)' and we needs to detect where is nearest
rooms, and display them. In future we can use traps, teleports, secret
rooms that can be build on the fly or conversely, remove rooms, or that halfs.
Exesting objects simplify that calculations, and searchs.
So, it needs. Nuff said."""

"""Common idea - Graphs.
Create rooms as graph vertex. Then, randomly connect several of those
(fill adjacency matrix). If we have more than one component - connect them.
Then get each room, and put items to it. Dungeon ready.
Also, praphs have algoriths for found longest way, in other words farthers
node from current - use it in creation of downstairs."""


class DungeonGenerator():
    """ Create simple dungeon. It's have a little bit of rooms,
    little bit of items and naturally, monsters. """
    def __init__(self, roomsCount=0, itemsCount=0, monstersCount=0):
        self.roomsCount = roomsCount
        self.itemsCount = itemsCount
        self.monstersCount = monstersCount

    def generateDungeon(self):
        """ Generation function. use values of counts in initialization.
        Should return Dungeon object that countains Rooms, Items, Monsters.
        And Hero, of course."""
        pass  # return Dungeon

    def generateRooms(self):
        """ Create rooms.
        Used for contains Items, Hero, Monsters, etc.
        Should return list of Rooms objects,
        that used for contains in World. """
        pass  # return Rooms[]

    def generateConnections(self):
        """Define connections between Rooms. They used for determine which
        rooms connected. """
        pass

    def connectRects(self, src, dest):
        """ generate connection of src and dest rects.
        Return list of lists of points that represent corridor.
        With that we can save data 'bout "occupancy" of map. And found
        "black holes" in map."""
        pass  # return []


def getMaxDividers(num):
    """Return max dividers of num. Used for split map in defined count tiles.
    for 4 : 2,2; 6 - 3,2; 7 - 1,7; 8 - 4,2; 12 - 3,4; etc."""
    devider = 1
    rest = num
    outdev = devider
    while (rest > devider):
        if num % devider == 0:
            rest = num // devider
            outdev = devider
        devider += 1
    return sorted([rest, outdev])
