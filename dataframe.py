import pandas as pd
from calculations import OrbitalVelocity


class Data:
    def __init__(self, path):
        self.path = path
        self.df = None
        self.column_names = []
        self.planet_system = None

    def read_data(self):
        self.df = pd.read_csv(self.path, skiprows=16)
        self.df['rowupdate'] = pd.to_datetime(self.df['rowupdate'])  # changing to datetime format
        print(self.df)

    def clean_data(self):
        most_recent_data_index = self.df.groupby('pl_name')['rowupdate'].idxmax()
        self.df = self.df.loc[most_recent_data_index]
        print(self.df)

    def group_data(self):
        grouped_data = self.df.groupby('hostname')
        print(grouped_data)
        return grouped_data

    def get_group(self, hostname):
        self.planet_system = self.group_data().get_group(hostname)
        return self.planet_system


data = Data('/home/migle/PycharmProjects/n_body_simulator/nasa_exoplanet_data.csv')
data.read_data()
data.clean_data()
data.group_data()

system = data.get_group('ups And')  # veliau pakeisiu


class PlanetSystemData:
    def __init__(self, planet_system):
        self.planet_system = planet_system
        self.host_star = self.planet_system.iloc[0, 1]
        self.host_mass = self.planet_system.iloc[0, 7]
        self.planet_count = self.planet_system.iloc[0, 3]
        self.planet_list = []
        self.planet_mass_list = []
        self.semi_major_axis_list = []
        self.orbital_period_list = []
        self.orbital_velocity_list = []
        self.particle_list = []
        self.system = {}

    def get_planet_data(self):
        for planet_name, planet_mass, a, T in zip(self.planet_system.loc[:, 'pl_name'],
                                                  self.planet_system.loc[:, 'pl_bmassj'],
                                                  self.planet_system.loc[:, 'pl_orbsmax'],
                                                  self.planet_system.loc[:, 'pl_orbper']):
            self.planet_list.append(planet_name)
            self.planet_mass_list.append(planet_mass)
            self.semi_major_axis_list.append(a)
            self.orbital_period_list.append(T)

        print(self.planet_count)
        print(self.host_star)
        print(self.host_mass)
        print(self.planet_list)
        print(self.semi_major_axis_list)
        print(self.orbital_period_list)
        print(self.planet_mass_list)


planet_system_data = PlanetSystemData(system)
planet_system_data.get_planet_data()
calc = OrbitalVelocity(planet_system_data)
calc.calculate_orbital_velocity()
