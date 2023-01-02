i=0
j=1
a=[0,1]
while True:
    
    if (a[i]+a[j])>=100:
        break
    a.append(a[i]+a[j])
    i=i+1
    j=j+1
print(a)
    
