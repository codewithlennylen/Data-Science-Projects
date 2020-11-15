# import matplotlib.pyplot as plt
import math
import numpy as np

# A light ray from air entering water of refactive index, n = 1.33

# Defining the Variables
n1 = 1 # Refractive index of air
n2 = 1.33 # Refractive index of water

## NOTE: The value returned by the math.sin function is in radians!!
# 1 Radian = 57.2958 Degrees

# Generate the angles of incidence with 5 degree increments
theta_i = []
start = 5
for _i in range(10):
    theta_i.append(start)
    start += 5

print(len(theta_i))
print(theta_i[-1])


# Calculate the angles of refraction using Snell's Law
# Snell's Law :> n1sinO1 = n2sinO2
# O2 = sin-1((n1sinO1/n2))
theta_r = []
for angle in theta_i:

    calculated_theta_r = (math.sin(angle)) * 57.2958 # Convert radians to degrees
    calculated_theta_r = ((n1 * math.sin(angle))/n2)
    # calculated_theta_r = 1/math.sin(calculated_theta_r)
    calculated_theta_r = math.asin(calculated_theta_r)

    theta_r.append(calculated_theta_r)

print(len(theta_r))
print(theta_r[-1])

print('\n\n')
print(math.sin(50)*57.2958)
print(np.sin(50)*57.2958)