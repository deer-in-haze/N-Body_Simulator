from settings import Settings


class FigureSettings(Settings):
    class Builder():
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
            return self

        def set_background(self, background):
            self.__background = background
            return self

        def set_edge_colour(self, edge_colour):
            self.__edge_colour = edge_colour
            return self

        def set_plot_colour(self, plot_colour):
            self.__plot_colour = plot_colour
            return self

        def set_particle_colour(self, particle_colour):
            self.__particle_colour = particle_colour
            return self

        def set_custom_colours(self, custom_colours):
            self.__custom_colours = custom_colours
            return self

        def set_custom_sizes(self, custom_sizes):
            self.__custom_sizes = custom_sizes
            return self

        def set_line_weight(self, line_weight):
            self.__line_weight = line_weight
            return self

        def set_line_colour(self, line_colour):
            self.__line_colour = line_colour
            return self

        def set_line_style(self, line_style):
            self.__line_style = line_style
            return self

        def set_line_custom_colours(self, line_custom_colours):
            self.__line_custom_colours = line_custom_colours
            return self

        def build(self):
            return FigureSettings(self.__fig_size,
                                  self.__background,
                                  self.__edge_colour,
                                  self.__plot_colour,
                                  self.__particle_colour,
                                  self.__custom_colours,
                                  self.__custom_sizes,
                                  self.__line_weight,
                                  self.__line_colour,
                                  self.__line_style,
                                  self.__line_custom_colours)

    def __init__(self, fig_size, background, edge_colour, plot_colour, particle_colour, custom_colours, custom_sizes,
                 line_weight, line_colour, line_style, line_custom_colours):
        self.__fig_size = fig_size
        self.__background = background
        self.__edge_colour = edge_colour
        self.__plot_colour = plot_colour
        self.__particle_colour = particle_colour
        self.__custom_colours = custom_colours
        self.__custom_sizes = custom_sizes
        self.__line_weight = line_weight
        self.__line_colour = line_colour
        self.__line_style = line_style
        self.__line_custom_colours = line_custom_colours

    def get_fig_size(self):
        return self.__fig_size

    def get_background(self):
        return self.__background

    def get_edge_colour(self):
        return self.__edge_colour

    def get_plot_colour(self):
        return self.__plot_colour

    def get_particle_colour(self):
        return self.__particle_colour

    def get_custom_colours(self):
        return self.__custom_colours

    def get_custom_sizes(self):
        return self.__custom_sizes

    def get_line_weight(self):
        return self.__line_weight

    def get_line_colour(self):
        return self.__line_colour

    def get_line_style(self):
        return self.__line_style

    def get_line_custom_colours(self):
        return self.__line_custom_colours

    def display(self):
        pass
