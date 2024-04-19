import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from simulation import Simulation
from particle_systems import three_body_system, binary_system, earth_system, inner_solar_system, particle_list
from particle_system_creator import ParticleSystemCreator
from data_processing import DataProcessor
from constants import NASA_DATABASE_API_KEY, DAY, HOUR, MIN, SMALL_MASS_TIMESTEP
from settings import Settings
from settings_interface import SettingsWindow
from figure_settings import FigureSettingsBuilder


class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("N-Body Simulator")
        self.master.geometry("400x500")
        self.create_widgets()
        self.custom_settings = None

    def create_widgets(self):

        tk.Label(self.master, text="Hostname:").pack()
        self.hostname_entry = tk.Entry(self.master, width=40)
        self.hostname_entry.pack()

        tk.Label(self.master, text="Particle system:").pack()
        particle_system_options = ['Three body system', 'Binary system', 'Earth system', 'Inner solar system',
                                   '9 particles']
        self.particle_system_combobox = ttk.Combobox(self.master, values=particle_system_options, width=37)
        self.particle_system_combobox.pack()
        self.particle_system_combobox.set('Select particle system')

        tk.Label(self.master, text="Time step:").pack()
        time_step_options = ['Day', 'Hour', 'Minute', '20 ms']
        self.time_step_combobox = ttk.Combobox(self.master, values=time_step_options, width=37)
        self.time_step_combobox.pack()
        self.time_step_combobox.set('Select time step')

        tk.Label(self.master, text="Gravity constant:").pack()
        gravity_constant_options = ['6.67e-11', '0.001']
        self.gravity_constant_combobox = ttk.Combobox(self.master, values=gravity_constant_options, width=37)
        self.gravity_constant_combobox.pack()
        self.gravity_constant_combobox.set('Select gravity constant')

        tk.Label(self.master, text="Animation length:").pack()
        self.animation_length_entry = tk.Entry(self.master, width=40)
        self.animation_length_entry.pack()
        self.animation_length_entry.insert(0, '4')

        tk.Label(self.master, text="Title:").pack()
        self.title_entry = tk.Entry(self.master, width=40)
        self.title_entry.pack()
        self.title_entry.insert(0, 'test_sample.gif')

        self.update_var = tk.IntVar()
        update_check = tk.Checkbutton(self.master, text="Update Data", variable=self.update_var)
        update_check.pack()

        settings_button = tk.Button(self.master, text="Open Settings", command=self.open_settings)
        settings_button.pack(pady=20, padx=20)

        start_button = tk.Button(self.master, text="Start Simulation", command=self.run_simulation)
        start_button.pack()

    def setup_default_settings(self):
        # Default settings for the simulation
        self.custom_settings = FigureSettingsBuilder().build()

    def open_settings(self):
        settings_window = tk.Toplevel(self.master)
        settings_app = SettingsWindow(settings_window, self.handle_new_settings)

    def handle_new_settings(self, settings):
        # Here you can handle the settings, e.g., store them, or pass them to other parts of the application
        self.custom_settings = settings

    def open_gif_window(self, gif_path):
        gif_window = tk.Toplevel(self.master)
        gif_window.title("Simulation Result")
        gif_image = Image.open(gif_path)
        gif_photo = ImageTk.PhotoImage(gif_image)

        gif_label = tk.Label(gif_window, image=gif_photo)
        gif_label.image = gif_photo
        gif_label.pack()

        self.animate_gif_in_window(gif_image, gif_label, gif_window)

    def animate_gif_in_window(self, gif_image, gif_label, gif_window, frame_num=0):
        try:
            gif_image.seek(frame_num)
            frame_photo = ImageTk.PhotoImage(gif_image.copy())
            gif_label.config(image=frame_photo)
            gif_label.image = frame_photo
            gif_window.after(20, self.animate_gif_in_window, gif_image, gif_label, gif_window, frame_num + 1)
        except EOFError:
            gif_image.seek(0)
            gif_window.after(20, self.animate_gif_in_window, gif_image, gif_label, gif_window, 0)

    def run_simulation(self):
        hostname = self.hostname_entry.get()
        particle_system = self.particle_system_combobox.get()
        time_step = self.time_step_combobox.get()
        gravity_constant = self.gravity_constant_combobox.get()
        animation_length = int(self.animation_length_entry.get())
        title = self.title_entry.get()
        update = self.update_var.get()

        if update:
            processor = DataProcessor(NASA_DATABASE_API_KEY)
            processor.update_data()

        if particle_system == 'Binary system':
            particle_system = binary_system
        elif particle_system == 'Three body system':
            particle_system = three_body_system
        elif particle_system == 'Earth system':
            particle_system = earth_system
        elif particle_system == 'Inner solar system':
            particle_system = inner_solar_system
        elif particle_system == '9 particles':
            particle_system = particle_list

        if hostname:
            particle_system_creator = ParticleSystemCreator(hostname)
            particle_system = particle_system_creator.create_particle_system()

        settings = Settings()
        if time_step == 'Day':
            settings.set_step_size(DAY)
        elif time_step == 'Hour':
            settings.set_step_size(HOUR)
        elif time_step == 'Minute':
            settings.set_step_size(MIN)
        elif time_step == '20 ms':
            settings.set_step_size(SMALL_MASS_TIMESTEP)

        if gravity_constant == "0.001":
            settings.set_gravity_const(0.001)
        elif gravity_constant == "6.67e-11":
            settings.set_gravity_const(6.67e-11)

        if self.custom_settings is None:
            self.setup_default_settings()

        frames = int(animation_length / 0.02)
        simulation = Simulation(particle_system, settings, self.custom_settings, frames, title)
        simulation.start()

        messagebox.showinfo("Simulation", "Simulation is complete!")
        self.open_gif_window(title)
