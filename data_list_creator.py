from constants import DAY, MASS_EARTH, AU
from decorators import status_update


class DataListCreator:
    def __init__(self, grouped_data, hostname):
        self.grouped_data = grouped_data
        self.hostname = hostname
        self.planet_system = None
        self.host_star = None
        self.host_mass = None
        self.planet_count = None
        self.planet_name_list = []
        self.planet_mass_list = []
        self.semi_major_axis_list = []
        self.position_list = []
        self.orbital_period_list = []
        self.orbital_velocity_list = []
        self.particle_list = []
        self.system = {}

    @status_update
    def get_group(self):
        self.planet_system = self.grouped_data.get_group(self.hostname)
        self.host_star = self.planet_system.iloc[0, 1]
        self.host_mass = self.planet_system.iloc[0, 7]
        self.planet_count = len(self.planet_system)

    @status_update
    def append_data_lists(self):
        for planet_name, planet_mass, semi_major_axis, orbital_period in zip(self.planet_system.loc[:, 'pl_name'],
                                                                             self.planet_system.loc[:, 'pl_bmassj'],
                                                                             self.planet_system.loc[:, 'pl_orbsmax'],
                                                                             self.planet_system.loc[:, 'pl_orbper']):
            self.planet_name_list.append(planet_name)
            self.planet_mass_list.append(planet_mass * MASS_EARTH)
            self.semi_major_axis_list.append(semi_major_axis * AU)
            self.position_list.append([semi_major_axis * AU, 0])
            self.orbital_period_list.append(orbital_period * DAY)

    @status_update
    def create_data_list(self):
        self.get_group()
        self.append_data_lists()
