def swap(a,b):
    tmp=a
    a=b
    b=tmp
    print("After Swap: n1 = ",a," n2 = ",b)
    return

n1=int(input("Enter: "))
n2=int(input("Enter: "))
print("Before Swap: n1 = ",n1," n2 = ",n2)
swap(n1,n2)
