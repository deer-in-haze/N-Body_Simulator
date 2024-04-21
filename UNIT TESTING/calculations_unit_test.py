import pytest
import numpy as np
from unittest.mock import Mock
from calculations import Limits, CentreOfMass, Acceleration, OrbitalVelocity
from constants import PI


@pytest.fixture(params=[
    (np.array([[1, 2], [3, 4], [0, 0]]), 5.0 * 1.1),
    (np.array([[-1, -2], [-3, -4], [0, 0]]), 5.0 * 1.1),
    (np.array([[0, 0], [0, 0], [0, 0]]), 0 * 1.1)
])
def particle_list_and_limit(request):
    return request.param


def test_calculate_limits(particle_list_and_limit):
    position_list, expected_limit = particle_list_and_limit
    mock_particle_list = Mock()
    mock_particle_list.get_position_list.return_value = position_list
    limits = Limits(mock_particle_list)
    limits.calculate_limits()
    assert abs(limits.get_limit()) == expected_limit


@pytest.fixture
def particle_list_mock():
    mock = Mock()
    mock.get_mass_list.return_value = np.array([500, 500])
    mock.get_position_list.return_value = np.array([[-3., 3.], [-3., 0.]])
    mock.get_velocity_list.return_value = np.array([[0., 0.], [0., 0.]])
    return mock


def test_centre_positions_and_velocities(particle_list_mock):
    com = CentreOfMass(particle_list_mock)
    com.centre_positions_and_velocities()

    expected_positions = np.array([[0., 1.5], [0., -1.5]])
    expected_velocities = np.array([[0., 0.], [0., 0.]])

    np.testing.assert_array_almost_equal(com.get_position_list(), expected_positions)
    np.testing.assert_array_almost_equal(com.get_velocity_list(), expected_velocities)


@pytest.fixture
def setup_acceleration():
    particle_list = Mock()
    particle_list.get_mass_list.return_value = np.array([500, 500])
    particle_list.get_position_list.return_value = np.array([[-3, 3], [-3, 0]])
    particle_list.get_velocity_list.return_value = np.array([[0, 0], [0, 0]])

    settings = Mock()
    settings.get_softening.return_value = 0.1
    settings.get_gravity_const.return_value = 0.001  # Gravitational constant

    acceleration = Acceleration(particle_list, settings)
    return acceleration


def test_acceleration_calculation(setup_acceleration):
    acc = setup_acceleration
    result = acc.acceleration_calculation()

    expected = np.array([0., 0., -0.05546, 0.05546])

    np.testing.assert_array_almost_equal(result, expected, decimal=5)


@pytest.fixture
def setup_orbital_velocity():
    planet_system_data = Mock()
    planet_system_data.get_planet_count.return_value = 3
    planet_system_data.get_semi_major_axis_list.return_value = [1, 5, 10]
    planet_system_data.get_orbital_period_list.return_value = [1, 2, 5]

    orbital_velocity = OrbitalVelocity(planet_system_data)
    return orbital_velocity


def test_calculate_orbital_velocity(setup_orbital_velocity):
    ov = setup_orbital_velocity
    ov.calculate_orbital_velocity()

    expected_velocities = [
        [0, 2 * PI * 1 / 1],
        [0, 2 * PI * 5 / 2],
        [0, 2 * PI * 10 / 5]
    ]

    calculated_velocities = ov.get_velocity_list()
    assert calculated_velocities == expected_velocities
