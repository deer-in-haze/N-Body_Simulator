from data_list_creator import DataListCreator
from data_processing import NASADataProcessor
from calculations import OrbitalVelocity
from particles import Particles
from constants import NASA_DATABASE_API_KEY
from decorators import status_update


class ParticleSystemCreator:
    def __init__(self, hostname):
        self._hostname = hostname

    @status_update
    def create_particle_system(self):
        processor = NASADataProcessor(NASA_DATABASE_API_KEY)
        processor.load_data('clean')
        grouped_data = processor.group_data()
        appender = DataListCreator(grouped_data, self._hostname)
        appender.create_data_list()
        calc = OrbitalVelocity(appender)
        calc.calculate_orbital_velocity()
        particles = Particles()
        particles.create_particles(appender, calc)
        particle_system = particles.get_particle_list()
        return particle_system
