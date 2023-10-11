def un_Camel(n):
    count = 1
    for i in n:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count += 1
    return count

def can_win(n):
    if len(n) % 2 != 0: return "No"
    else:    
        for i in n:
            count = n.count(i)
            if count % 2 != 0: return "No"
        return "Yes"
    
print(un_Camel('oneTwoThreeFour'))
print(can_win("cbcba"))