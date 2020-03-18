import os

from alpha_vantage.timeseries import TimeSeries


class Data:
    def __init__(self, key, data_dir, output_format='pandas', ):
        self.ts = TimeSeries(key=key, output_format=output_format)
        self.data_dir = data_dir
        self.create_data_directory(path=data_dir)

    def daily_to_csv(self, symbol):
        data, meta = self.ts.get_daily(symbol=symbol, outputsize='full')
        data.to_csv(path_or_buf=self.data_dir + '/' + symbol + '.csv')
        pass

    @staticmethod
    def create_data_directory(path):
        if not os.path.isdir(path):
            os.mkdir(path)

    # TODO could be more portable
    def clean(self, path=None):
        rm_dir = path if path is not None else self.data_dir
        if os.path.isdir(rm_dir):
            os.system('rm -rf %s' % rm_dir)
