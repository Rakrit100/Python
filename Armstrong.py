a=int(input("Start: "))
b=int(input("Stop: "))
for n in range(a,b):
    n1=n
    sum=int(0)
    while(n1!=0):
        d=int(n1%10)
        sum=int((d*d*d)+sum)
        n1=int(n1/10)
    if(n==sum):
        print(n," is an Armstrong no.")
            
