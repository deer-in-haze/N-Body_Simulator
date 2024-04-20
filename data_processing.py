from abc import ABC, abstractmethod
import pandas as pd
import requests
from constants import DATA_FOLDER, ORIGINAL_DATA_FILENAME, CLEAN_DATA_FILENAME
from decorators import status_update, singleton

class DataProcessor(ABC):

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def _analyse_data(self):
        pass

    @abstractmethod
    def _clean_data(self):
        pass

    @abstractmethod
    def _save_data(self):
        pass



#@singleton
class NASADataProcessor(DataProcessor):
    def __init__(self, api_url):
        self.__api_url = api_url
        self.__destination_path = DATA_FOLDER
        self.__original_file_name = ORIGINAL_DATA_FILENAME
        self.__cleaned_file_name = CLEAN_DATA_FILENAME
        self.__original_data = None
        self.__clean_data = None
        self.__grouped_data = None
        self.__df = None

    @status_update
    def __fetch_data(self):
        response = requests.get(self.__api_url)
        self.__original_data = response.content

    @status_update
    def __delete_outdated_data(self):
        self.__df['rowupdate'] = pd.to_datetime(self.__df['rowupdate'])
        most_recent_data_index = self.__df.groupby('pl_name')['rowupdate'].idxmax()
        self.__df = self.__df.loc[most_recent_data_index]

    @status_update
    def _analyse_data(self):
        has_missing_values = self.__df.isna().any().any()
        print(f'Dataframe has missing values: {has_missing_values}')
        rows_with_missing_data = self.__df[self.__df.isna().any(axis=1)]
        planets_with_missing_data = rows_with_missing_data['pl_name']
        print(f'Planets with incomplete data: {len(planets_with_missing_data)}')

    @status_update
    def __handle_missing_data(self):
        has_missing_values = self.__df.isna().any().any()
        if has_missing_values:
            self.__df.dropna(inplace=True)

    @status_update
    def _clean_data(self):
        self.__delete_outdated_data()
        self.__handle_missing_data()



    @status_update
    def _save_data(self, option):
        if option == "original":
            with open(self.__destination_path + self.__original_file_name, 'wb') as file:
                file.write(self.__original_data)
        elif option == "df":
            self.__df.to_csv(self.__destination_path + self.__cleaned_file_name, index=False)


    @status_update
    def load_data(self, option):
        if option == "original":
            self.__df = pd.read_csv(self.__destination_path + self.__original_file_name)
        elif option == "clean":
            self.__df = pd.read_csv(self.__destination_path + self.__cleaned_file_name)

    def group_data(self):
        return self.__df.groupby('hostname')


    @status_update
    def update_data(self):
        self.__fetch_data()
        self._save_data("original")
        self.load_data("original")
        self._analyse_data()
        self._clean_data()
        self._analyse_data()
        self._save_data("df")
