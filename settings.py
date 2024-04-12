from constants import GRAVITY_CONST, DAY, HOUR, SMALL_MASS_TIMESTEP
from decorators import singleton

@singleton
class Settings:
    def __init__(self, **kwargs):
        self._gravity_const = kwargs.get('gravity_const', GRAVITY_CONST)
        self._step_size = kwargs.get('step_size', SMALL_MASS_TIMESTEP)
        self._softening = kwargs.get('softening', 0.1)
        self._half_step_size = 0.5 * self._step_size

    def set_gravity_const(self, gravity_const):
        self._gravity_const = gravity_const

    def get_gravity_const(self):
        return self._gravity_const

    def set_step_size(self, step_size):
        self._step_size = step_size
        self._half_step_size = 0.5 * step_size

    def get_step_size(self):
        return self._step_size

    def set_softening(self, softening):
        self._softening = softening

    def get_softening(self):
        return self._softening

    def set_half_step_size(self, half_step_size):
        self._half_step_size = half_step_size

    def get_half_step_size(self):
        return self._half_step_size

