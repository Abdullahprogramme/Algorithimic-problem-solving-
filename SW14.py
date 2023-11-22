# dictionary = {}
# for i in range(10):
#     N = int(input())
#     dictionary[N] = dictionary.get(N, 0) + 1
# print(dictionary)

A = {"mixed": [ [1,2,3], {"pi": 3.142, "life": 21} ] }
print(A["mixed"][1]["life"])
d = {"e": 3, "w": 2, "f": 1}
new_d = { v:k for k, v in d.items()}
print(new_d)

counts = {"A": 1, "B": 3, "C": 1}
letters = {}
for k, v in counts.items():
    if v in letters:
        letters[v].append(k)
    else: letters[v] = [k]
print(letters)

def itemFrequency(items):
    counts = {}
    for i in items:
        counts[i] = counts.get(i, 0) + 1
    for key in counts.keys():
        print(key, counts[key])

itemFrequency(["A", "A", "B", "A"])

def popularBirthday(birthdays):
    Month = {1: "January", 2: "February", 3: "March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10: "October", 11: "November", 12:"December"}
    popularMonths = []
    empty = {}
    for dictionary in birthdays:
        empty[Month[dictionary["month"]]] = empty.get(Month[dictionary["month"]], 0) + 1 
    maxVal = max(empty.values())
    popularMonths = [key for key, value in empty.items() if value == maxVal]
    for i in range(len(popularMonths)):
        if i == len(popularMonths) - 1:
            print(popularMonths[i])
        else: print(popularMonths[i], end=", ")

popularBirthday([{"month": 12}, {"month": 11}, {"month": 5}, {"month": 4}])

def PriceCheck(products,productPrices, productsSold, soldPrice):
    Pro = {}
    for i in range(len(products)):
        Pro[products[i]] = productPrices[i]
    error = 0
    for i in range(len(productsSold)):
        if Pro[productsSold[i]] != soldPrice[i]: error += 1
    return error

print(PriceCheck(['e', 'm', 'c'], [1,2,3], ['e', 'e', 'c', 'm'], [1, 1, 3, 2]))

def wordMorph(mapping, s):
    dictionary, string = {}, ""
    for row in range(len(mapping)):
        dictionary[mapping[row][0]] = mapping[row][1]
    for i in s:
        corr = dictionary[ord(i)]
        string += chr(corr)
    return string

print(wordMorph([[105,115], [98, 97], [97,97], [100, 100]], "ibad"))

def mappinExist(a, b):
    d = {}
    for i in range(len(a)):
        if a[i] in d:
            if d[a[i]] != b[i]:
                return False
        else:
            d[a[i]] = b[i]
    return True
print(mappinExist('zartad', 'mbsllq'))
