def calculate_percentage(grades):
    sums, total = 0, len(grades) * 100
    for number in grades:
        sums += number
    return round((sums / total * 100), 1)

print(calculate_percentage([92,91,100,37,86,43,59]))

def get_distinct_items(cart):
    newList = []
    for letter in cart:
        if letter not in newList:
            newList.append(letter)
    return newList

print(get_distinct_items(['b', 'a', 'b', 'c', 'd', 'a', 'e']))

def cyclic_shuffle(cards, X):
    if X > len(cards): X = X % len(cards)
    for i in range(X):
        stored = cards.pop(0)
        cards.append(stored)
    return cards

print(cyclic_shuffle([2,9,4], 7))

def prime_factorization(N):
    lst = []
    while N > 1:
        number = 2
        while N % number != 0:
            number += 1
        lst.append(number)
        N = N / number
    return lst

print(prime_factorization(1430))

def get_repeatedItems(cart):
    repeated_items = []
    for item in range(len(cart)):
        if cart[item] in cart[item+1:] and cart[item] not in repeated_items:
            repeated_items.append(cart[item])
    return repeated_items

print(get_repeatedItems(['b','a','b','c''d','a','e']))