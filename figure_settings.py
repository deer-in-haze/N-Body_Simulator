class FigureSettings:
    def __init__(self):
        self.__fig_size = (5, 5)
        self.__background = 'black'
        self.__edge_colour = 'black'
        self.__plot_colour = 'black'
        self.__particle_colour = 'white'
        self.__custom_colours = None
        self.__custom_sizes = None
        self.__line_weight = 1
        self.__line_colour = 'white'
        self.__line_style = '-'
        self.__line_custom_colours = None


    def set_fig_size(self, fig_size):
        self.__fig_size = fig_size

    def get_fig_size(self):
        return self.__fig_size

    def set_background(self, background):
        self.__background = background

    def get_background(self):
        return self.__background

    def set_edge_colour(self, edge_colour):
        self.__edge_colour = edge_colour

    def get_edge_colour(self):
        return self.__edge_colour

    def set_plot_colour(self, plot_colour):
        self.__plot_colour = plot_colour

    def get_plot_colour(self):
        return self.__plot_colour

    def set_particle_colour(self, particle_colour):
        self.__particle_colour = particle_colour

    def get_particle_colour(self):
        return self.__particle_colour

    def set_custom_colours(self, custom_colours):
        self.__custom_colours = custom_colours

    def get_custom_colours(self):
        return self.__custom_colours

    def set_custom_sizes(self, custom_sizes):
        self.__custom_sizes = custom_sizes

    def get_custom_sizes(self):
        return self.__custom_sizes

    def set_line_weight(self, line_weight):
        self.__line_weight = line_weight

    def get_line_weight(self):
        return self.__line_weight

    def set_line_colour(self, line_colour):
        self.__line_colour = line_colour

    def get_line_colour(self):
        return self.__line_colour

    def set_line_style(self, line_style):
        self.__line_style = line_style

    def get_line_style(self):
        return self.__line_style

    def set_line_custom_colours(self, line_custom_colours):
        self.__line_custom_colours = line_custom_colours

    def get_line_custom_colours(self):
        return self.__line_custom_colours


class FigureSettingsBuilder:
    def __init__(self):
        self.__settings = None
        self.__reset()

    def __reset(self):
        self.__settings = FigureSettings()
        return self

    def set_fig_size(self, size):
        self.__settings.set_fig_size(size)
        return self

    def get_fig_size(self):
        return self.__settings.get_fig_size()

    def set_background(self, background):
        self.__settings.set_background(background)
        return self

    def get_background(self):
        return self.__settings.get_background()

    def set_edge_colour(self, edge_colour):
        self.__settings.set_edge_colour(edge_colour)
        return self

    def get_edge_colour(self):
        return self.__settings.get_edge_colour()

    def set_plot_colour(self, plot_colour):
        self.__settings.set_plot_colour(plot_colour)
        return self

    def get_plot_colour(self):
        return self.__settings.get_plot_colour()

    def set_particle_colour(self, particle_colour):
        self.__settings.set_particle_colour(particle_colour)
        return self

    def get_particle_colour(self):
        return self.__settings.get_particle_colour()

    def set_custom_colours(self, custom_colours):
        self.__settings.set_custom_colours(custom_colours)
        return self

    def get_custom_colours(self):
        return self.__settings.get_custom_colours()

    def set_custom_sizes(self, custom_sizes):
        self.__settings.set_custom_sizes(custom_sizes)
        return self

    def get_custom_sizes(self):
        return self.__settings.get_custom_sizes()

    def set_line_weight(self, line_weight):
        self.__settings.set_line_weight(line_weight)
        return self

    def get_line_weight(self):
        return self.__settings.get_line_weight()

    def set_line_colour(self, line_colour):
        self.__settings.set_line_colour(line_colour)
        return self

    def get_line_colour(self):
        return self.__settings.get_line_colour()

    def set_line_style(self, line_style):
        self.__settings.set_line_style(line_style)
        return self

    def get_line_style(self):
        return self.__settings.get_line_style()

    def set_line_custom_colours(self, line_custom_colours):
        self.__settings.set_line_custom_colours(line_custom_colours)
        return self

    def get_line_custom_colours(self):
        return self.__settings.get_line_custom_colours()

    def build(self):
        return self.__settings
