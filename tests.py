import data

w = 8
h = 5
s = 5 # space
m = data.Map(20,20)
rc_row = 80 // (w+s)
rc_col = 25 // (h+s) 
print(rc_col, rc_row)
for i in range(0, rc_col):
    m.addRoom(data.Room(1, 1+h*i+s*i, w, h))
    for i in range(0, rc_row):
        m.addRoom(data.Room(1+w*i+s*i, 1, w, h))
m.printMap()
print()
