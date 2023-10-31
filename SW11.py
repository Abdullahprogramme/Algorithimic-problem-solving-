def leftovers(N, M):
    if N < M: return N
    else: return leftovers(N - M, M)

print(leftovers(12,15))

def SheepProd(N):
    if N == 0: return 0
    elif N % 2 == 0: return 0.25 + SheepProd(N - 1)
    else: return 0.5 + SheepProd(N - 1)

print(SheepProd(4))

def TriangleNum(N):
    if N == 1: return 1
    else: return N + TriangleNum(N - 1)

print(TriangleNum(11))

def facht(N):
    if N == 1: return 1
    else: return (N - 1) * facht(N - 1)

print(facht(5))

def facht2(A):
    if A == 0: return 0
    else: return A % 10 + facht2(A // 10)

print(facht2(6))