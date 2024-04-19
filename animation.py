import numpy as np
import matplotlib.animation as animation
from decorators import status_update


class ParticleAnimation:
    def __init__(self, figure, acceleration, particle_list, settings, animation_settings):
        self.__acceleration_list = particle_list.get_acceleration_list()
        self.__velocity_list = particle_list.get_velocity_list()
        self.__position_list = particle_list.get_position_list()
        self.__softening = settings.get_softening()
        self.__step_size = settings.get_step_size()
        self.__half_step_size = settings.get_half_step_size()
        self.__acceleration = acceleration
        self.__scatter = figure.get_scatter()
        self.__figure = figure.get_figure()
        self.__lines = figure.get_lines()
        self.__lines_on = animation_settings.get_lines()

        self.__frames = animation_settings.get_frames()
        self.__interval = animation_settings.get_interval()

        self.__blit = animation_settings.get_blit()
        self.__anim = None

    def __animate(self, i):
        self.__velocity_list += self.__acceleration_list * self.__half_step_size
        self.__position_list += self.__velocity_list * self.__step_size
        self.__acceleration_list = self.__acceleration.acceleration_calculation()
        self.__velocity_list += self.__acceleration_list * self.__half_step_size
        self.__scatter.set_offsets(self.__position_list)

        if self.__lines_on:
            for line, position in zip(self.__lines, self.__position_list):
                line.set_xdata(np.append(line.get_xdata(), position[0]))
                line.set_ydata(np.append(line.get_ydata(), position[1]))

                line.set_xdata(line.get_xdata()[-self.__frames:])
                line.set_ydata(line.get_ydata()[-self.__frames:])

    @status_update
    def create_animation(self):
        self.__anim = animation.FuncAnimation(self.__figure, self.__animate,
                                              frames=self.__frames,
                                              interval=self.__interval,
                                              blit=self.__blit)

    @status_update
    def save_animation(self, filename='test.gif'):
        self.__anim.save(filename, writer='pillow')
