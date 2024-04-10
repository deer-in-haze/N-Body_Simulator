import numpy as np
from decorators import status_update
from constants import MASS_SUN


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
    def create_particles(self, planet_system_data, orbital_velocity_instance):
        self.particle_list.append(Particle(planet_system_data.host_mass * MASS_SUN, [0, 0], [0, 0]))  # system host star

        for i in range(planet_system_data.planet_count):
            self.particle_list.append(
                Particle(planet_system_data.planet_mass_list[i], planet_system_data.position_list[i],
                         orbital_velocity_instance.velocity_list[i]))

    @status_update
    def add_particle(self, new_particle):
        self.particle_list.append(new_particle)
        self.mass_list = np.vstack((self.mass_list, new_particle.mass))
        self.position_list = np.vstack((self.position_list, new_particle.position))
        self.velocity_list = np.vstack((self.velocity_list, new_particle.velocity))
        self.acceleration_list = np.vstack((self.acceleration_list, new_particle.acceleration))
