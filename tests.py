import gameio
import data

out = gameio.Output()
inp = gameio.Input()

out.page()

( w, h ) = out.size()
while 1:
    out.clear()
    map = data.Map( w, h ) # auto generate rooms and corrs on __init___
    map.draw( out )
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
