"""MATHEMATICAL"""
PI = 3.14159265359

"""ASTRONOMICAL"""
AU = 1.496e11  # astronomical unit
GRAVITY_CONST = 6.67e-11
MASS_SUN = 1.988e30
MASS_JUPITER = 1.898e27
MASS_EARTH = 5.972e24

"""TIMESTEP"""
DAY = 86400  # [s]
HOUR = DAY / 24
MIN = HOUR / 60

SMALL_MASS_TIMESTEP = 20 / 1000

"""MISCELLANEOUS"""
OFFSET = 0

"""APIs"""
NASA_DATABASE_API_KEY = ("https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,sy_snum,"
                         "sy_pnum,pl_orbper,pl_orbsmax,pl_bmassj,st_mass,rowupdate+from+ps&format=csv")
"""PATHS"""
DATA_FOLDER = '/home/migle/PycharmProjects/n_body_simulator/DATA/'

"""FILENAMES"""
ORIGINAL_DATA_FILENAME = 'original_data.csv'
CLEAN_DATA_FILENAME = 'clean_data.csv'
