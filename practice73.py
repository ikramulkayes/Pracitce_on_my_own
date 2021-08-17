word = input("Enter a number: ")
word = word.strip(".")
word = word.strip(". ")
lst = word.split()
gg = []
for i in lst:
    if i not in gg:
        gg.append(i)
lst = gg
sym = input("symbol: ")
sym = sym[1:-1]
sym = sym.split(", ")
count = len(sym)
mm = []
for i in sym:
    i = i [1:-1]
    mm.append(i)
sym = mm
final = {}
for i in lst:
    sum = 0
    for k in i:
        if k != ".":
            sum += ord(k)
    val = sum % count 
    m = i.strip(".")
    if sym[val] not in final.keys():
        final[sym[val]] = [m]
    else:
        final[sym[val]].append(m)
    sum = 0
print(final)