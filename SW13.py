def Bill(X):
    sums = 0
    for i in X:
        sums += i[1]
    return sums
print(Bill([["S", 109], ["A", 125], ['sd', 45], ['sd', 270]]))

def matrixSubtraction(A, B):
    if len(A) != len(B):
        return -1
    else:
        new = [[] for i in range(len(B))]
        for i in range(len(A)):
            for j in range(len(A[i])):
                new[i].append(A[i][j] - B[i][j])
        return new
print(matrixSubtraction([[2,1], [8,6], [4,9]], [[1,1], [5,6], [2,7]]))

def when_and_what(X, N):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for i in range(len(N)):
        n = N[i]
        for j in range(len(n)):
            if X == N[i][j]:
                return i + 1, days[j] 
    return -1   
print(when_and_what("cake", [["banana", "cake"], ['per', 'sd']]))

def calculateTotalEidi(N):
    sum = 0
    for i in N:
        if type(i) is list:
            sum += calculateTotalEidi(i)
        else:
            sum += i
    return sum
print(calculateTotalEidi([500, 100, 750, [ 850, [[200, 200, [[700, 100]], 400]]]]))

def print_nested_list(A):
    for nested in range(len(A)):
        for element in range(len(A[nested])):
            print(A[nested][element], end=" ")
        print()

print_nested_list([[2,3], [4,5], [5,6,7]])
