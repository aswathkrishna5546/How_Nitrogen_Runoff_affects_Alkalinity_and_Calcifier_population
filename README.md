# How_Nitrogen_Runoff_affects_Alkalinity_and_Calcifier_population
This Python code runs a simple time-based simulation of two coupled quantities: alkalinity in water and a calcifer population that depends on that alkalinity. Alkalinity is continuously supplied by a constant continental runoff input, but is reduced as the calcifers grow and consume it; meanwhile the calcifer population increases through growth that depends on both the current alkalinity and the current population, and decreases through removal by sedimentation at a constant rate. The model numerically steps forward in small increments over the full simulation period and then plots how alkalinity and calcifer population change through time on the same graph using two y-axes.

## Code
See [`Code.py`](Code.py)

pip install numpy matplotlib
python Code.py
output.png
## Output

![Simulation graph](output.png)
