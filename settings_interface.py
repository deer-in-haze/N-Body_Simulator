import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
from figure_settings import FigureSettingsBuilder


class SettingsWindow:
    def __init__(self, master, on_settings_applied=None):
        self.master = master
        self.master.title("Settings")
        self.on_settings_applied = on_settings_applied

        self.custom_settings = None

        self.__background = 'black'
        self.__particle_colour = 'white'
        self.__edge_colour = 'black'
        self.__plot_colour = 'black'
        self.__line_colour = 'white'

        self.create_widgets()

    def create_widgets(self):
        # Background color selection
        ttk.Label(self.master, text="Background Color:").pack(pady=(10, 0))
        self.background_display = ttk.Label(self.master, background="white", width=20)
        self.background_display.pack()
        self.background_button = ttk.Button(self.master, text="Choose Color", command=self.choose_background)
        self.background_button.pack()

        # Particle color selection
        ttk.Label(self.master, text="Particle Colour:").pack(pady=(10, 0))
        self.particle_colour_display = ttk.Label(self.master, background="white", width=20)
        self.particle_colour_display.pack()
        self.particle_colour_button = ttk.Button(self.master, text="Choose Color", command=self.choose_particle_colour)
        self.particle_colour_button.pack()

        ttk.Label(self.master, text="Edge Colour:").pack(pady=(10, 0))
        self.edge_colour_display = ttk.Label(self.master, background="white", width=20)
        self.edge_colour_display.pack()
        self.edge_colour_button = ttk.Button(self.master, text="Choose Color", command=self.choose_edge_colour())
        self.edge_colour_button.pack()

        ttk.Label(self.master, text="Plot Colour:").pack(pady=(10, 0))
        self.plot_colour_display = ttk.Label(self.master, background="white", width=20)
        self.plot_colour_display.pack()
        self.plot_colour_button = ttk.Button(self.master, text="Choose Color", command=self.choose_plot_colour())
        self.plot_colour_button.pack()

        # Apply and Cancel buttons
        self.apply_button = ttk.Button(self.master, text="Apply", command=self.apply_settings)
        self.apply_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.cancel_button = ttk.Button(self.master, text="Cancel", command=self.cancel_settings)
        self.cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def choose_background(self):
        colour = colorchooser.askcolor(title="Choose Background Color")
        if colour[1]:  # Check if a color was chosen
            self.__background = colour[1]
            self.background_display.configure(background=self.__background)

    def choose_particle_colour(self):
        colour = colorchooser.askcolor(title="Choose Particle Color")
        if colour[1]:  # Check if a color was chosen
            self.__particle_colour = colour[1]
            self.particle_colour_display.configure(background=self.__particle_colour)

    def choose_edge_colour(self):
        colour = colorchooser.askcolor(title="Choose Edge Colour")
        if colour[1]:
            self.__edge_colour = colour[1]
            self.edge_colour_display.configure(background=self.__edge_colour)

    def choose_plot_colour(self):
        colour = colorchooser.askcolor(title="Choose Edge Colour")
        if colour[1]:
            self.__plot_colour = colour[1]
            self.plot_colour_display.configure(background=self.__plot_colour)

    def apply_settings(self):
        figure_settings = FigureSettingsBuilder().set_background(self.__background).set_particle_colour(
            self.__particle_colour).set_edge_colour(self.__edge_colour).build()
        self.custom_settings = figure_settings
        if self.on_settings_applied:
            self.on_settings_applied(self.custom_settings)
        messagebox.showinfo("Settings Applied", "Settings have been applied successfully.")
        self.master.destroy()

    def cancel_settings(self):
        self.master.destroy()

        '''
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
        '''
