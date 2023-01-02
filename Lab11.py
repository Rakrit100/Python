dict1={}
dict2={}
file=open("G:\lab11.txt")
for line in file:
    dict1={}
    for l in line:
        dict1.update({l:line.count(l)})
    for i in dict1.keys():
        if i in dict2:
            dict2.update({i:(line.count(i)+dict2[i])})
        else:
            dict2.update({i:line.count(i)})
print (dict2)
