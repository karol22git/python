import numpy as np
from matplotlib import pyplot as plt
def SIN(x) :
    return np.sin(x)

def g(x) :
    return x - x**3/6 + x**5/120

theta = np.linspace(-2*np.pi,2*np.pi,200)

fig, ax = plt.subplots()

fig.canvas.manager.set_window_title("Plots for ex 8.")
plt.title("Sin function and its approximation with Taylor series")

ax.plot(theta,SIN(theta),color = "blue",label = "sin(x)")
ax.plot(theta,g(theta),color = "red",label = "g(x)")


tick_values = np.linspace(-2*np.pi, 2 * np.pi,10)
tick_values2 = np.linspace(g(-2*np.pi),g(2*np.pi),10)
plt.grid(color="grey",linestyle="--",linewidth=0.5)
ax.set_xticks(tick_values)
ax.set_yticks(tick_values2)
plt.legend()
plt.show()