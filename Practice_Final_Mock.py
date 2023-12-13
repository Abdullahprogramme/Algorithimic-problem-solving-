# def square(n):
#     i = 0
#     helper(n, i)

# def helper(n, i):
#     if i == 0: 
#         print('*' * n)
#         helper(n, i + 1)
#     elif i == n - 1:
#         print('*' * n)
#     else:
#         print('*' + (i - 1) * "^" + '*' + (n -2 - i) * "^" + '*')
#         helper(n, i + 1)
# square(5)

# def calculateTotalEidi(N):
#     length = len(N)
#     return help(0, N, length)

# def help(i, N, length):
#     sum = 0
#     if i == length:
#         return 0
#     if type(N[i]) is int:
#         sum += N[i] 
#     elif type(N[i]) is list:
#         sum += help(0, N[i], len(N[i]))
#     sum += help(i + 1, N, length)
#     return sum
# print(calculateTotalEidi([500, 100, 750, [ 850, [[200, 200, [[700, 100]], 400]]]]))

# def MinMax(N):
#     if len(N) is 1: return (N[0], N[-1])
#     a, b = MinMax(N[1:])
#     if N[0] < a:
#         a = N[0]
#     if N[0] > b:
#         b = N[0]
#     return a, b
# print(MinMax([1]))

# def Dot(A, B):
#     if len(A) is 0: return 0
#     return A[0] * B[0] + Dot(A[1:], B[1:])
# print(Dot([0, -3, 6], [4, 9, 1]))

# def spiral(N):
#     n = len(N)
#     lengths = []
#     for i in range(1, n): lengths += [i, i]
#     lengths.append(n - 1)
#     row = col = n // 2
#     spiral = [N[row][col]]
#     direction = 0
#     for length in lengths:
#         for _ in range(length):
#             if direction == 0: row -= 1
#             elif direction == 1: col += 1
#             elif direction == 2: row += 1
#             else: col -= 1
#             spiral.append(N[row][col])
#         direction = (direction + 1) % 4
#     return spiral

# print(spiral([[1, 2, 3], \
#             [4, 5, 6],\
#             [7, 8, 9]]))

# def num_toppings(toppings, B):
#     prices = list(toppings.values())
#     length = len(toppings)
#     t = 0
#     for x in range(length):
#         for y in range(x + 1, length):
#             for z in range(y + 1, length):
#                 if prices[x] + prices[y] + prices[z] <= B: t += 1
#     return t
# print(num_toppings({'a': 250, 'b': 350, 'c': 150, 'd': 200, 'e': 300}, 700))

# def num_n_toppings(prices, B, n):
#     if n > len(prices): return 0
#     elif n is 0: return 1
#     num = 0
#     for i in range(len(prices)):
#         if prices[i] <= B: num += num_n_toppings(prices[i+1: ], B - prices[i], n - 1)
#     return num

# print(num_n_toppings([250, 350, 150, 200, 300], 700, 3))

# def print_plus_and_equals(size):
#     a = int(size // 2)
#     result = ''
#     for i in range(2):
#         result += (a - 1) * ' ' + "**" + '\n'
#     for i in range(2):
#         result += '*' * size +'\n'
#     for i in range(2):
#         result += (a - 1) * ' ' + "**" + '\n'
#     result += '\n' + '*' * size + '\n' * 3 + '*' * size
#     return result

# print(print_plus_and_equals(4))

# def level_up(start, multi, bonus, level):
#     if level == 1: return start
#     else: return level_up(start, multi, bonus, level - 1) * multi + bonus

# print(level_up(2, 3, 5, 6))

# def partition_modulo(n, nums):
#     a = {}
#     if n >= 0:
#         for i in range(n): a[i] = []
#     else:
#         for i in range(n + 1, 1): a[i] = []
#     for j in nums:
#         a[j % n].append(j)
#     return a

# print(partition_modulo(-4, [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))

# def friends_shares(no_of_packs, no_of_friends):
#     dollar = no_of_packs * 1.5 / (no_of_friends + 1)
#     cents = no_of_packs * 1.5 // (no_of_friends + 1)
#     print(f"Each friend spends {int(cents)} dollar and {int((dollar - cents) * 100)} cents")

# friends_shares(99, 10)

# def holidays(n):
#     t = 8
#     for i in range(n):
#         a = int(input('> '))
#         if a not in (6, 7, 13, 14, 20, 21, 27, 28): t += 1
#     return t

# print(holidays(2))

# def Pressure(n, k):
#     n = (n + k) % 4
#     if n == 0: return 'OFF'
#     elif n == 1: return 'LOW'
#     elif n == 2: return 'MEDIUM'
#     else: return 'HIGH'

# print(Pressure(0, 11))

# def echo(n):
#     for i in range(len(n), -1, -1):
#         print(n[:i])
#     for i in range(0, len(n) + 1):
#         print(n[:i])
# echo('ECHO')

# def pyramid(n):
#     call(0, n)
    
# def call(i, n):
#     for j in range(n):
#         print(' ' * (n - i - 1) + '* ' * (i+1))
#         i += 1
# pyramid(5)

# def pattern(n):
#     for i in range(n):
#         for j in range(i + 1):
#             print(2**j, end="")
#         for j in range(i - 1, -1, -1):
#             print(2**j, end="")
#         print()
# pattern(3)

# def stars(n):
#     caller(0, n)

# def caller(i, n):
#     for j in range(n):
#         print(' ' * (n - i - 1) + '*' * (i + 1))
#         i += 1
# stars(4)

# def tomorrow(a, b, c):
#     if c == 31:
#         c = 1
#         b += 1
#     else: c += 1
#     if b >= 12:
#         b = 1
#         a += 1
#     print(f"{a}-{b}-{c}")
# tomorrow(2023, 10, 18)

def divide_by_3(A, B):
    count = 0
    if A % 3 == 0 or B % 3 == 0: return 0
    elif A == B: return 1
    while A % 3 != 0 and B % 3 != 0:
        diff = abs(A - B)
        if A > B: 
            A = diff
            count += 1
        elif B > A: 
            count += 1
            B = diff
        else: return count
    return count
print(divide_by_3(2,7))

def round(grade):
    if grade > 33:
        diff = grade % 10
        if 10 - diff < 5: grade = grade - diff + 10
    return grade
print(round(75))

def collatz(n):
    result = str(n)
    while n not in (1, 5 ,17):
        if n % 2 == 0: n = n // 2
        else: n = 3*n - 1
        result += ', ' + str(n)
    return result
print(collatz(3))
