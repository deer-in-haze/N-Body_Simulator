import numpy as np
from decorators import status_update
from constants import MASS_SUN


class Particle:
    def __init__(self, mass, position, velocity):
        self.__mass = mass
        self.__position = position
        self.__velocity = velocity
        self.__acceleration = np.zeros((1, 2))

    def get_mass(self):
        return self.__mass

    def get_position(self):
        return self.__position

    def get_velocity(self):
        return self.__velocity

    def get_acceleration(self):
        return self.__acceleration


class Particles:
    def __init__(self):
        self.__particle_list = []
        self.__mass_list = np.zeros((0, 1))
        self.__position_list = np.zeros((0, 2))
        self.__velocity_list = np.zeros((0, 2))
        self.__acceleration_list = np.zeros((0, 2))

    def get_particle_list(self):
        return self.__particle_list

    def get_mass_list(self):
        return self.__mass_list

    def get_position_list(self):
        return self.__position_list

    def get_velocity_list(self):
        return self.__velocity_list

    def get_acceleration_list(self):
        return self.__acceleration_list

    @status_update
    def create_particles(self, planet_system_data, orbital_velocity_instance):
        self.__particle_list.append(Particle(planet_system_data.get_host_mass() * MASS_SUN, [0, 0], [0, 0]))  # system host star

        for i in range(planet_system_data.get_planet_count()):
            self.__particle_list.append(
                Particle(planet_system_data.get_planet_mass_list()[i], planet_system_data.get_position_list()[i],
                         orbital_velocity_instance.get_velocity_list()[i]))

    @status_update
    def add_particle(self, new_particle):
        self.__particle_list.append(new_particle)
        self.__mass_list = np.vstack((self.__mass_list, new_particle.get_mass()))
        self.__position_list = np.vstack((self.__position_list, new_particle.get_position()))
        self.__velocity_list = np.vstack((self.__velocity_list, new_particle.get_velocity()))
        self.__acceleration_list = np.vstack((self.__acceleration_list, new_particle.get_acceleration()))
