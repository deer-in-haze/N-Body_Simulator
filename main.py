from simulation import Simulation
from particle_systems import three_body_system
from particle_system_creator import ParticleSystemCreator
from data_processing import DataProcessor
from constants import NASA_DATABASE_API_KEY

if __name__ == '__main__':
    data_path = '/home/migle/PycharmProjects/n_body_simulator/nasa_exoplanet_data.csv'
    hostname = '11 Com'
    particle_system = three_body_system
    title = 'test_sample.gif'
    update = False

    if update:
        processor = DataProcessor(NASA_DATABASE_API_KEY)
        processor.update_data()

    if hostname is not None:
        particle_system_creator = ParticleSystemCreator(hostname)
        particle_system = particle_system_creator.create_particle_system()

    simulation = Simulation(particle_system, title)

    simulation.start()
