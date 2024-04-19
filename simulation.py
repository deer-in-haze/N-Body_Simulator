from particles import Particles
from animation import ParticleAnimation
from calculations import CentreOfMass, Acceleration, Limits
from figure import Figure
from figure_settings import FigureSettingsBuilder
from decorators import status_update
from animation_settings import AnimationSettingsBuilder


class Simulation:
    def __init__(self, particle_system, settings, figure_settings, frames, filename):
        self.__filename = filename
        self.__settings = settings
        self.__figure_settings = figure_settings
        self.__frames = frames
        self.__particles = Particles()
        self.__particle_system = particle_system

    def __initiate_particles(self):
        for particle in self.__particle_system:
            self.__particles.add_particle(particle)

    @status_update
    def start(self):

        self.__initiate_particles()

        com = CentreOfMass(self.__particles)
        com.centre_positions_and_velocities()

        limits = Limits(self.__particles)
        limits.calculate_limits()

       # figure_settings_builder = FigureSettingsBuilder()
       # figure_settings = figure_settings_builder.set_line_style(':').build()

        figure = Figure(self.__particles, limits, self.__figure_settings)
        figure.plot_figure()

        acceleration = Acceleration(self.__particles, self.__settings)

        animation_settings_builder = AnimationSettingsBuilder()
        animation_settings = animation_settings_builder.build()

        animation_func = ParticleAnimation(figure, acceleration,
                                           self.__particles,
                                           self.__settings,
                                           animation_settings)
        animation_func.create_animation()
        animation_func.save_animation(filename=self.__filename)
