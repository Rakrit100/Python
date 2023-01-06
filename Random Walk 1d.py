import numpy as np
import matplotlib.pyplot as plt
import random
 
n = 100000
x=0
timepoint=np.arange(n+1)
positions=[x]
for i in range(1, n+1):
    val = random.randint(1, 2)
    if val == 1:
        x+=1
    elif val == 2:
        x-=1
    positions.append(x)

plt.title("Random Walk ($n = " + str(n) + "$ steps)")
plt.plot(timepoint,positions, c='r')
plt.show()

