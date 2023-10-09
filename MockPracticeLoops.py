
def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

def RightTri(n):
    count = 1
    for i in range(n):
        for j in range(count):
            print("*", end="")
        count += 1
        print()

def print_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars + spaces)

def priint_pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

def Vowels(n):
    count = 0
    for i in n.lower():
        if i in "aeiou":
            count += 1
    print(count)

def Prime(n):
    for i in range(2, n):
        count = 0
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
        if count == 1: print(i)

def SCube(n):
    sum = 0
    for i in range(1, n + 1):
        cube = i ** 3
        sum += cube
    print(sum)

def Diamond(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()
    for i in range(n - 1):
        for j in range(i + 1):
            print(" ", end="")
        for j in range((n - i - 1) * 2 - 1):
            print("*", end="")
        print()

def Rectangle(m, n):
    for i in range(m):
        for j in range(n):
            print("*", end="")
        print()

def Fibonacci(n):
    a = 0
    b = 1
    for i in range(n - 1):
        if i == 0:
            print(a, b, end=" ")
        else: 
            a, b = b , a + b
            print(b, end=" ")
    print()
        
def Chess(n, m):
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                if j % 2 == 0:
                    print("X", end="")
                else: print("O", end="")
            else: 
                if j % 2 != 0:
                    print("X", end="")
                else: print("O", end="")
        print()

def HalfDiamond(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()
    for i in range(n - 1):
        for j in range(n - i - 1):
            print("*", end="")
        print()

def HollowSquare(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            for j in range(n):
                print("*", end="")
            print()
        else:
            space = " " * (n - 2)
            mess = "*" + space + "*"
            print(mess)

# def Alpha(n):
#     for i in range(n):
#         for j in range(n - i - 1):
#             print(" ", end="")
#         for j in range(2 * i + 1):
            


square(4)
RightTri(5)
print_pyramid(4)
priint_pyramid(4)
Vowels("Hello, World!")
Prime(20)
SCube(3)
Diamond(5)
Rectangle(3, 5)
Fibonacci(6)
Chess(5, 5)
HalfDiamond(4)
HollowSquare(5)