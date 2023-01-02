def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main():
    i=0
    n=int(input("Enter "))
    while fib(i)<n:
        print(fib(i))
        i=i+1
if __name__=="__main__":
    main()
