import pytest
from unittest.mock import patch
import pandas as pd
from data_processing import NASADataProcessor


@pytest.fixture
def nasa_processor():
    api_url = "test.com"
    return NASADataProcessor(api_url)


def test_load_data(nasa_processor):
    with patch('pandas.read_csv') as mock_read_csv:
        nasa_processor.load_data("original")
        mock_read_csv.assert_called_once_with(
            nasa_processor._NASADataProcessor__destination_path + nasa_processor._NASADataProcessor__original_file_name)

        mock_read_csv.reset_mock()

        nasa_processor.load_data("clean")
        mock_read_csv.assert_called_once_with(
            nasa_processor._NASADataProcessor__destination_path + nasa_processor._NASADataProcessor__cleaned_file_name)


def test_analyse_data(nasa_processor):
    data = {'pl_name': ['Earth', 'Mars', 'Mars'], 'rowupdate': ['2021-01-01', '2021-01-02', '2021-02-01']}
    df = pd.DataFrame(data)
    df['rowupdate'] = pd.to_datetime(df['rowupdate'])
    nasa_processor._NASADataProcessor__df = df
    nasa_processor._analyse_data()


def test_clean_data(nasa_processor):
    data = {'pl_name': ['Earth', 'Earth', 'Mars', 'Mars'],
            'rowupdate': pd.to_datetime(['2021-01-01', '2021-01-02', '2021-01-01', '2021-02-01'])}
    df = pd.DataFrame(data)
    nasa_processor._NASADataProcessor__df = df
    nasa_processor._clean_data()

    assert len(nasa_processor._NASADataProcessor__df) == 2
    assert nasa_processor._NASADataProcessor__df['pl_name'].tolist() == ['Earth', 'Mars']
