def squares(square):
    if square < 1:
        return 1
    else: return 2 * (square - 1) + squares(square - 1)

print(squares(1))

messag = "i am+abdullah]atra"

def encode(message, key):
    new = ""
    for i in message:
        if i.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if key > 26: key = key % 26
            temp = ord(i.upper()) + key
            if temp > 90: temp = temp - 26
            new += chr(temp)
        else: 
            new += i
    return new

def decode(message, key):
    new = ""
    for i in message:
        if i.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if key > 26: key = key % 26
            temp = ord(i.upper()) - key
            if temp < 65: temp = temp + 26
            new += chr(temp)
        else: 
            new += i
    return new
a = encode(messag, 36)
print(a)
print(decode(a, 36))
