from constants import DAY, MASS_EARTH, AU
from decorators import status_update


class DataListCreator:
    def __init__(self, grouped_data, hostname):
        self.__grouped_data = grouped_data
        self.__hostname = hostname
        self.__planet_system = None
        self.__host_star = None
        self.__host_mass = None
        self.__planet_count = None
        self.__planet_name_list = []
        self.__planet_mass_list = []
        self.__semi_major_axis_list = []
        self.__position_list = []
        self.__orbital_period_list = []
        self.__particle_list = []
        self.__host_mass = None

    def get_hostname(self):
        return self.__hostname

    def get_planet_system(self):
        return self.__planet_system

    def get_host_star(self):
        return self.__host_star

    def get_host_mass(self):
        return self.__host_mass

    def get_planet_count(self):
        return self.__planet_count

    def get_planet_name_list(self):
        return self.__planet_name_list

    def get_planet_mass_list(self):
        return self.__planet_mass_list

    def get_semi_major_axis_list(self):
        return self.__semi_major_axis_list

    def get_position_list(self):
        return self.__position_list

    def get_orbital_period_list(self):
        return self.__orbital_period_list

    def get_particle_list(self):
        return self.__particle_list

    @status_update
    def __get_group(self):
        self.__planet_system = self.__grouped_data.get_group(self.__hostname)
        self.__host_star = self.__planet_system.iloc[0, 1]
        self.__host_mass = self.__planet_system.iloc[0, 7]
        self.__planet_count = len(self.__planet_system)

    @status_update
    def __append_data_lists(self):
        for planet_name, planet_mass, semi_major_axis, orbital_period in zip(self.__planet_system.loc[:, 'pl_name'],
                                                                             self.__planet_system.loc[:, 'pl_bmassj'],
                                                                             self.__planet_system.loc[:, 'pl_orbsmax'],
                                                                             self.__planet_system.loc[:, 'pl_orbper']):
            self.__planet_name_list.append(planet_name)
            self.__planet_mass_list.append(planet_mass * MASS_EARTH)
            self.__semi_major_axis_list.append(semi_major_axis * AU)
            self.__position_list.append([semi_major_axis * AU, 0])
            self.__orbital_period_list.append(orbital_period * DAY)

    @status_update
    def create_data_list(self):
        self.__get_group()
        self.__append_data_lists()
