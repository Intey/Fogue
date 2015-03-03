import generation


def printRoom(room):
    for row in room:
        print("".join([e for e in row]))

room = (generation.createRoom(8, 6))
printRoom(room)
