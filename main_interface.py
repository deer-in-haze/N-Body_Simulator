import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from simulation import Simulation
from particle_systems import three_body_system, binary_system, earth_system, inner_solar_system, particle_list
from constants import hostname_options, SIMULATIONS_FOLDER
from particle_system_creator import ParticleSystemCreator
from data_processing import NASADataProcessor
from constants import NASA_DATABASE_API_KEY, DAY, HOUR, MIN, SMALL_MASS_TIMESTEP
from simulation_settings import SimulationSettings
from figure_settings import FigureSettings




class MainApplication:
    def __init__(self, master):

        self.style = ttk.Style()
        self.style.configure("TCombobox", foreground="black")
        self.master = master
        self.master.configure(bg="black")
        self.master.title("N-Body Simulator")
        self.master.geometry("400x450")
        self.create_widgets()

    def create_widgets(self):

        tk.Label(self.master, text="Hostname:", bg="black", fg="white", ).pack(pady=(10, 0))
        self.hostname_combobox = ttk.Combobox(self.master, values=hostname_options, width=37, state="readonly")
        self.hostname_combobox.pack()
        self.hostname_combobox.set('Select hostname')

        tk.Label(self.master, text="OR", bg="black", fg="white").pack()

        tk.Label(self.master, text="Particle system:", bg="black", fg="white").pack()
        particle_system_options = ['Select particle system','Three body system', 'Binary system', 'Earth system', 'Inner solar system',
                                   '9 particles']
        self.particle_system_combobox = ttk.Combobox(self.master, values=particle_system_options, width=37, state="readonly")
        self.particle_system_combobox.pack(pady=5)
        self.particle_system_combobox.set('Select particle system')

        tk.Label(self.master, text="Time step:", bg="black", fg="white").pack(pady=(30, 0))
        time_step_options = ['Day', 'Hour', 'Minute', '20 ms']
        self.time_step_combobox = ttk.Combobox(self.master, values=time_step_options, width=37, state="readonly")
        self.time_step_combobox.pack()
        self.time_step_combobox.set('Select time step')

        tk.Label(self.master, text="Gravity constant:", bg="black", fg="white").pack()
        gravity_constant_options = ['6.67e-11', '0.001']
        self.gravity_constant_combobox = ttk.Combobox(self.master, values=gravity_constant_options, width=37, state="readonly")
        self.gravity_constant_combobox.pack()
        self.gravity_constant_combobox.set('Select gravity constant')

        tk.Label(self.master, text="Animation length:", bg="black", fg="white").pack()
        self.animation_length_entry = tk.Entry(self.master, width=40)
        self.animation_length_entry.pack()
        self.animation_length_entry.insert(0, '4')

        tk.Label(self.master, text="Title:", bg="black", fg="white").pack()
        self.title_entry = tk.Entry(self.master, width=40)
        self.title_entry.pack()
        self.title_entry.insert(0, 'test_sample.gif')

        self.update_var = tk.IntVar()
        update_check = tk.Checkbutton(self.master, text="Update Data", bg="black", fg="white", variable=self.update_var, selectcolor="black", highlightbackground="black", activebackground="black", activeforeground="white")
        update_check.pack()


        start_button = tk.Button(self.master, text="Start Simulation", bg="black", fg="white", command=self.run_simulation, highlightbackground="black", activebackground="white", activeforeground="black")
        start_button.pack()

    def validate_hostname(self):
        hostname = self.hostname_combobox.get()
        particle_system = self.particle_system_combobox.get()
        if hostname == 'Select hostname' and particle_system == 'Select particle system':
            messagebox.showerror("Error", "Hostname and particle system cannot be empty")
            return False
        elif hostname != 'Select hostname' and particle_system != 'Select particle system':
            messagebox.showerror("Error", "Please choose either hostname or particle system")
            return False
        return True

    def validate_step_size(self):
        step_size = self.time_step_combobox.get()
        if step_size == 'Select time step':
            messagebox.showerror("Error", "Time step cannot be empty")
            return False
        return True


    def validate_animation_length(self):
        animation_length = self.animation_length_entry.get()
        if not animation_length.isdigit():
            messagebox.showerror("Error", "Animation length must be a valid integer")
            return False
        elif int(animation_length) <= 0:
            messagebox.showerror("Error", "Animation length must be greater than 0")
            return False
        elif not animation_length:
            messagebox.showerror("Error", "Animation length cannot be empty")
            return False
        return True

    def validate_gravity_constant(self):
        gravity_constant = self.gravity_constant_combobox.get()
        if gravity_constant == 'Select gravity constant':
            messagebox.showerror("Error", "Gravity constant cannot be empty")
            return False
        return True

    def validate_title(self):
        title = self.title_entry.get()
        if not title:
            messagebox.showerror("Error", "Title cannot be empty")
            return False
        elif ".gif" not in title:
            messagebox.showerror("Error", "Title must have .gif extension")
            return False
        return True

    def run_simulation(self):
        if not self.validate_hostname():
            return
        if not self.validate_step_size():
            return
        if not self.validate_gravity_constant():
            return
        if not self.validate_animation_length():
            return
        if not self.validate_title():
            return

        hostname = self.hostname_combobox.get()
        particle_system = self.particle_system_combobox.get()
        time_step = self.time_step_combobox.get()
        gravity_constant = self.gravity_constant_combobox.get()
        animation_length = int(self.animation_length_entry.get())
        title = self.title_entry.get()
        update = self.update_var.get()

        if update:
            processor = NASADataProcessor(NASA_DATABASE_API_KEY)
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

        if hostname != "Select hostname":
            particle_system_creator = ParticleSystemCreator(hostname)
            particle_system = particle_system_creator.create_particle_system()

        if time_step == 'Day':
            step_size = DAY
        elif time_step == 'Hour':
            step_size = HOUR
        elif time_step == 'Minute':
            step_size = MIN
        elif time_step == '20 ms':
            step_size = SMALL_MASS_TIMESTEP

        if gravity_constant == "0.001":
            gravity_const = 0.001
        elif gravity_constant == "6.67e-11":
            gravity_const = 6.67e-11

        frames = int(animation_length / 0.02)
        simulation = Simulation(particle_system, step_size, gravity_const, frames, title)
        simulation.start()

        messagebox.showinfo("Simulation", "Simulation is complete!")
        self.open_gif_window(SIMULATIONS_FOLDER + title)


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

