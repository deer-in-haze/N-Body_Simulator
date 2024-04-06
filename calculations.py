import numpy as np
from decorators import status_update


class CentreOfMass:
    def __init__(self, mass_list, position_list, velocity_list):
        self.mass_list = mass_list
        self.position_list = position_list
        self.velocity_list = velocity_list
        self.com_p = np.zeros((0, 2))
        self.com_v = np.zeros((0, 2))

    def centre_of_mass_position(self):
        self.com_p = np.sum(np.multiply(self.mass_list, self.position_list), axis=0) / np.sum(self.mass_list, axis=0)
        return self.com_p

    def centre_of_mass_velocity(self):
        self.com_v = np.sum(np.multiply(self.mass_list, self.velocity_list), axis=0) / np.sum(self.mass_list, axis=0)
        return self.com_v

    @status_update
    def centre_positions_and_velocities(self):
        com_p = self.centre_of_mass_position()
        com_v = self.centre_of_mass_velocity()
        self.position_list -= com_p
        self.velocity_list -= com_v


class Acceleration:
    def __init__(self, position_list, mass_list, softening, gravity):
        self.position_list = position_list
        self.mass_list = mass_list
        self.softening = softening
        self.gravity = gravity

    def acceleration_calculation(self):
        x = self.position_list[:, 0:1]
        y = self.position_list[:, 1:2]
        dx = x.T - x
        dy = y.T - y
        inv_r3 = (dx ** 2 + dy ** 2 + self.softening ** 2) ** (-1.5)
        acceleration_x = self.gravity * (dx * inv_r3) @ self.mass_list
        acceleration_y = self.gravity * (dy * inv_r3) @ self.mass_list
        return np.hstack((acceleration_x, acceleration_y))
