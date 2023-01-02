str1=input("Enter the String: ")
dict1={}
for s in str1:
    dict1.update({s:str1.count(s)})
print (dict1)
