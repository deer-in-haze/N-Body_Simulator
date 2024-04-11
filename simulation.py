from particles import Particles
from animation import ParticleAnimation
from calculations import CentreOfMass, Acceleration
from settings import Settings
from figure import Figure
from figure_settings import FigureSettings
from decorators import status_update


class Simulation:
    def __init__(self, particle_system, settings, frames, filename):
        self.filename = filename
        self.settings = settings
        self.frames = frames
        self.particles = Particles()
        self.particle_system = particle_system

    @status_update
    def start(self):
        for particle in self.particle_system:
            self.particles.add_particle(particle)

        com = CentreOfMass(self.particles.mass_list, self.particles.position_list, self.particles.velocity_list)
        com.centre_positions_and_velocities()

        fig_settings = FigureSettings(particle_list=self.particles)
        fig_settings.calculate_limits()
        fig = Figure(self.particles, fig_settings)
        fig.plot_figure()

        acceleration = Acceleration(self.particles.position_list, self.particles.mass_list,
                                    self.settings.get_softening(), self.settings.get_gravity_const())

        animation_func = ParticleAnimation(fig, acceleration, self.particles, self.settings, lines_on=True,
                                           frames=self.frames)
        animation_func.create_animation()
        animation_func.save_animation(filename=self.filename)
