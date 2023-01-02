import math
def arms(n):
    sum=0
    n1=n
    c=len(str(n1))
    while(n1!=0):
          d=n1%10
          sum=sum+math.pow(d,c)
          n1=n1//10
    if sum == n:
         print(f"{n} ia an Armsyrong number")

def main():
    a=int(input("Enter the Starting Range: "))
    b=int(input("Enter the Ending Range: "))
    for i in range (a,b):
        arms(i)
if __name__=="__main__":
    main()
