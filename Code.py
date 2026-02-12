import numpy as np
import matplotlib.pyplot as plt

k=0.05*10**(3) #growth rate constant, m^3/(moleq*kyr)
Cont_runoff= 4*10**(-3) #continental runoff, moleq/(m^3*kyr), I
Sediment_rate=0.1*10**(3) #calcifer sedimentation rate per calcifer, kyr^(-1)

sim_length=200
dt = 0.001
time = np.arange(0, sim_length, dt)
steps = len(time)

A = np.zeros(steps)
P = np.zeros(steps)

A[0] = 2 #Alkalinity, moleq/m^3
P[0] = 4*10**(-4) #Pop of calcifers, moleq/m^3

for step in range (steps-1) :
    P_growth = k*A[step]*P[step]
    P_sediment = Sediment_rate*P[step]

    #for each time step, we update the value of the stocks
    A[step+1]=A[step]+(Cont_runoff-P_growth)*dt
    P[step+1]=P[step]+(P_growth-P_sediment)*dt

fig, ax1=plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Time [kyr]')
ax1.set_ylabel('Alkalinity [moleq/m^3]', color= 'blue')
plt.plot(time, A, label = 'Alkalinity', color = 'blue')
ax1.tick_params(axis='y', labelcolor= 'blue')

ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('Calcifer Population [mmoleq/m^3]', color= 'pink' )  # we already handled the x-label with ax1
ax2.plot(time, P*10**3, label = 'Calcifer Population', color= 'pink')
ax2.tick_params(axis='y', labelcolor= 'pink')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

