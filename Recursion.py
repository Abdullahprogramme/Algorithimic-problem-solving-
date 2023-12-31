def Rec_hat(N, i = 0):
    if i < N: # recursive case
        Rec_hat_support(N, i)
        print()
        Rec_hat(N, i + 1)
def Rec_hat_support(N, i, s = 0):
    if s == 0: # recursive case
        print(" " * i, end="")
        Rec_hat_support(N, i, s + 1)
    elif s != N + 1 - i: # recursive case
        print("*", end=" ")
        Rec_hat_support(N, i, s + 1)

def multiplication_Table(N, k):
    if k > 0: # recursive case
        multiplication_Table(N, k - 1)
        print(N, "*", k , "=", N * k)

def Triangle(N):
    def RightTri(N):
        if N > 0: # recursive case
            print(N * "*")
            RightTri(N - 1)

    def Reverse_RightTri(N):
        if N != 0: # recursive case
            Reverse_RightTri(N - 1)
            print(N * "*")
    RightTri(N)
    Reverse_RightTri(N)

def Diamond(N):
    def Diamond_RightTri(N, i = 0):
        if N > 0:
            print(N * "*" + (i * 2) * " " + N * "*" )
            Diamond_RightTri(N - 1, i + 1) # recursive case

    def Diamond_Reverse_RightTri(N, i = 0):
        if N != 0:
            Diamond_Reverse_RightTri(N - 1, i + 1) # recursive case
            print(N * "*" + (i * 2) * " " + N * "*")
    Diamond_RightTri(4)
    Diamond_Reverse_RightTri(4)

def Factorial(n):
    if n == 0 or n == 1: return 1 # base case
    else: return n * Factorial(n - 1) # recursive case

def binary_search(lst, start, end, val):
    mid = (start + end) // 2
    if lst[mid] == val: return mid # base case
    elif lst[mid] > val: return binary_search(lst, start, mid - 1, val) # recursive case
    elif lst[mid] < val: return binary_search(lst, mid + 1, end, val) # recursive case

def GCD(a, b):
    if b == 0: return a # base case
    else: return GCD(b ,a % b) # recursive case

def Palindrome(N):
    if len(N) <= 1: # base case
        return True
    elif N[0] == N[-1]:
        return Palindrome(N[1:-1]) # recursive case
    else: return False # base case

def Reverse(N):
    if len(N) <= 1:
        return N # base case
    else: return N[-1] + Reverse(N[:- 1]) # recursive case

def Sum_of_Natural_Nums(N):
    if N == 1: return 1 # base case
    else: return N + Sum_of_Natural_Nums(N - 1) # recursive case

def Count_digits(N):
    if N < 10:
        return 1 # base case
    else: 
        return 1 + Count_digits(N // 10) # recursive case

def Fibonacci(N):
    if N <= 1: return N # base case
    else: return Fibonacci(N - 1) + Fibonacci(N - 2) # recursive case

def Sum_Of_Digits(N):
    if N < 1: return 0 # base case
    else: return N % 10 + Sum_Of_Digits(N // 10) # recursive case

def PowerCal(base, exponent):
    if exponent < 1: return 1 # base case
    else: return base * PowerCal(base, exponent - 1) # recursive case

def hanoi(n, source, auxiliary, target):
    if n == 1:
        print("Move disk 1 from", source, "to", target) # base case
    else:
        hanoi(n-1, source, target, auxiliary) # recursive case
        print("Move disk", n, "from", source, "to", target)
        hanoi(n-1, auxiliary, source, target) # recursive case

def anotherBigHat(N):
    def anotherHat(n, a = 0):
        if n > 0: # recursive case
            print(" " * a + "* " * n)
            anotherHat(n - 1, a + 1)
    def anotherReverseHat(n, a = 0):
        if n > 0: # recursive case
            anotherReverseHat(n - 1, a + 1)
            print(" " * a + "* " * n)
    anotherHat(N)
    anotherReverseHat(N)

def Count_Vowels(N):
    if len(N) < 1: return 0 # base case
    else: 
        if N[-1].lower() in 'aeiou': # recursive case
            return 1 + Count_Vowels(N[:-1])
        else: return Count_Vowels(N[:-1]) # recursive case

def my_find(s, subs, a = 0):
    if s[:len(subs)] == subs: return a # base case
    else: return my_find(s[1:], subs, a+1) # recursive case

def main():
    # flag = True
    # start = temp = 0
    # s = 'axc'
    # t = 'ahbgdc'
    # if (len(s) >= len(t) and (len(s) != 0 or len(t) != 0)) or len(t) == 0 and len(s) != 0: flag = False
    # while flag is True and temp != len(s):
    #     i = s[temp]
    #     temp += 1
    #     start = t.find(i, start, len(t))
    #     if start == -1:
    #         flag = False
    #         break
    #     start += 1
    # print(flag)
    Rec_hat(4)
    multiplication_Table(5, 10)
    Triangle(4)
    Diamond(4)
    print("Found at: ", binary_search([1,2,3,4,5,6,7,8,9,10], 0, 9, 3))
    print(Factorial(4))
    print(GCD(3,9))
    print(Palindrome("RacecaR"))
    print(Reverse("Abdullah"))
    print(Sum_of_Natural_Nums(6))
    print(Count_digits(123456))
    print(Fibonacci(6))
    print(Sum_Of_Digits(123))
    print(PowerCal(3, 2))
    hanoi(3, 1, 2, 3)
    anotherBigHat(4)
    print(Count_Vowels("AbduLLah"))
    print(my_find('bbbbba', 'a'))
    
if __name__ == "__main__":
    main()
