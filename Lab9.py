from datetime import date, timedelta

n=int(input("Enter the number of days to be added: "))
newdate=date.today()+timedelta(n)
print(newdate)

