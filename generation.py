def createDungeon(roomsCnt, connections):
    rooms = createRooms(8)
    # get each pair of rooms
    connectRooms(rooms[0], rooms[1])
    # connect pairs of rooms


def createRooms(count):
    rooms = [createRoom() for i in count]
    return rooms


def connectRooms(first, second):
    # determine direction of corridor
    return False


def createRoom(width, height):
    """just return empty room with borders"""
    room = [["." for c in range(width)] for r in range(height)]
    # create border
    for row in range(height):
        if row == 0 or row == height-1:
            room[row] = list(("#" * width))
        else:
            for col in range(width):
                if col == 0 or col == width-1:
                    room[row][col] = "#"
    return room

