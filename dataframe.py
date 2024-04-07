import pandas as pd
from constants import DAY, MASS_SUN, MASS_EARTH, AU
from decorators import status_update


class Data:
    def __init__(self, path):
        self.path = path
        self.df = None
        self.column_names = []
        self.planet_system = None
        self.has_missing_values = False

    @status_update
    def read_data(self):
        self.df = pd.read_csv(self.path, skiprows=16)
        self.df['rowupdate'] = pd.to_datetime(self.df['rowupdate'])  # changing to datetime format

    @status_update
    def clean_data(self):
        most_recent_data_index = self.df.groupby('pl_name')['rowupdate'].idxmax()
        self.df = self.df.loc[most_recent_data_index]
        has_missing_values = self.df.isna().any().any()
        print(f'Dataframe has missing values: {has_missing_values}')
        rows_with_missing_data = self.df[self.df.isna().any(axis=1)]
        planets_with_missing_data = rows_with_missing_data['pl_name']
        print(f'Planets with incomplete data: {len(planets_with_missing_data)}')

    def group_data(self):
        grouped_data = self.df.groupby('hostname')
        return grouped_data

    def get_group(self, hostname):
        self.planet_system = self.group_data().get_group(hostname)
        self.has_missing_values = self.planet_system.isna().any().any()
        return self.planet_system


class PlanetSystemData:
    def __init__(self, planet_system):
        self.planet_system = planet_system
        self.host_star = self.planet_system.iloc[0, 1]
        self.host_mass = self.planet_system.iloc[0, 7]
        self.planet_count = self.planet_system.iloc[0, 3]
        self.planet_name_list = []
        self.planet_mass_list = []
        self.semi_major_axis_list = []
        self.position_list = []
        self.orbital_period_list = []
        self.orbital_velocity_list = []
        self.particle_list = []
        self.system = {}

    @status_update
    def get_planet_data(self):
        for planet_name, planet_mass, a, T in zip(self.planet_system.loc[:, 'pl_name'],
                                                  self.planet_system.loc[:, 'pl_bmassj'],
                                                  self.planet_system.loc[:, 'pl_orbsmax'],
                                                  self.planet_system.loc[:, 'pl_orbper']):
            self.planet_name_list.append(planet_name)
            self.planet_mass_list.append(planet_mass * MASS_EARTH)
            self.semi_major_axis_list.append(a * AU)
            self.position_list.append([a * AU, 0])
            self.orbital_period_list.append(T * DAY)
