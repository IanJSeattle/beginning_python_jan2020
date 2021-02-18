""" this program takes in a csv file with one data point per line, and analyzes
the data statistically. """

import csv
import sys

def get_csv_data(filename):
    """ retrieve CSV data from the file, and return it as a list """
    data = []
    with open(filename) as fp:
        # read in the data
        csv_reader = csv.reader(fp)
        for row in csv_reader:
            data.append(row)
    # close is automatically called at this point
    return data

def main():
    """ do the main thing """
    filename = sys.argv[1]
    data = get_csv_data(filename)
    print(data)
    #print_stats(data)

# call the main function.  this is not the best way to do it, but we'll talk
# about better ways in a future lesson.
main()
