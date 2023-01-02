n1=int(input("Enter no. 1: "))
n2=int(input("Enter no. 2: "))
n3=int(input("Enter no. 3: "))
if(n1>n2)and(n2>n3):
    largest=n1
else:
    if(n2>n1)and(n2>n3):
        largest=n2
    else:
        largest=n3
print("Largest: ",largest)
