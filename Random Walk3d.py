import numpy as np 
import matplotlib.pyplot as plt
import random

n = 1000
 
x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)
 
for i in range(1, n):
    val = random.randint(1, 6)
    if val == 1:
        x[i] = x[i - 1] + 10
        y[i] = y[i - 1]
        z[i] = z[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 10
        y[i] = y[i - 1]
        z[i] = z[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 10
        z[i] = z[i - 1]
    elif val == 4:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 10
        z[i] = z[i - 1]
    elif val == 5:
        x[i] = x[i - 1]
        y[i] = y[i - 1] 
        z[i] = z[i - 1] + 10
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] 
        z[i] = z[i - 1] - 10
     

plt.title(f"Random Walk {n} steps")
plt.subplot(1,1,1, projection='3d')
plt.plot(x,y,z, c='r')
plt.plot(z,y,x, c='g')
plt.plot(y,z,x, c='b')
plt.show()

