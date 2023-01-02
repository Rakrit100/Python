import pandas as pd
df1 = pd.DataFrame(
    [('Rakshith', 50,49,50), 
     ('Jose', 50,50,50),
     ('Tejas', 45,52,48)], 
    columns=['Student Name', 'Computer', 'Science', 'Maths']
)
print(df1)
df2 = pd.DataFrame(
    [('Ritvik', 40,32,38),
    ('Vivek', 41,35,41)],
    columns=['Student Name', 'Computer', 'Science', 'Maths']
)
print(df2)
df3 = pd.concat([df1, df2], ignore_index=True)
print(df3)
