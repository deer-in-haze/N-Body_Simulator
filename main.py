import sys
from simulation import Simulation
from particle_systems import three_body_system
from dataframe import Data, PlanetSystemData
from calculations import OrbitalVelocity
from particles import Particles

if __name__ == '__main__':
    data_path = '/home/migle/PycharmProjects/n_body_simulator/nasa_exoplanet_data.csv'
    host_name = 'GJ 1148'
    particle_system = three_body_system
    title = 'test_sample.gif'

    if host_name is not None:
        data = Data(data_path)
        data.read_data()
        data.clean_data()
        data.group_data()
        group_data = data.get_group(host_name)
        if data.has_missing_values:
            print(f'{host_name} system is missing some data, please choose a different host star.')
            sys.exit(1)
        planet_system_data = PlanetSystemData(group_data)
        planet_system_data.get_planet_data()
        calc = OrbitalVelocity(planet_system_data)
        calc.calculate_orbital_velocity()
        particles_from_system = Particles()
        particles_from_system.create_particles(planet_system_data, calc)
        particle_system = particles_from_system.particle_list

    simulation = Simulation(particle_system, title)

    simulation.start()
