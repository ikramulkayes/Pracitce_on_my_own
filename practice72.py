num = int(input("Enter a number: "))
sum = ""
long = 0
for i in range(num):
    stid = input("Enter your student id: ")
    for i in stid:
        long = long + int(i)
    if long in range(5,11):
        sum = sum + "Ciao\n" 
    elif long in range(11,16):
        sum = sum + "Hello\n" 
    elif long in range(20,26):
        sum = sum + "Hola\n" 
    elif long in range(30,36):
        sum = sum + "Salut\n" 
    else:
        sum = sum + "ByeBye\n"
    long = 0
sum = sum.rstrip()
print(sum)