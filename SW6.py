def temperature(A,B,C):
    if A < B and C < B:
        return "Yes"
    else: return "NO"

def Equlizer(a,b):
    if (a + b) % 2 == 0: return "Yes"
    else: return "NO"

def Five(n):
    temp = n % 10
    if temp == 0 or temp == 5: return "Yes"
    else: return "No"

def Happy(n):
    count = 0
    for i in range(len(n)):
        if n[i] in "aeiou": count += 1
        else: count = 0
        if count > 2: return "Happy"
    return "Sad"

print(temperature(19,28,10))
print(Equlizer(1,2))
print(Five(114))
print(Happy('abcdeeafg'))