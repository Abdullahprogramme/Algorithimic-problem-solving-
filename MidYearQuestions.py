# finds the last word and it's length and outputs both
sum = 0
def sums(lst, i):
    global sum
    if len(lst) == 0: print("NO value")
    elif len(lst) == 1: print(lst[0])
    else: 
        if i < len(lst):
            sum += lst[i]
            sums(lst, i + 1)
        else: print(sum)

def pattern(n):
    if n > 0:
        print('*' * n)
        pattern(n - 1)

def Last_word(n):
    flag = True
    count = 0
    word = ''
    for i in range(-1,-len(n),-1):
        if n[i] != ' 'and flag is True:
            count += 1
            word = n[i] + word
        else: flag = False
    print("The last word is '" + word + "' with length " + str(count) )

# takes n as input until @ entered and finds the square of it
def fact(n):
    pro = 1
    for i in range(1, n + 1):
        pro *= i
    return pro
def Fixfact():
    n = input("Enter a number: ")
    while n != '@':
        N = n
        n = input("Enter a number: ")
    factorial = fact(int(N))
    print(factorial)

# makes a geometric series where a is the starting number , b is the ratio and c is the limit of the numbers produced in the series
def series(a,b,c):
    print(a , end="")
    while c > 1:
        a = a * b
        print("," + str(a), end="")
        c -= 1
    print(".")

# finds the product of the numbers in the odd places 
def odd_numbers(n):
    product = 1
    for i in range(len(n)):
        if i % 2 == 0:
            product *= int(n[i])
    print(product)

# shifts the number from the left side to right side concatinating them to (shift) places
def shift_num(n,shift):
    new =''
    if shift > len(n): new= reversed(n)
    else: new = n[shift:len(n)] + n[:shift]
    print(new)

def productExceptSelf(nums):
        answer = [0] * len(nums)
        for i in range(len(nums)):
            answer[i] = product(nums, nums[i])
        return answer

def product(array, j):
    products = 1
    #array.remove(j)
    for k in range(len(array)):
        if array[k] != j:
            products *= array[k]
    return products

def multiplication_table(n, k):
    if k != 0:
        multiplication_table(n, k - 1)
        print(str(n) + " * " + str(k) + " =" , n * k)
        


def main():
    sums([5,7,2,3], 0)
    pattern(7)
    multiplication_table(5, 10)
    print(productExceptSelf([-1,1,0,-3,3]))
    Last_word('My name is Abdullah Tariq')
    Fixfact()
    series(2,2,3)
    odd_numbers('1234')
    shift_num('12345678',4)
    
if __name__ == "__main__":
    main()
    
