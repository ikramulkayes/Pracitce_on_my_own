num1 = int(input(""))
sq = ""
for i in range(1,num1+1):
    if i == 1:
        print("=== Iteration ",i ,"===")
        print(i)
    elif i % 2 == 0:
        print("=== Iteration ",i ,"===")
        for k in range(1,i+1):
            v = "X"*k
            print(v)
    else:
        print("=== Iteration ",i ,"===")
        for k in range(1,i+1):
            sq += str(k)
        for gg in range(i):
            print(sq)
    sq = ""