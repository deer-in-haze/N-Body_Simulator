from data_list_creator import DataListCreator
from data_processing import DataProcessor
from calculations import OrbitalVelocity
from particles import Particles
from constants import NASA_DATABASE_API_KEY
from decorators import status_update


class ParticleSystemCreator:
    def __init__(self, hostname):
        self.hostname = hostname

    @status_update
    def create_particle_system(self):
        processor = DataProcessor(NASA_DATABASE_API_KEY)
        processor.load_data('clean')
        grouped_data = processor.group_data()
        appender = DataListCreator(grouped_data, self.hostname)
        appender.create_data_list()
        calc = OrbitalVelocity(appender)
        calc.calculate_orbital_velocity()
        particles_from_system = Particles()
        particles_from_system.create_particles(appender, calc)
        particle_system = particles_from_system.particle_list
        return particle_system
