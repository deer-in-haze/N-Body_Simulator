import pandas as pd


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
        print(self.planet_system)

