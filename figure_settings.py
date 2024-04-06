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
