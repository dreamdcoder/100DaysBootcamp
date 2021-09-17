row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1, row2, row3]

for i in range(len(map)):
    print(*map[i])

position= input("Enter 2D Co-ordinates in digit form without space or ','" )

col = int(position[0])-1
row = int(position[1])-1

try:
    map[row][col] = ' X'
    for i in range(len(map)):
        print(*map[i])
except BaseException as e:
    print(e)
