dict1={}
file=open("G:lab11.txt")
st=file.read()
for l in st:
    dict1.update({l:st.count(l)})
print(dict1)
