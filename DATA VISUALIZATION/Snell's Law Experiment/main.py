import matplotlib.pyplot as plt
import math


# A light ray from air entering water of refactive index, n = 1.33

# Defining the Variables
n1 = 1 # Refractive index of air
n2 = 1.33 # Refractive index of water

# Generate the angles of incidence with 5 degree increments
theta_i = []
start = 0
for _i in range(30):
    theta_i.append(start)
    start += 5

print(len(theta_i))
print(theta_i[-1])


# Calculate the angles of refraction using Snell's Law
# Snell's Law :> n1sinO1 = n2sinO2
# O2 = sin-1((n1sinO1/n2))
theta_r = []
for angle in theta_i:
    calculated_theta_r = ((n1 * sin(angle))/n2)
