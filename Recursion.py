def Rec_hat(N, i = 0):
    if i < N:
        Rec_hat_support(N, i)
        print()
        Rec_hat(N, i + 1)
def Rec_hat_support(N, i, s = 0):
    if s == 0:
        print(" " * i, end="")
        Rec_hat_support(N, i, s + 1)
    elif s != N + 1 - i:
        print("*", end=" ")
        Rec_hat_support(N, i, s + 1)

def multiplication_Table(N, k):
    if k > 0:
        multiplication_Table(N, k - 1)
        print(N, "*", k , "=", N * k)

def Triangle(N):
    def RightTri(N):
        if N > 0:
            print(N * "*")
            RightTri(N - 1)

    def Reverse_RightTri(N):
        if N != 0:
            Reverse_RightTri(N - 1)
            print(N * "*")
    RightTri(N)
    Reverse_RightTri(N)

def Diamond(N):
    def Diamond_RightTri(N, i = 0):
        if N > 0:
            print(N * "*" + (i * 2) * " " + N * "*" )
            Diamond_RightTri(N - 1, i + 1)

    def Diamond_Reverse_RightTri(N, i = 0):
        if N != 0:
            Diamond_Reverse_RightTri(N - 1, i + 1)
            print(N * "*" + (i * 2) * " " + N * "*")
    Diamond_RightTri(4)
    Diamond_Reverse_RightTri(4)

def binary_search(lst, start, end, val):
    mid = (start + end) // 2
    if lst[mid] == val: return mid
    elif lst[mid] > val: return binary_search(lst, start, mid - 1, val)
    elif lst[mid] < val: return binary_search(lst, mid + 1, end, val)

def main():
    Rec_hat(4)
    multiplication_Table(5, 10)
    Triangle(4)
    Diamond(4)
    print("Found at: ", binary_search([1,2,3,4,5,6,7,8,9,10], 0, 9, 3))
    
if __name__ == "__main__":
    main()