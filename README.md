# How_Nitrogen_Runoff_affects_Alkalinity_and_Calcifier_population
This Python code runs a simple time-based simulation of two coupled quantities: alkalinity in water and a calcifer population that depends on that alkalinity. Alkalinity is continuously supplied by a constant continental runoff input, but is reduced as the calcifers grow and consume it; meanwhile the calcifer population increases through growth that depends on both the current alkalinity and the current population, and decreases through removal by sedimentation at a constant rate. The model numerically steps forward in small increments over the full simulation period and then plots how alkalinity and calcifer population change through time on the same graph using two y-axes.

## Code
See [`Code.py`](Code.py)

pip install numpy matplotlib
python Code.py
output.png
## Output

![Simulation graph](output.png)

import numpy as np

# Use a non-interactive backend so this works anywhere (including GitHub/Codespaces/Actions)
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

# -----------------------------
# Parameters
# -----------------------------
k = 0.05 * 10**3            # growth rate constant, m^3/(moleq*kyr)
Cont_runoff = 4 * 10**(-3)  # continental runoff, moleq/(m^3*kyr), I
Sediment_rate = 0.1 * 10**3 # calcifer sedimentation rate per calcifer, kyr^(-1)

sim_length = 200
dt = 0.001
time = np.arange(0, sim_length, dt)
steps = len(time)

# -----------------------------
# State variables
# -----------------------------
A = np.zeros(steps)  # Alkalinity, moleq/m^3
P = np.zeros(steps)  # Calcifer population, moleq/m^3

A[0] = 2             # initial alkalinity
P[0] = 4 * 10**(-4)  # initial population

# -----------------------------
# Time integration (Euler)
# -----------------------------
for step in range(steps - 1):
    P_growth = k * A[step] * P[step]
    P_sediment = Sediment_rate * P[step]

    A[step + 1] = A[step] + (Cont_runoff - P_growth) * dt
    P[step + 1] = P[step] + (P_growth - P_sediment) * dt

# -----------------------------
# Plotting
# -----------------------------
fig, ax1 = plt.subplots()

ax1.set_xlabel("Time [kyr]")
ax1.set_ylabel("Alkalinity [moleq/m^3]", color="blue")
ax1.plot(time, A, label="Alkalinity", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

ax2 = ax1.twinx()
ax2.set_ylabel("Calcifer Population [mmoleq/m^3]", color="pink")
ax2.plot(time, P * 10**3, label="Calcifer Population", color="pink")
ax2.tick_params(axis="y", labelcolor="pink")

fig.tight_layout()

# Save the figure so it can be displayed on GitHub via README embedding
plt.savefig("output.png", dpi=200, bbox_inches="tight")
print("Saved plot to output.png")

