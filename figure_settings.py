class FigureSettings:
    def __init__(self, **kwargs):
        self.fig_size = kwargs.get('fig_size', (5, 5))
        self.background = kwargs.get('background', 'black')
        self.edge_colour = kwargs.get('edge_colour', 'black')
        self.plot_colour = kwargs.get('plot_colour', 'black')
        self.particle_colour = kwargs.get('particle_colour', 'white')
        self.custom_colours = kwargs.get('colour_list', None)
        self.custom_sizes = kwargs.get('size_list', None)
        self.line_weight = kwargs.get('line_weight', 1)
        self.line_colour = kwargs.get('line_colour', 'white')
        self.line_style = kwargs.get('line_style', '-')
        self.line_custom_colours = kwargs.get('line_custom_colours', None)

        self.particle_list = kwargs.get('particle_list', None)
        self.x_limit = kwargs.get('x_limit', None)
        self.y_limit = kwargs.get('y_limit', None)

    def calculate_limits(self):
        if self.x_limit is None or self.y_limit is None:
            max_distance = 0

            for i in range(len(self.particle_list.position_list)):
                for j in range(i + 1, len(self.particle_list.position_list)):

                    distance = ((self.particle_list.position_list[j][0] -
                                 self.particle_list.position_list[i][0]) ** 2 + (
                                self.particle_list.position_list[j][1] -
                                self.particle_list.position_list[i][1]) ** 2) ** 0.5
                    if distance > max_distance:
                        max_distance = distance

            self.x_limit = max_distance + max_distance * 0.1
            self.y_limit = max_distance + max_distance * 0.1
