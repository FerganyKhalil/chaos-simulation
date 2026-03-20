import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

r_values = np.linspace(2.5, 4.0, 1000)
iterations = 1000
last = 100

x = 1e-5 * np.ones(len(r_values))

results = []

for i in range(iterations):
    x = logistic_map(r_values, x)
    if i >= (iterations - last):
        results.append(x)

results = np.array(results)

plt.figure(figsize=(10, 7))
for i in range(last):
    plt.plot(r_values, results[i], ',k', alpha=0.25)

plt.title("Bifurcation Diagram - Logistic Map")
plt.xlabel("r")
plt.ylabel("x")
plt.show()
