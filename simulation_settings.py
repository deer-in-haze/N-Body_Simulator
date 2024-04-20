from settings import Settings
from constants import GRAVITY_CONST, DAY


class SimulationSettings(Settings):
    class Builder():
        def __init__(self):
            self.__gravity_const = GRAVITY_CONST
            self.__softening = 0.1
            self.__step_size = DAY
            self.__half_step_size = 0.5 * self.__step_size

        def set_gravity_const(self, gravity_const):
            self.__gravity_const = gravity_const
            return self

        def set_step_size(self, step_size):
            self.__step_size = step_size
            self.__half_step_size = 0.5 * step_size
            return self

        def set_softening(self, softening):
            self.__softening = softening
            return self

        def build(self):
            return SimulationSettings(self.__gravity_const,
                                      self.__softening,
                                      self.__step_size)

    def __init__(self, gravity_const, softening, step_size):
        self.__gravity_const = gravity_const
        self.__softening = softening
        self.__step_size = step_size
        self.__half_step_size = 0.5 * self.__step_size

    def get_gravity_const(self):
        return self.__gravity_const

    def get_step_size(self):
        return self.__step_size

    def get_softening(self):
        return self.__softening

    def get_half_step_size(self):
        return self.__half_step_size

    def display(self):
        pass
