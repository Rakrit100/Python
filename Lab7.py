def evencheck(x):
    if (x%2==0):
        return True
    else:
        return False
def main():
    n=int(input("Enter the no. of elements: "))
    list1=[]
    for i in range (0,n):
        list1.append(int(input(f"Enter item {i}: ")))
    list2=filter(evencheck,list1)
    for x in list2:
        print (x)
if __name__=="__main__":
    main()
    
