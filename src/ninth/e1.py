#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""First Exercise: Graph Time vs The unemployed population in Mexico from
2007 to 2017"""
import csv
import os
from functools import reduce
from math import floor

import matplotlib.pyplot as plt

from .export import export

__author__ = "Luis Daniel Aragon Bermudez 416041271"
__credits__ = ["Luis Daniel Aragon Bermudez"]
__maintainer__ = "Luis Daniel Aragon Bermudez"
__email__ = "daniel.aragon@ciencias.unam.mx"
__status__ = "Production"

__PERIODS = {'Primer': '_1',
             'Segundo': '_2',
             'Tercer': '_3',
             'Cuarto': '_4'}
__YEARS = list(range(2017, 2006, -1))
__MEDIA_DIR = '../../media/'
__CSV_DIR = 'csv_files/'


def year_avg(year, dictionary):
    """Calculates average population for a given year
    :param year: given year.
    :param dictionary: dictionary that contains all the data."""
    sample = [value for key, value in dictionary.items() if
              int(key[:4]) == year]
    n = len(sample)
    return floor(reduce(lambda x, y: x + y, sample) / n)


def render_fig1(media_dir=__MEDIA_DIR, f_name='fig5.png', width=5, height=5,
                padding=0, dpi=120):
    """Renders the first figure.

    This figure shows the graph of Time vs The unemployed population in
    Mexico from 2007 to 2017.

    :param media_dir: Export directory for the figure.
    :param f_name: Export file name.
    :param width: Figure's width (inches).
    :param height: Figure's height (inches).
    :param padding: Figure's padding (inches).
    :param dpi: Figure's DPI.
    """
    # Sets graphing style
    plt.style.use('ggplot')
    # Sets cwd to this file's location to ensure relative paths work as expected
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Gets current axis
    fig, ax = plt.subplots()

    # Extract INEGI's data into a list
    clean = {}
    with open(__CSV_DIR + "unemployed.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            split_period = row['Periodo'].split(' ')
            period = split_period[-1] + __PERIODS[split_period[0]]
            population = int(row['Población'].split('|')[0])
            clean[period] = population
    unemployed = [year_avg(y, clean) for y in __YEARS]

    # Plot values
    plt.title("Población desocupada en México (2007-2017)")
    plt.plot(__YEARS, unemployed, '-*')
    plt.xlabel('Año')
    plt.ylabel('Población')
    plt.xticks(__YEARS, map(str, __YEARS), rotation='vertical')

    # Export
    export(media_dir, f_name, fig, width, height, padding, dpi)


if __name__ == '__main__':
    render_fig1()
