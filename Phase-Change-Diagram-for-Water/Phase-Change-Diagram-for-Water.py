import matplotlib.pyplot as plt
import numpy as np

# Define the temperature and pressure ranges for the phase change diagram
Tmin, Tmax = 200, 800  # in K
Pmin, Pmax = 0, 800  # in kPa

# Define the critical point of water
Tc, Pc = 647.096, 22.064  # in K and MPa

# Define the slope of the liquid-vapor coexistence curve
m = Pc / (Tc ** 0.5)

# Define the temperature and pressure values for the triple point and the critical point
Tp = 273.16  # in K
Pp = 611.73  # in Pa
Tc = 647.096  # in K
Pc = 22.064  # in MPa

# Plot the phase change diagram
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the solid-liquid coexistence curve
Tsl = np.linspace(Tmin, Tp, 100)
Psl = Pp * np.exp((-(1/Tsl)+(1/Tp))*3170)
ax.plot(Tsl, Psl, 'b-', linewidth=2)

# Plot the liquid-vapor coexistence curve
Tlv = np.linspace(Tmin, Tc, 100)
Plv = np.exp(34.541-(5107.3/Tlv))
ax.plot(Tlv, Plv, 'b-', linewidth=2)

# Plot the critical point
ax.plot(Tc, Pc, 'ko', markersize=8)

# Label the plot
ax.set_xlim(Tmin, Tmax)
ax.set_ylim(Pmin, Pmax)
ax.set_xlabel('Temperature (K)')
ax.set_ylabel('Pressure (kPa)')
ax.set_title('Phase Change Diagram for Water')

ax.annotate('Liquid', xy=(300, 100), xytext=(400, 200),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Solid', xy=(250, 1), xytext=(200, 10),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Gas', xy=(700, 800), xytext=(600, 700),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.grid()

plt.show()
