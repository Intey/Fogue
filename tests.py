import generation
import io

def printRoom(room):
    for row in room:
        print("".join([e for e in row]))

room = (generation.createRoom(8, 6))
printRoom(room)
print()

mp = generation.Map(20, 20)
mp.addRoom(generation.Room(4, 4, 8, 8))
mp.addRoom(generation.Room(10, 10, 15, 18))

generation.printTiles(mp)

io = Output
room.draw(io)
