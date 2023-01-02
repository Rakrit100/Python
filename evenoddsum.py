esum=0
osum=0
for n in range (0,101):
    if(n%2==0):
        esum=esum+n
    elif (n%2!=0):
        osum=osum+n
print("Even sum = ",esum)
print("Odd sum = ",osum)
