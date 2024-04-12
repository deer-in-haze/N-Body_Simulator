import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from simulation import Simulation
from particle_systems import three_body_system, binary_system, earth_system, inner_solar_system, particle_list
from particle_system_creator import ParticleSystemCreator
from data_processing import DataProcessor
from constants import NASA_DATABASE_API_KEY, DAY, HOUR, MIN, SMALL_MASS_TIMESTEP
from settings import Settings


def run_interface():
    def start_simulation():
        hostname = hostname_entry.get()
        particle_system = particle_system_combobox.get()
        time_step = time_step_combobox.get()
        gravity_constant = gravity_constant_combobox.get()
        animation_length = int(animation_length_entry.get())
        title = title_entry.get()
        update = update_var.get()

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

        frames = int(animation_length / 0.02)
        simulation = Simulation(particle_system, settings, frames, title)
        simulation.start()

        messagebox.showinfo("Simulation", "Simulation is complete!")
        open_gif_window(title)

        settings.get_step_size()
        settings.get_half_step_size()

    def open_gif_window(gif_path):
        gif_window = tk.Toplevel(root)
        gif_window.title("Simulation Result")
        gif_image = Image.open(gif_path)
        gif_photo = ImageTk.PhotoImage(gif_image)

        gif_label = tk.Label(gif_window, image=gif_photo)
        gif_label.image = gif_photo
        gif_label.pack()

        animate_gif_in_window(gif_image, gif_label, gif_window)

    def animate_gif_in_window(gif_image, gif_label, gif_window, frame_num=0):
        try:
            gif_image.seek(frame_num)
            frame_photo = ImageTk.PhotoImage(gif_image.copy())
            gif_label.config(image=frame_photo)
            gif_label.image = frame_photo
            gif_window.after(20, animate_gif_in_window, gif_image, gif_label, gif_window, frame_num + 1)
        except EOFError:
            gif_image.seek(0)
            gif_window.after(20, animate_gif_in_window, gif_image, gif_label, gif_window, 0)

    root = tk.Tk()
    root.title("N-Body Simulation Interface")
    root.geometry("400x400")

    tk.Label(root, text="Hostname:").pack()
    hostname_entry = tk.Entry(root, width=40)
    hostname_entry.pack()

    tk.Label(root, text="Particle system:").pack()
    particle_system_options = ['Three body system', 'Binary system', 'Earth system', 'Inner solar system',
                               '9 particles']
    particle_system_combobox = ttk.Combobox(root, values=particle_system_options, width=37)
    particle_system_combobox.pack()
    particle_system_combobox.set('Select particle system')

    tk.Label(root, text="Time step:").pack()
    time_step_options = ['Day', 'Hour', 'Minute', '20 ms']
    time_step_combobox = ttk.Combobox(root, values=time_step_options, width=37)
    time_step_combobox.pack()
    time_step_combobox.set('Select time step')

    tk.Label(root, text="Gravity constant:").pack()
    gravity_constant_options = ['6.67e-11', '0.001']
    gravity_constant_combobox = ttk.Combobox(root, values=gravity_constant_options, width=37)
    gravity_constant_combobox.pack()
    gravity_constant_combobox.set('Select gravity constant')

    tk.Label(root, text="Animation length:").pack()
    animation_length_entry = tk.Entry(root, width=40)
    animation_length_entry.pack()
    animation_length_entry.insert(0, '4')

    tk.Label(root, text="Title:").pack()
    title_entry = tk.Entry(root, width=40)
    title_entry.pack()
    title_entry.insert(0, 'test_sample.gif')

    update_var = tk.IntVar()
    update_check = tk.Checkbutton(root, text="Update Data", variable=update_var)
    update_check.pack()

    start_button = tk.Button(root, text="Start Simulation", command=start_simulation)
    start_button.pack()

    root.mainloop()
