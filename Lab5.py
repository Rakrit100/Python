def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

def main():
    a=int(input("Enter the First no.: "))
    b=int(input("Enter the Second no.: "))
    print("Menu: \nI) Addition \nII) Subtraction \nIII) Multiplication \nIV) Division")
    choice=int(input("Enter your choice(1,2,3,4) : "))
    if(choice==1):
        print(add(a,b))
    elif(choice==2):
        print(sub(a,b))
    elif(choice==3):
        print(multi(a,b))
    elif(choice==4):
        print(div(a,b))
    else:
        print("Incorrect Choice")
if __name__=="__main__":
    main()
