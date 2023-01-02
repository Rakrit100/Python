import pandas as po
import matplotlib.pyplot as mat
file=po.read_csv(r"C:\Users\raksh\Downloads\BCA\BCA SEM III\3- PYTHON -3\IDLE III sem BCA\Lab program 16.csv")
print(file)

#part a
print("Total Profit:- ",file['Total profit'].sum())
mat.plot(file['Months'],file['Total units'],'--b',label='Total units',linewidth=4)
mat.xlabel('Months')
mat.ylabel('Sold Unit')
mat.legend(loc='lower right')
mat.show()

#part b
mat.plot(file['Months'],file['Pen'],label='Pen Sales',linewidth=4)
mat.plot(file['Months'],file['Book'],label='Book Sales',linewidth=4)
mat.plot(file['Months'],file['Marker'],label='Marker Sales',linewidth=4)
mat.plot(file['Months'],file['Chair'],label='Chair Sales',linewidth=4)
mat.plot(file['Months'],file['Table'],label='Table Sales',linewidth=4)
mat.plot(file['Months'],file['Pen stand'],label='Pen Stand Sales',linewidth=4)
mat.xlabel("Months")
mat.ylabel("Units sold")
mat.legend(loc='upper left')
mat.show()

#part c
mat.bar(file['Months'],file['Chair'],label='Chair Sales',width=0.5)
mat.bar(file['Months'],file['Table'],label='Table Sales',width=-0.5)
mat.xlabel("Months")
mat.ylabel("Units sold")
mat.legend(loc='upper left')
mat.show()

#part d
mat.plot([],[],'--c',label='Pen Sales',linewidth=4)
mat.plot([],[],'--b',label='Book Sales',linewidth=4)
mat.plot([],[],'--g',label='Marker Sales',linewidth=4)
mat.plot([],[],'--y',label='Chair Sales',linewidth=4)
mat.plot([],[],'--k',label='Table Sales',linewidth=4)
mat.plot([],[],'--r',label='Pen Stand Sales',linewidth=4)
mat.stackplot(file['Months'],file['Pen'],file['Book'],file['Marker'],file['Chair'],file['Table'],file['Pen stand'],colors=['c','b','g','y','k','r'])
mat.xlabel("Months")
mat.ylabel("Units sold")
mat.legend(loc='upper left')
mat.show()
