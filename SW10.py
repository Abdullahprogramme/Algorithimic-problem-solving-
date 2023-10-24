def numbers(n):
    if n <= 0: print(0)
    else:
        numbers(n - 1)
        print(n)

def stars_pattern(n):
    if n > 0:
        stars_pattern(n - 1)
        print('*' * n)

def anotherStars_pattern(n):
    if n <= 0:
        pass
    else: 
        anotherStars_pattern(n - 1)
        print("*" * n)
    
def countOdd(n):
    if n == 0:
        pass
    elif n % 2 != 0:
        print(n)
        countOdd(n - 1)
    else: countOdd(n - 1)


def main():
    numbers(5)
    stars_pattern(5)
    anotherStars_pattern(5)
    countOdd(9)
if __name__ == "__main__":
    main()