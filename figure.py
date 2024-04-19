import matplotlib.pyplot as plt
import numpy as np
from decorators import status_update


class Figure:
    def __init__(self, particle_list, limits, figure_settings):
        self.__background = figure_settings.get_background()
        self.__edge_colour = figure_settings.get_edge_colour()
        self.__plot_colour = figure_settings.get_plot_colour()
        self.__particle_colour = figure_settings.get_particle_colour()
        self.__custom_colours = figure_settings.get_custom_colours()
        self.__size = np.log2(particle_list.get_mass_list())
        self.__sizes = figure_settings.get_custom_sizes()
        self.__line_weight = figure_settings.get_line_weight()
        self.__line_colour = figure_settings.get_line_colour()
        self.__line_style = figure_settings.get_line_style()
        self.__line_custom_colours = figure_settings.get_line_custom_colours()

        self.__figure = plt.figure(figsize=figure_settings.get_fig_size())
        self.__scatter = None
        self.__lines = []
        self.__position_list = particle_list.get_position_list()

        self.__xlim = [-limits.get_limit(), limits.get_limit()]
        self.__ylim = [-limits.get_limit(), limits.get_limit()]

    def get_figure(self):
        return self.__figure

    def get_scatter(self):
        return self.__scatter

    def get_lines(self):
        return self.__lines

    def get_position_list(self):
        return self.__position_list


    @status_update
    def plot_figure(self):
        self.__figure = plt.figure()
        self.__figure.patch.set_facecolor(self.__background)
        axes = plt.axes(xlim=self.__xlim, ylim=self.__ylim)
        axes.set_aspect(1)
        axes.set_facecolor(self.__plot_colour)
        self.__scatter = axes.scatter(self.__position_list[:, 0],
                                      self.__position_list[:, 1],
                                      s=self.__size,
                                      color=self.__particle_colour,
                                      edgecolors=self.__edge_colour, lw=self.__line_weight)

        for pos in self.__position_list:
            line, = axes.plot(pos[0], pos[1],
                              color=self.__line_colour,
                              linestyle=self.__line_style,
                              linewidth=self.__line_weight)
            self.__lines.append(line)
