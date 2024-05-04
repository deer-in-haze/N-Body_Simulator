import pytest
from unittest.mock import Mock
from particles import Particles, CelestialBody, Particle
from constants import MASS_SUN
import numpy as np


@pytest.fixture
def setup_particles():
    particles = Particles()
    return particles


def test_create_particles(setup_particles):
    particles = setup_particles
    planet_system_data = Mock()
    orbital_velocity_instance = Mock()

    # Setting mock returns
    planet_system_data.get_host_mass.return_value = 1
    planet_system_data.get_planet_count.return_value = 2
    planet_system_data.get_planet_mass_list.return_value = [1 * MASS_SUN, 0.5 * MASS_SUN]
    planet_system_data.get_position_list.return_value = [[1, 0], [2, 0]]
    orbital_velocity_instance.get_velocity_list.return_value = [[0, 1], [0, 2]]

    expected_masses = [1 * MASS_SUN, 1 * MASS_SUN, 0.5 * MASS_SUN]
    expected_positions = [[0, 0], [1, 0], [2, 0]]
    expected_velocities = [[0, 0], [0, 1], [0, 2]]

    particles.create_particles(planet_system_data, orbital_velocity_instance)

    for i, particle in enumerate(particles.get_particle_list()):
        assert particle.get_mass() == expected_masses[i]
        assert particle.get_position() == expected_positions[i]
        assert particle.get_velocity() == expected_velocities[i]


def test_add_particle(setup_particles):
    particles = setup_particles
    new_particle = CelestialBody(0.3 * MASS_SUN, [0.5, 0.5], [0.2, 0.2])

    particles.add_particle(new_particle)

    assert particles.get_mass_list()[-1] == 0.3 * MASS_SUN
    assert np.all(particles.get_position_list()[-1] == [0.5, 0.5])
    assert np.all(particles.get_velocity_list()[-1] == [0.2, 0.2])
    assert np.all(particles.get_acceleration_list()[-1] == [0, 0])  # Expected to be zeros initially
