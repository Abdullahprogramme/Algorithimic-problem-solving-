a = 3
b = 2 
c = 10
print(max(a, b, c))
print(min(a, b, c))

for i in range(10):
    print(i -1)

dictionary = {}
lst = [0,1 ,2,3,4,5,6,7,8,9]
for char in lst:
    dictionary[char] = dictionary.get(char, 0) + 1

print(dictionary)
d = 0
while b < 10 or a < 9:
    a += 1
    b += 1
    d += c
    print(d)

N = 3
for i in range(2):
    sum = 0
    for j in range(1,N+1):
        sum += j
    N = sum
print(sum)

def share(pack, f):
    cost = (pack *1.5) / (f+1)
    costs = (pack *1.5) // (f+1)
    cents = cost - costs
    print("each frind receivs ", int(costs), "dollars and ", int(cents*100), "cents")
share(4,2)