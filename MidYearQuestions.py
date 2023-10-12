# finds the last word and it's length and outputs both
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
def Fixfact():
    n = input("Enter a number: ")
    while n != '@':
        N = n
        n = input("Enter a number: ")
    square = int(N) ** 2
    print(square)

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

Last_word('My name is Abdullah Tariq')
Fixfact()
series(2,2,3)
odd_numbers('1234')
shift_num('12345678',4)