import numpy as np
import matplotlib.animation as animation
from decorators import status_update


class ParticleAnimation:
    def __init__(self, figure, acceleration, particle_list, settings, **kwargs):
        self.acceleration_list = particle_list.acceleration_list
        self.velocity_list = particle_list.velocity_list
        self.position_list = particle_list.position_list
        self.softening = settings.get_softening()
        self.step_size = settings.get_step_size()
        self.half_step_size = settings.get_half_step_size()
        self.acceleration = acceleration
        self.scatter = figure.scatter
        self.figure = figure.figure
        self.lines = figure.lines
        self.lines_on = kwargs.get('lines_on', False)

        self.frames = kwargs.get('frames', 200)
        self.interval = kwargs.get('interval', 20)

        self.blit = False
        self.anim = None

    def animate(self, *args):
        self.velocity_list += self.acceleration_list * self.half_step_size
        self.position_list += self.velocity_list * self.step_size
        self.acceleration_list = self.acceleration.acceleration_calculation()
        self.velocity_list += self.acceleration_list * self.half_step_size
        self.scatter.set_offsets(self.position_list)

        if self.lines_on:
            for line, position in zip(self.lines, self.position_list):
                line.set_xdata(np.append(line.get_xdata(), position[0]))
                line.set_ydata(np.append(line.get_ydata(), position[1]))

                # limits shown data points
                line.set_xdata(line.get_xdata()[-self.frames:])
                line.set_ydata(line.get_ydata()[-self.frames:])

    @status_update
    def create_animation(self):
        self.anim = animation.FuncAnimation(self.figure, self.animate, frames=self.frames, interval=self.interval,
                                            blit=self.blit)

    @status_update
    def save_animation(self, filename='test.gif'):
        self.anim.save(filename, writer='pillow')
