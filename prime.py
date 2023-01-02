l = int(input("Starting Point: "))
u = int(input("Ending point: "))
flag=int(0)
for n in range(l,u+1):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                flag=int(1)
        if(flag!=1):
            print(n)
        n+=1
        flag=int(0)
