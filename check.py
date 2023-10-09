import re
s = "partypartypart"
s = s.replace("party", "pawri")
print(s)
s = "ab9[cd]2[ef]g"
message = ""
flag = True
num = ""
temp = ""
for i in s:
    if i in "0123456789":
        num = num + i
    elif i in "abcdefghijklmnopqrstuvwxyz":
        temp = temp + i
    elif i == "[":
        flag = True
    elif i == "]":
        flag = False
    if num !="" and flag is False:
        mess = temp * int(num)
        message = message + mess
        num = ""
        flag = True
        mess = ""
        temp = ""
    elif num == "" and flag is True: 
        message = message + temp
        temp = ""
print(message)

# global sum 
# def func(D,N):
#     sum = 0
#     for i in range(D):
#         for j in range(1,N + 1):
#             sum += j
#         if i != 0:
#             sum -= N
#         N = sum
#     return sum
# x = func(2,6)
# print(x)

# S = "09083"
# if "0" not in S:
#     print("FALSE")
# else:
#     print("TRUE")

a = 1
b = 10
for i in range(a, b + 1):
    count = 0
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1
    if count == 1:
        print(i)


s = "I am 1 8 Abdullah Tariq!@gmail.com"
item = (s[9:-17]).lower() + '@' + re.findall('@([^ ]*)', s)[0]
print(item)


# for x in range(len(s)):
#     for y in range(len(s)):
#         for z in range(len(s)):
#             if s[x] == s[y] or s[x] == s[z] or s[y] == s[z]:
#                 pass
#             else: print(s[x] + s[y] + s[z])

