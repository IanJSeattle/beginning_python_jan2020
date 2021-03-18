""" this program takes in a csv file with one data point per line, and analyzes
the data statistically. """

import csv
import sys

def get_csv_data(filename):
    """ retrieve CSV data from the file, and return it as a list """
    data = [ ]
    with open(filename) as fp:
        # read in the data
        csv_reader = csv.reader(fp)
        for row in csv_reader:
            data.append(row)
    # close is automatically called at this point
    return data

def print_stats(data):
    """ print out useful statistics about our data """
    #data_copy = [item for item in data]
    good_data = [int(item[0]) for item in data if int(item[0]) > 10]
    running_total = sum(good_data)
    maximum = max(good_data)
    minimum = min(good_data)
    print(f'max: {maximum}, min: {minimum}, total: {running_total}')
    mean = running_total / len(good_data)
    print(f'mean: {mean}')

def main():
    """ do the main thing """
    filename = sys.argv[1]
    data = get_csv_data(filename)
    print_stats(data)

# call the main function.  this is done conditionally, so that if
# this module is imported elsewhere, it won't run
if __name__ == '__main__':
    main()
