def square(n):
    i = 0
    helper(n, i)

def helper(n, i):
    if i == 0: 
        print('*' * n)
        helper(n, i + 1)
    elif i == n - 1:
        print('*' * n)
    else:
        print('*' + (i - 1) * "^" + '*' + (n -2 - i) * "^" + '*')
        helper(n, i + 1)
square(5)

def calculateTotalEidi(N):
    length = len(N)
    return help(0, N, length)

def help(i, N, length):
    sum = 0
    if i == length:
        return 0
    if type(N[i]) is int:
        sum += N[i] 
    elif type(N[i]) is list:
        sum += help(0, N[i], len(N[i]))
    sum += help(i + 1, N, length)
    return sum
print(calculateTotalEidi([500, 100, 750, [ 850, [[200, 200, [[700, 100]], 400]]]]))

def MinMax(N):
    if len(N) is 1: return (N[0], N[-1])
    a, b = MinMax(N[1:])
    if N[0] < a:
        a = N[0]
    if N[0] > b:
        b = N[0]
    return a, b
print(MinMax([1]))

def Dot(A, B):
    if len(A) is 0: return 0
    return A[0] * B[0] + Dot(A[1:], B[1:])
print(Dot([0, -3, 6], [4, 9, 1]))

