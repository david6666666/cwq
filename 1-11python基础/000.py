while True:
    try:
        n = int(input())
        c1 = [sum(range(i)) for i in range(1, n+2)]
        print(c1)
        c2 = [i+1 for i in c1]
        print(c2)
        for j in range(n):
            c2 = [i-1 for i in c2[1:]]
            print(c2)
            print(' '.join(map(str, c2)))
    except:
        break

