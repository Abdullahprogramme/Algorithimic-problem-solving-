# total = 0
# count = 0
# n = 2
# for i in range(n):
#     count += 1
#     for j in range(count):
#         total += 3
# print(total)

# sum = 0
# pro = 1
# n = 0
# for i in range(n + 1):
#     if i % 2 != 0:
#         num = i
#         for count in range(4):
#             pro = num * count
#             sum += pro
#         pro = 1
# print(sum)

# n = 4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# N = 7
# for i in range(N, 0, -1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

m = 4
n = 3
s = 8
t = 13
a = 6
b = 18
Apple = Orange = 0
for i in range(m):
    num = int(input("Enter a number: "))
    number = a + num
    if number >= s and number <= t:
        Apple += 1
for i in range(n):
    num = int(input("Enter a number: "))
    number = b + num
    if number >= s and number <= t:
        Orange += 1
print(Apple, " ", Orange)

