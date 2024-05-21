'''
1. Build bingo map
2. Erase 
3. Check if bingo using for sentences
    row, col, diagonal
'''

def find_bmap(a):
    for row in range(5):
        if bmap[row].count(a):
            bmap[row][bmap[row].index(a)] = 0
            break

def check():
    bingo = 0
    # row
    for row in range(5):
        if bmap[row].count(0) == 5:
            bingo += 1
            if bingo == 3:
                return 1
    # col
    for col in range(5):
        sum_col = 0
        for row in range(5):
            sum_col += bmap[row][col]
        if sum_col == 0:
            bingo += 1
            if bingo == 3:
                return 1
    # diagonal
    sum_dia = 0
    for dia in range(5): # 1
        sum_dia += bmap[dia][dia]
    if sum_dia == 0:
        bingo += 1
        if bingo == 3:
            return 1
    sum_dia = 0
    for dia in range(5): # 2
        sum_dia += bmap[4-dia][dia]
    if sum_dia == 0:
        bingo += 1
        if bingo == 3:
            return 1


bmap = list(list(map(int, input().split())) for _ in range(5))
call = list(list(map(int, input().split())) for _ in range(5))

cnt = 0
flag = False
for i in range(5):
    for j in range(5):
        find_bmap(call[i][j]) # Erase to 0
        cnt += 1
        if check(): # Check if row, col, diagonal
            print(cnt)
            flag = True
            break
    if flag == True:
        break