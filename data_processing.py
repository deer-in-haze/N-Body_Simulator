import pandas as pd
import requests
from constants import DATA_FOLDER, ORIGINAL_DATA_FILENAME, CLEAN_DATA_FILENAME
from decorators import status_update, singleton


@singleton
class DataProcessor:
    def __init__(self, api_url):
        self.api_url = api_url
        self.destination_path = DATA_FOLDER
        self.original_file_name = ORIGINAL_DATA_FILENAME
        self.cleaned_file_name = CLEAN_DATA_FILENAME
        self.original_data = None
        self.clean_data = None
        self.grouped_data = None
        self.df = None

    @status_update
    def fetch_data(self):
        response = requests.get(self.api_url)
        self.original_data = response.content

    @status_update
    def delete_outdated_data(self):
        self.df['rowupdate'] = pd.to_datetime(self.df['rowupdate'])
        most_recent_data_index = self.df.groupby('pl_name')['rowupdate'].idxmax()
        self.df = self.df.loc[most_recent_data_index]

    @status_update
    def analyse_data(self):
        has_missing_values = self.df.isna().any().any()
        print(f'Dataframe has missing values: {has_missing_values}')
        rows_with_missing_data = self.df[self.df.isna().any(axis=1)]
        planets_with_missing_data = rows_with_missing_data['pl_name']
        print(f'Planets with incomplete data: {len(planets_with_missing_data)}')

    @status_update
    def handle_missing_data(self):
        has_missing_values = self.df.isna().any().any()
        if has_missing_values:
            self.df.dropna(inplace=True)

    def group_data(self):
        return self.df.groupby('hostname')

    @status_update
    def save_data(self, option):
        if option == "original":
            with open(self.destination_path + self.original_file_name, 'wb') as file:
                file.write(self.original_data)
        elif option == "df":
            self.df.to_csv(self.destination_path + self.cleaned_file_name, index=False)

    @status_update
    def load_data(self, option):
        if option == "original":
            self.df = pd.read_csv(self.destination_path + self.original_file_name)
        elif option == "clean":
            self.df = pd.read_csv(self.destination_path + self.cleaned_file_name)

    @status_update
    def update_data(self):
        self.fetch_data()
        self.save_data("original")
        self.load_data("original")
        self.analyse_data()
        self.delete_outdated_data()
        self.handle_missing_data()
        self.analyse_data()
        self.save_data("df")
