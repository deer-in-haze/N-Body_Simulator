from simulation import Simulation
from particle_systems import three_body_system

if __name__ == '__main__':

    title = 'test_sample.gif'
    particle_system = three_body_system

    simulation = Simulation(particle_system, title)

    simulation.start()





