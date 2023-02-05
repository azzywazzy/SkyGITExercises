import math

gravity = 9.81
velocity = 44
theta = 80 * (math.pi/180)
distance = 0.5
heightBarrel = 1

height = heightBarrel + distance*math.tan(theta) - (gravity*distance*distance)/(2*((velocity*math.cos(theta))*(velocity*math.cos(theta))))

print(height)



