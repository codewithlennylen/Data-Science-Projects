import matplotlib.pyplot as plt
import math

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

    # Convert the angle to radians first. 
    # The math.sin function expects the input in radians
    angle_radians = angle / 57.2958

    calculated_theta_r = (math.sin(angle_radians))
    calculated_theta_r = ((n1 * calculated_theta_r)/n2)
    
    # After computing the arcsine of the input,
    # Convert the output back to degrees 
    calculated_theta_r = math.asin(calculated_theta_r) * 57.2958

    theta_r.append(calculated_theta_r)

print(len(theta_r))
print(theta_r[-1])

# print('\n\n')
# print(math.sin(50/57.2958)) # 0.7660442425476806
# print(math.asin(0.7660442425476806) * 57.2958)

# Plot theta_i against theta_r
plt.plot(theta_i, theta_r, marker='X')
# plt.plot([math.sin(i) for i in theta_i], [math.sin(r) for r in theta_r]) # Epic Fail!
plt.xlabel('Angle of Incidence')
plt.ylabel('Angle of Refraction')
plt.title('Graphical Representation of Snell\'s Law')
plt.show()