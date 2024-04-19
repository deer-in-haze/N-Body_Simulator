from constants import GRAVITY_CONST, DAY, HOUR, SMALL_MASS_TIMESTEP
from decorators import singleton

@singleton
class Settings:
    def __init__(self):
        self.__gravity_const = GRAVITY_CONST
        self.__softening = 0.1
        self.__step_size = DAY
        self.__half_step_size = 0.5 * self.__step_size

    def set_gravity_const(self, gravity_const):
        self.__gravity_const = gravity_const

    def get_gravity_const(self):
        return self.__gravity_const

    def set_step_size(self, step_size):
        self.__step_size = step_size
        self.__half_step_size = 0.5 * step_size

    def get_step_size(self):
        return self.__step_size

    def set_softening(self, softening):
        self.__softening = softening

    def get_softening(self):
        return self.__softening

    def get_half_step_size(self):
        return self.__half_step_size

