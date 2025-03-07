import numpy as np
from matplotlib import pyplot as plt
def f(x) :
    return 2*np.sin(x)

user_input_str = input("Enter:")

X = [float(x) for x in user_input_str.split()]

fig, ax = plt.subplots()

fig.canvas.manager.set_window_title("Plot for ex 6")

ax.plot(X,f(X),label = "2*sin(x)")

plt.title("Applying 2*sin(x) for vector given by user")

plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.legend()

plt.grid(color="grey",linestyle="--",linewidth=0.5)
plt.show()