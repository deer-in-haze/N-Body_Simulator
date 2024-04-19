import numpy as np
from constants import PI
from decorators import status_update


class Limits:
    def __init__(self, particle_list):
        self.__position_list = particle_list.get_position_list()
        self.__limit = 0

    def get_limit(self):
        return self.__limit

    def calculate_limits(self):
        max_distance = 0
        for i in range(len(self.__position_list)):
            for j in range(i + 1, len(self.__position_list)):
                distance = ((self.__position_list[j][0] -
                             self.__position_list[i][0]) ** 2 + (
                             self.__position_list[j][1] -
                             self.__position_list[i][1]) ** 2) ** 0.5
                if distance > max_distance:
                    max_distance = distance
        self.__limit = max_distance + max_distance * 0.1


class CentreOfMass:
    def __init__(self, particle_list):
        self.__mass_list = particle_list.get_mass_list()
        self.__com_p = np.zeros((0, 2))
        self.__com_v = np.zeros((0, 2))
        self.__position_list = particle_list.get_position_list()
        self.__velocity_list = particle_list.get_velocity_list()

    def get_position_list(self):
        return self.__position_list

    def get_velocity_list(self):
        return self.__velocity_list

    @status_update
    def __centre_of_mass_position(self):
        self.__com_p = np.sum(np.multiply(self.__mass_list, self.__position_list), axis=0) / np.sum(self.__mass_list,
                                                                                                  axis=0)
        return self.__com_p

    @status_update
    def __centre_of_mass_velocity(self):
        self.__com_v = np.sum(np.multiply(self.__mass_list, self.__velocity_list), axis=0) / np.sum(self.__mass_list,
                                                                                                  axis=0)
        return self.__com_v

    @status_update
    def centre_positions_and_velocities(self):
        self.__com_p = self.__centre_of_mass_position()
        self.__com_v = self.__centre_of_mass_velocity()
        self.__position_list -= self.__com_p
        self.__velocity_list -= self.__com_v


class Acceleration:
    def __init__(self, particle_list, settings):
        self.__mass_list = particle_list.get_mass_list()
        self.__softening = settings.get_softening()
        self.__gravity = settings.get_gravity_const()
        self.__position_list = particle_list.get_position_list()

    def get_position_list(self):
        return self.__position_list

    def acceleration_calculation(self):
        x = self.__position_list[:, 0:1]
        y = self.__position_list[:, 1:2]
        dx = x.T - x
        dy = y.T - y
        inv_r3 = (dx ** 2 + dy ** 2 + self.__softening ** 2) ** (-1.5)
        acceleration_x = self.__gravity * (dx * inv_r3) @ self.__mass_list
        acceleration_y = self.__gravity * (dy * inv_r3) @ self.__mass_list
        return np.hstack((acceleration_x, acceleration_y))


class OrbitalVelocity:
    def __init__(self, planet_system_data):
        self.__velocity_list = []
        self.__planet_count = planet_system_data.get_planet_count()
        self.__semi_major_axis_list = planet_system_data.get_semi_major_axis_list()
        self.__orbital_period_list = planet_system_data.get_orbital_period_list()

    def get_velocity_list(self):
        return self.__velocity_list
    @status_update
    def calculate_orbital_velocity(self):
        for semi_major_axis, orbital_period in zip(self.__semi_major_axis_list, self.__orbital_period_list):
            orbital_velocity = (2 * PI * semi_major_axis) / orbital_period
            self.__velocity_list.append([0, orbital_velocity])
