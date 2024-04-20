from particles import Particles
from animation import ParticleAnimation
from calculations import CentreOfMass, Acceleration, Limits
from figure import Figure
from figure_settings import FigureSettings
from decorators import status_update
from animation_settings import AnimationSettings
from simulation_settings import SimulationSettings


class Simulation:
    def __init__(self, particle_system, step_size, gravity_const, frames, filename):
        self.__particle_system = particle_system
        self.__step_size = step_size
        self.__gravity_const = gravity_const
        self.__frames = frames
        self.__filename = filename
        self.__particles = Particles()


    def __initiate_particles(self):
        for particle in self.__particle_system:
            self.__particles.add_particle(particle)

    @status_update
    def start(self):

        self.__initiate_particles()
        print(self.__frames)

        com = CentreOfMass(self.__particles)
        com.centre_positions_and_velocities()

        limits = Limits(self.__particles)
        limits.calculate_limits()

        figure_settings = FigureSettings.Builder().set_line_style(':').build()

        figure = Figure(self.__particles, limits, figure_settings)
        figure.plot_figure()

        simulation_settings = SimulationSettings.Builder().set_step_size(self.__step_size).set_gravity_const(self.__gravity_const).build()

        acceleration = Acceleration(self.__particles, simulation_settings)

        animation_settings = AnimationSettings.Builder().set_frames(self.__frames).build()

        animation_func = ParticleAnimation(figure, acceleration,
                                           self.__particles,
                                           simulation_settings,
                                           animation_settings)
        animation_func.create_animation()
        animation_func.save_animation(filename=self.__filename)
