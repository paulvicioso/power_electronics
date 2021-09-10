import numpy as np
import math as math
import matplotlib.pyplot as plt


Vs = 120        # V (rms)
E = 10          # V (DC)
Freq = 60       # Hz
omega = 2 * math.pi * Freq   # angular freq. (rad/s)

R = 2.5         # ohms
L = 6.5e-3      # Henries

Vm = Vs * math.sqrt(2)  # Voltaje Maximo
Z = math.sqrt(R**2 + (omega*L)**2)  # impedancia de la carga
theta = math.atan2((omega*L), R)      # angulo de impedancia de la carga
chi = E / Vm        # relacion de voltaje

# #######################################
# Testing
theta = math.radians(60)
chi = 0.4
#
# #######################################

alpha = math.asin(chi)

# generate an array fo the time
t = np.arange(0, 100e-3, 1e-3)

angles = np.arange(math.pi/2.0, 2*math.pi, 1e-3)

temp = [math.sin(beta - theta)
        + (chi/math.cos(theta) - math.sin(alpha - theta))
        * math.exp((alpha - beta) / math.tan(theta))
        - chi/math.cos(theta) for beta in angles]

angles = np.degrees(angles)

res = [abs(ele) for ele in temp]
x0, y0 = (angles[res.index(min(res))], temp[res.index(min(res))])

xtext, ytext = (max(angles) / 10.0, max(res) / 4.0)

print('El valor de Beta es {}'.format(x0))

# Plot the points using matplotlib
plt.plot(angles, temp, lw=2)
plt.plot(x0, y0, 'go')

text = r'$\beta = {0:.2f}, f(\beta) = {1:.2f}$'.format(x0, math.fabs(y0))

plt.annotate(text, xy=(x0, y0), xytext=(x0 + xtext, ytext),
            arrowprops=dict(facecolor='black', shrink=0.05),)

plt.title(r'Variaciones de $\beta$')
plt.xlabel(r'$\mathit{Angle} \/\/\/ [Degrees]$')
plt.ylabel(r'$\mathit{Valores \/\/ de \/\/ \beta} \/\/\/[\#]$')
plt.grid(True)
plt.show()
