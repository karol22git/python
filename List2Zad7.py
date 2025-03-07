import sys
import numpy as np
from matplotlib import pyplot as plt
x, y, r = input("x = ?, y = ?, r = ?").split()
try:
    x = int(x)
    y = int(y)
    r = int(r)
except ValueError:
    print("error")
    sys.exit()

theta = np.linspace(0,2*np.pi,100)
X= np.cos(theta)*r + x
Y = np.sin(theta)*r + y

#tworzymy nowa figure fig, oraz zbiory podwykresow ax
#figure canvas, one or more axes = areas where data will be plotted
#figure moze zawierac wiele podwykresow, kontener na wykresy
#ax to pojedynczy wykres
fig, ax = plt.subplots()

fig.canvas.manager.set_window_title("Plot for ex 7")

plt.title("Circle draw in polar coordinates")

plt.xlabel("x - axis")
plt.ylabel("y - axis")

ax.plot(X,Y,label="circle")
ax.plot(x,y,marker="o",markersize=5,color="red",label="center of circle")
plt.show()

#fig = plt.subplots()
#fig.plit(thta)