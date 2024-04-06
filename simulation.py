from matplotlib import pyplot as plt
from particles import Particles
from animation import Animation
from calculations import CentreOfMass, Acceleration
from settings import Settings
from figure import Figure
from decorators import status_update


class Simulation:
    def __init__(self, particle_system, filename):
        self.filename = filename
        self.settings = Settings()
        self.particles = Particles()
        self.particle_system = particle_system

    @status_update
    def start(self):
        for particle in self.particle_system:
            self.particles.add_particle(particle)

        com = CentreOfMass(self.particles.mass_list, self.particles.position_list, self.particles.velocity_list)
        com.centre_positions_and_velocities()

        fig = Figure(self.particles)
        fig.plot_figure()

        acceleration = Acceleration(self.particles.position_list, self.particles.mass_list,
                                    self.settings.get_softening(), self.settings.get_gravity_const())

        animation_func = Animation(fig, acceleration, self.particles, self.settings)
        animation_func.create_animation()
        plt.show()
        animation_func.save_animation(filename=self.filename)
