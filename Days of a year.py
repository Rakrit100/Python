n_d=int(input("Enter: "))
n_y=int(n_d/365)
n_w=int(n_d%365/7)
r_n_d=int(n_d%365%7)
print("No. of Years:- ",n_y,", No.of Weeks:- ",n_w,", No. of Days:- ",r_n_d)