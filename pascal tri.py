def pascal():
    n=int(input("Enter the no. of rows: "))
    k=1
    count=1
    for i in range (0,n):
        for l in range (0,n-k):
            print(end="   ")
        for j in range (0,k):
            if len(str(count))==1:
                 print (count,end="     ")
            if len(str(count))==2:
                 print (count,end="    ")
            if len(str(count))==3:
                print (count,end="   ")
            if len(str(count))==4:
                print (count,end="  ")
            if len(str(count))==5:
                print (count,end=" ")
            if len(str(count))==6:
                print (count,end="")
           
            count+=1
        print()
        k+=1
def main():
    pascal()
if __name__=="__main__":
    main()
            
