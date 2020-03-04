from stock_data import data_getter
import argparse

ALPHA_VANTAGE_API_KEY='IKDJ9GE6HUPN0CYW'
data_folder_path='data'

parser = argparse.ArgumentParser(description='Download, process MACD pointer and show the plot of given company.')
parser.add_argument('--pull', metavar='symbol', type=str,
                    help='download data of given company')
parser.add_argument('--process', metavar='symbol', type=str,
                    help='process already downloaded data')
parser.add_argument('--clean',
                    help='clean pulled data')
args = parser.parse_args()
if args.pull:
    print("Pulling {0:s} data.".format(args.pull))
elif args.process:
    print("Processing {0:s} data.".format(args.process))
elif args.clean:
    print("Cleaning data.")
else:
    parser.print_usage()


#data_getter.csv_daily_data(symbol, "{0:s}/{1:s}.csv".format(data_folder_path, symbol))


