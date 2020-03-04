from alpha_vantage.timeseries import TimeSeries
import csv
import matplotlib.pyplot as plt
symbol = 'CDR'
ts = TimeSeries(key='IKDJ9GE6HUPN0CYW', output_format='pandas')

def csv_daily_data(symbol, path):
    data, _ = ts.get_daily(symbol=symbol)
    data.to_csv(path)