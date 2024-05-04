import pytest
from figure_settings import FigureSettings


def test_figure_settings_builder():
    settings = FigureSettings.Builder() \
        .set_fig_size((10, 10)) \
        .set_background('white') \
        .set_edge_colour('blue') \
        .set_plot_colour('green') \
        .set_particle_colour('red') \
        .set_custom_colours(['red', 'green']) \
        .set_custom_sizes([5, 10]) \
        .set_line_weight(2) \
        .set_line_colour('yellow') \
        .set_line_style('dashed') \
        .set_line_custom_colours(['blue', 'black']) \
        .build()

    assert settings.get_fig_size() == (10, 10)
    assert settings.get_background() == 'white'
    assert settings.get_edge_colour() == 'blue'
    assert settings.get_plot_colour() == 'green'
    assert settings.get_particle_colour() == 'red'
    assert settings.get_custom_colours() == ['red', 'green']
    assert settings.get_custom_sizes() == [5, 10]
    assert settings.get_line_weight() == 2
    assert settings.get_line_colour() == 'yellow'
    assert settings.get_line_style() == 'dashed'
    assert settings.get_line_custom_colours() == ['blue', 'black']


def test_figure_settings_initialization():
    settings = FigureSettings((8, 8), 'grey', 'orange', 'black', 'white', ['purple', 'brown'], [3, 6],
                              3, 'silver', 'dot', ['gold', 'platinum'])

    assert settings.get_fig_size() == (8, 8)
    assert settings.get_background() == 'grey'
    assert settings.get_edge_colour() == 'orange'
    assert settings.get_plot_colour() == 'black'
    assert settings.get_particle_colour() == 'white'
    assert settings.get_custom_colours() == ['purple', 'brown']
    assert settings.get_custom_sizes() == [3, 6]
    assert settings.get_line_weight() == 3
    assert settings.get_line_colour() == 'silver'
    assert settings.get_line_style() == 'dot'
    assert settings.get_line_custom_colours() == ['gold', 'platinum']
