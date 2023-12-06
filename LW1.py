def Chairs(X,Y):
    if X >= Y: print(X-Y)
    else: print(0) 

def MinMoves(x,y,X,Y):
    count = 0
    while x != X and y != Y:
        x += 1
        y += 1
        count += 1
    if x == X:
        count += Y - y
    elif y == Y:
        count += X - x
    return count

def Shoes(N,M):
    count = N
    if N >= M:
        while N != M:
            M += 1
            count += 1
    print(count)

def Pattern(N):
    count = 0
    a = 1
    for i in range(N):
        for j in range(a):
            count += 1
        a = a + count
    print(count)


Chairs(12,12)
print(MinMoves(2,3,9,9))
Shoes(8,8)
Pattern(4)
