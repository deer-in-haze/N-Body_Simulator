import matplotlib.pyplot as plt

from constants import AU
from decorators import status_update


class Figure:
    def __init__(self, particle_list):
        self.figure = plt.figure(figsize=(5, 5))
        self.scatter = None
        self.position_list = particle_list.position_list
        self.mass_list = particle_list.mass_list
        self._xlim = [-2 * AU, 2 * AU]
        self._ylim = [-2 * AU, 2 * AU]
        self.background = 'black'
        self.particle_colour = 'white'
        self.edge_colour = 'black'
        self.plot_colour = 'black'
        self.line_weight = 1
        self.lines = []  # Added lines attribute to hold trajectory lines
        self.colours = ['white', 'white', 'white']
        self.sizes = [1e2, 1e2, 1e2]

    @status_update
    def plot_figure(self):
        self.figure = plt.figure()
        self.figure.patch.set_facecolor(self.background)
        axes = plt.axes(xlim=self._xlim, ylim=self._ylim)
        axes.set_aspect(1)
        axes.set_facecolor(self.plot_colour)
        self.scatter = axes.scatter(self.position_list[:, 0], self.position_list[:, 1], s=self.sizes, c=self.colours,
                                    edgecolors=self.edge_colour, lw=self.line_weight)

        for pos in self.position_list:
            line, = axes.plot(pos[0], pos[1], color='white', linestyle='-', linewidth=1)
            self.lines.append(line)

        for pos, color, size in zip(self.position_list, self.colours, self.sizes):
            line, = axes.plot(pos[0], pos[1], color=color, linestyle='-', linewidth=size / 10)
            self.lines.append(line)