n = int(input())
mat = []
count = 0
try:
    while True:
        try:
            s = list(map(int, input().split(' ')))
            mat.append(s)
        except:
            break
except:
    pass
print(mat)
for i in range(n):
    for j,e  in enumerate(mat[i]):
        if j%2 == 0 and mat[i][j] == mat[i][j+2] :
            for m in range(n):
                mat[m][j] = 'm'
        if j % 2 == 1 and mat[i][j] == mat[i][j + 2]:
            for m in range(n):
                mat[m][j] = 'm'