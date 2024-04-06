import numpy as np
from decorators import status_update


class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = np.zeros((1, 2))


class Particles:
    def __init__(self):
        self.particle_list = []
        self.mass_list = np.zeros((0, 1))
        self.position_list = np.zeros((0, 2))
        self.velocity_list = np.zeros((0, 2))
        self.acceleration_list = np.zeros((0, 2))

    @status_update
    def add_particle(self, new_particle):
        self.particle_list.append(new_particle)
        self.mass_list = np.vstack((self.mass_list, new_particle.mass))
        self.position_list = np.vstack((self.position_list, new_particle.position))
        self.velocity_list = np.vstack((self.velocity_list, new_particle.velocity))
        self.acceleration_list = np.vstack((self.acceleration_list, new_particle.acceleration))
