from particles import Particle
from constants import AU, OFFSET

"""PARTICLE MATRIX"""
p1 = Particle(500, [-3, 3], [0, 0])
p2 = Particle(500, [-3, 0], [0, 0])
p3 = Particle(500, [-3,-3], [0, 0])
p4 = Particle(500, [0,3],[0, 0])
p5 = Particle(1000, [0,0], [0, 0])
p6 = Particle(500, [0, -3], [0, 0])
p7 = Particle(1000, [3, 3], [0, 0])
p8 = Particle(500, [3, 0], [0, 0])
p9 = Particle(500,[3, -3], [0, 0])
"""LIST"""
particle_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

"""SOLAR SYSTEM"""
sun = Particle(1.988e30, [OFFSET, OFFSET], [0, 0])
earth = Particle(5.972e24, [AU + OFFSET, OFFSET], [0, 29766.5])
venus = Particle(4.867e24, [OFFSET, 1.082e11 + OFFSET], [34995.75, 0])
mars = Particle(6.39e23, [1.52 * AU + OFFSET, OFFSET], [0, 24130])
mercury = Particle(3.285e23, [0.39 * AU + OFFSET, OFFSET], [0, 47400])
jupiter = Particle(1.898e27, [5.20 * AU + OFFSET, OFFSET], [0, 13070,])
saturn = Particle(5.683e26, [9.58 * AU + OFFSET, OFFSET], [0, 9640])
uranus = Particle(8.681e25, [19.18 * AU + OFFSET, OFFSET], [0, 6810])
neptune = Particle(1.024e26, [30.07 * AU + OFFSET, OFFSET], [0, 5430])
"""LIST"""
inner_solar_system = [sun, earth, venus, mars, mercury]

"""MOON"""
distance_earth_moon = 384400 * 1e3
velocity_moon_relative_to_earth = 1022
position_moon = 1.496e11 + distance_earth_moon
velocity_moon = 29766.5 + velocity_moon_relative_to_earth
moon = Particle(7.342e22, [position_moon, 0], [0,velocity_moon])
"""EARTH SYSTEM"""
earth_system = [earth, moon]

"""CUSTOM SYSTEMS"""
star1 = Particle(1.403 * 10**30, [0, 0], [0, 0])
planet1 = Particle(1.403 * 10**30, [0.799 * AU, 0], [0, 27958.3133])
planet2 = Particle(1.403 * 10**30, [-0.799 * AU, 0], [0, -27958.3133])
"""LISTS"""
binary_system = [star1, planet1]
three_body_system = [star1, planet1, planet2]

