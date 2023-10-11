def Ali(N):
    c = 0
    for i in range(2,N):
        if N % i == 0: c += 1
        if c > 0: return False
    return True

def Reverse(N):
    new = ""
    while N > 0:
        a = N % 10
        N = N // 10
        new = new + str(a)
    print(new)

print(Ali(3))
Reverse(33602)