import matplotlib.animation as animation
from decorators import status_update


class Animation:
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

    @status_update
    def create_animation(self):
        self.anim = animation.FuncAnimation(self.figure, self.animate, frames=self.frames, interval=self.interval,
                                            blit=self.blit)

    @status_update
    def save_animation(self, filename='test.gif'):
        self.anim.save(filename, writer='pillow')
