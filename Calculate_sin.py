import math
degree=int(input("Enter the degrees: "))
nterm=int(input("Enter the no. of terms: "))
radian=degree*math.pi/180

def calculate_sin():
    result=0
    numerator=radian
    denominator=1
    for i in range (1,nterm+1):
        single_term=numerator/denominator
        result=result+single_term
        numerator=-numerator*radian*radian
        denominator=denominator*(2*i)*(2*i*1)

    return result
print(calculate_sin())
