t = (1,2,3,4)
*a, b, c = t
print(a,b,c)
print(tuple("Finally week 15"))
t = (1,2,3,4,5)
print(t[-1:0:-1])
def u():
    return 1, 2
a = u()
print(a)

def printall(*args):
    print(args)
printall(1, 2.0, "Hello")

def pri(string):
    lst = []
    for i in string:
        if (i, string.count(i)) not in lst:
            lst.append((i, string.count(i)))
    lst.sort(key=lambda x:(x[1], x[0]))
    print(lst)
pri("ewwww")

def order(l):
    # lst = []
    # for tpl in l:
    #     lst.append(tpl[-1::-1])
    # return lst
    return [tpl[-1::-1] for tpl in l]

print(order([("C", "B", "A"), ("A", "C", "A"),]))
import math
def distance(p1, p2, p3):
    distance1 = math.sqrt( math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))
    distance2 = math.sqrt( math.pow(p1[0] - p3[0], 2) + math.pow(p1[1] - p3[1], 2))
    if distance1 > distance2: return 3
    elif distance2 > distance1: return 2
    else: return -1
print(distance((1,1), (1,7), (5,6)))

def savemoney(x, y):
    lst = []
    dollar, cent = x[0], x[1]
    for i in range(7):
        temp = (dollar + y[0], cent + y[1])
        lst.append(temp)
        dollar, cent = dollar + y[0], cent + y[1]
    return lst
print(savemoney( (10, 10), (10, 20) ))

def lineCloud(lines):
    empty = {}
    for tup in lines:
        if tup[0] not in empty.keys():
            empty[tup[0]] = [tup[1]]
        else: empty[tup[0]].append(tup[1])
        if tup[1] not in empty.keys():
            empty[tup[1]] = [tup[0]]
        else: empty[tup[1]].append(tup[0])
    return empty
print(lineCloud([ ((0,0), (1,2)), ((1,2), (2,3)), ((2,3), (3,4)), ((3,4), (0,0)) ]))
