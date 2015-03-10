import gameio
import data
import random
# for val in range(2, 64, 1):
#    r, c = data.getMaxDividers(val)
#    print("for num %s rows %s and cols %s" % (val, r, c))
out = gameio.Output()
inp = gameio.Input()
out.__addOne__ = True
out.page()
out.hideCursor()
(w, h) = out.size()
tiles_counts = [4, 6, 9, 12, 15, 16, 18, 24, 32]
while 1:
    out.clear()
    data.YayMap( w, h, out )
    # map = data.Map(w, h, random.choice(tiles_counts))  # auto generate rooms and corrs on __init___
    # map.draw(out)
    ch = inp.char()
    if ch is "escape":
        out.reset()
        break

# out.move( 0, 15 )

# w = 8
# h = 5
# s = 3 # space
# m = data.Map(20,20)
# rc_row = 80 // (w+s)
# rc_col = 25 // (h+s)
# print(rc_col, rc_row)
# for i in range(0, rc_col):
#     m.addRoom(data.Room(3, 2+h*i+s*i, w, h))
#     for i in range(0, rc_row):
#         m.addRoom(data.Room(3+w*i+s*i, 2, w, h))
# m.printMap()
# print()
