lst = (input("Enter a Dictionary: "))
lst = lst[1:-1]
lst = lst.split(", ")
di1 = {}
final = {}
for i in lst:
    a = i.split(":")
    k = a[-1].strip()
    k = int(k)
    b = a[0].strip("'")
    di1[b] = k
num = int(input("Enter a number:"))
for i,v in di1.items():
    if v >= num:
        final[i] = v
print(final)