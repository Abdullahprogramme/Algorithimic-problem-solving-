def tax(s,x,y):
    xC = yC = 0
    for i in range(len(s) - 1):
        if s[i] == "0" and s[i + 1] == "1":
            xC += 1
        elif s[i] == "1" and s[i + 1] == "0":
            yC += 1
    return ( xC * x + yC * y)
    
def taxChange(s,x,y):
    xC = yC = 0
    for i in s:
        if i == "0": xC += 1
        elif i == "1": yC += 1
    if x > y: s = yC * "1" + xC * "0"
    else: s = xC * "0" + yC * "1"
    print( tax(s,x,y) )
s= "01010101"
taxChange(s, 4,55)

def tri(n):
    count = sum = 0
    for i in range(n):
        count += 1
        for j in range(count):
            sum += 1
    print(sum)
tri(6)

def pale(n):
    count = 0
    if n == reversed(n):
        return True
    else:
        for i in range(len(n)):
            if n[i] != n[len(n) - i - 1]:
                count += 1
        if count == 2: return True
        else: return False
print(pale('243212'))

flag = False
s= "pizza"
t ="olive"
for i in range(len(t)):
    if s[i] == t[i]:
        print("yes")
        flag = True
    else:
        if i != len(s) - 1:
            if ( s[i] == s[i+1]) and ( t[i] != t[i+1]):
                print("Yes")
                flag = True
if flag is False: print("No")
