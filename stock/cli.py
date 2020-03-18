import argparse
import os

from .data import Data

default_data_dir = 'data'

class CommandLineInterface:
    def __init__(self):
        self.api_key = None
        self.api_key_path = 'alpha_vantage_api_key'
        self.parser = self.setup_parser()
        self.data = None

    def setup_parser(self):
        parser = argparse.ArgumentParser(description='Download stock data and plot macd pointer of given company.')
        parser.add_argument('-k', '--key', type=self.save_key,
                            help='key to alpha vantage API')
        parser.add_argument('-d', '--download', type=self.download, metavar='symbols', nargs='+',
                            help='download stock data for given company symbol')
        parser.add_argument('-c', '--clean', help='remove all downloaded data', nargs='?',
                            type=self.clean, const=default_data_dir)
        return parser

    def setup_data(self):
        key = self.get_api_key()
        self.data = Data(key=key, data_dir=default_data_dir)

    def save_key(self, key):
        try:
            with open(self.api_key_path, 'w') as key_file:
                key_file.write(key)
        except OSError:
            raise OSError("Cannot write api key.")

    def load_api_key_from_file(self):
        try:
            if os.path.getsize(self.api_key_path) > 0:
                with open(self.api_key_path, 'r') as api_key_file:
                    self.api_key = api_key_file.readline()
        except OSError:
            raise OSError("You need to set alpha vantage API key. See https://www.alphavantage.co/support/#api-key.")

    def get_api_key(self):
        if self.api_key is None:
            self.load_api_key_from_file()
        return self.api_key

    def download(self, symbol):
        if self.data is None:
            self.setup_data()
        print('wow dawnlading %s' % symbol)
        self.data.daily_to_csv(symbol)

    def clean(self, path):
        if self.data is None:
            self.setup_data()
        self.data.clean(path)

    def run(self):
        print(self.parser.parse_args())
