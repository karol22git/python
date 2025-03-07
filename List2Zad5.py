import sys
from matplotlib import pyplot as plt
import numpy as np
a, b, c = input("a = ?, b = ?, c = ?").split()
try:
    a = int(a)
    b = int(b)
    c = int(c)
except ValueError:
    print("error")
    sys.exit()

def y(x):
    return a*x*x + b*x + c

#generujemy liste(? w kazdym razie zbior) punktow z przedzialu [-10,10] 
#liczacym 100 elementow, o rownym odstepie od siebie
X = np.linspace(-10,10,100)

#zmieniamy nazwe okna ktore wyskakuje po wywolaniu show()
fig = plt.figure()
fig.canvas.manager.set_window_title("Plot for ex 5")

plt.plot(X,y(X),label = "y(x)")

title = str(a) + "*x*x + " + str(b) + "*x + " +str(c)
plt.title(title)

plt.xlabel("x - axis")
plt.ylabel("y - axis")

plt.grid(color="grey",linestyle="--",linewidth=0.5)
plt.legend()
plt.show()