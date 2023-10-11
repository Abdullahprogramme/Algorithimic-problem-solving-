def Candies(N):
    if N % 2 == 0: print("Yes")
    else: print("No")

def Football(A,B,C,D):
    if A <= C and B <= D: print('Possible')
    else: print('Impossible')

def rook(x1,y1,x2,y2):
    if x1 == x2 or y1 == y2: print('Yes')
    else: print('No')

def Time(h,m):
    total = h * 60 + m
    total = int(total * 11/720) + 1
    print(total)


Candies(4)
Football(3,4,2,6)
rook(1,1,8,8)
Time(8,22)