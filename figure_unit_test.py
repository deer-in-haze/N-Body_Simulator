import numpy as np
import matplotlib.pyplot as plt
import pytest
from unittest.mock import Mock
from figure import Figure


@pytest.fixture
def mock_particle_list():
    mock = Mock()
    mock.get_mass_list.return_value = np.array([1, 10, 100, 1000])
    mock.get_position_list.return_value = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])
    return mock


@pytest.fixture
def mock_limits():
    mock = Mock()
    mock.get_limit.return_value = 5
    return mock


@pytest.fixture
def mock_figure_settings():
    mock = Mock()
    mock.get_background.return_value = 'black'
    mock.get_edge_colour.return_value = 'white'
    mock.get_plot_colour.return_value = 'gray'
    mock.get_particle_colour.return_value = 'blue'
    mock.get_custom_colours.return_value = None
    mock.get_custom_sizes.return_value = None
    mock.get_line_weight.return_value = 2
    mock.get_line_colour.return_value = 'yellow'
    mock.get_line_style.return_value = '--'
    mock.get_line_custom_colours.return_value = None
    mock.get_fig_size.return_value = (8, 8)
    return mock


def test_figure_initialization(mock_particle_list, mock_limits, mock_figure_settings):
    fig = Figure(mock_particle_list, mock_limits, mock_figure_settings)
    assert fig.get_figure() is not None
    assert fig.get_scatter() is None
    assert fig.get_lines() == []


def test_plot_figure(mock_particle_list, mock_limits, mock_figure_settings):
    fig = Figure(mock_particle_list, mock_limits, mock_figure_settings)
    fig.plot_figure()
    assert fig.get_scatter() is not None
    assert len(fig.get_lines()) == len(mock_particle_list.get_position_list())
    plt.close(fig.get_figure())
