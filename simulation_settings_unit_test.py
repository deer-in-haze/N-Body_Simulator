import pytest
from simulation import SimulationSettings
from constants import GRAVITY_CONST, DAY


def test_simulation_settings_builder_initialization():
    settings = SimulationSettings.Builder().build()

    assert settings.get_gravity_const() == GRAVITY_CONST
    assert settings.get_softening() == 0.1
    assert settings.get_step_size() == DAY
    assert settings.get_half_step_size() == 0.5 * DAY


def test_simulation_settings_builder_customization():
    custom_gravity_const = 9.81
    custom_step_size = 3600
    custom_softening = 0.05

    settings = SimulationSettings.Builder() \
        .set_gravity_const(custom_gravity_const) \
        .set_step_size(custom_step_size) \
        .set_softening(custom_softening) \
        .build()

    assert settings.get_gravity_const() == custom_gravity_const
    assert settings.get_softening() == custom_softening
    assert settings.get_step_size() == custom_step_size
    assert settings.get_half_step_size() == 0.5 * custom_step_size


def test_simulation_settings_consistency():
    step_sizes = [DAY, 2 * DAY, 10 * DAY]
    for step_size in step_sizes:
        settings = SimulationSettings.Builder().set_step_size(step_size).build()
        assert settings.get_half_step_size() == 0.5 * step_size

