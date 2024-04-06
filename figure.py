import matplotlib.pyplot as plt
import numpy as np

from constants import AU
from decorators import status_update


class Figure:
    def __init__(self, particle_list, figure_settings):
        self.figure = plt.figure(figsize=figure_settings.fig_size)
        self.scatter = None
        self.lines = []
        self.position_list = particle_list.position_list
        self.mass_list = particle_list.mass_list

        self._xlim = [-2 * AU, 2 * AU]
        self._ylim = [-2 * AU, 2 * AU]

        self.background = figure_settings.background
        self.edge_colour = figure_settings.edge_colour
        self.plot_colour = figure_settings.plot_colour
        self.particle_colour = figure_settings.particle_colour
        self.custom_colours = figure_settings.custom_colours
        self.size = np.log10(self.mass_list)
        self.sizes = figure_settings.custom_sizes
        self.line_weight = figure_settings.line_weight
        self.line_colour = figure_settings.line_colour
        self.line_style = figure_settings.line_style
        self.line_custom_colours = figure_settings.line_custom_colours

    @status_update
    def plot_figure(self):
        self.figure = plt.figure()
        self.figure.patch.set_facecolor(self.background)
        axes = plt.axes(xlim=self._xlim, ylim=self._ylim)
        axes.set_aspect(1)
        axes.set_facecolor(self.plot_colour)
        self.scatter = axes.scatter(self.position_list[:, 0], self.position_list[:, 1], s=self.size, color=self.particle_colour,
                                    edgecolors=self.edge_colour, lw=self.line_weight)

        for pos in self.position_list:
            line, = axes.plot(pos[0], pos[1], color=self.line_colour, linestyle=self.line_style, linewidth=self.line_weight)
            self.lines.append(line)