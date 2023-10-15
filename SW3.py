def air(a,b,c,d,e):
    if a+b > d or a+c > d or b+c > d or a > e or b > e or c > e: return "No"
    else: return "Yes"

def cricket(r1,r2,c1,c2,w1,w2):
    Bcount = Acount = 0
    if r1 > r2: Acount+= 1
    else: Bcount+=1
    if c1 > c2: Acount+=1
    else: Bcount+=1
    if w1 > w2: Acount+=1
    else: Bcount+=1
    if Acount > Bcount: return "A"
    else: return "B"

def Mood(a,b,c):
    maxed = min(a,b,c)
    if maxed == a: return b + c
    elif maxed == b: return a + c
    else : return a + c

def Forest(k):
    a = k - k // 2 
    b = k // 2
    return ( 3 * a + (-1 * b) )

def Inherit(x,y):
    total = x *1 + y *2
    if total % 2 == 0: return "Inherit"
    else: return "Vigo"

def Gold(n,x,y):
    if (n+1) * y >= x: return "Yes"
    else: return "No"


print(air(10,10,10,20,10))
print(cricket(0,1,2,2,3,4))
print(Mood(4,2,8))
print(Forest(4))
print(Inherit(5,7))
print(Gold(2,10,4))