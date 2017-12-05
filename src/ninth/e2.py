#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Second Exercise: Languages of the world, global and regional graphs"""
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .exporter import export

__author__ = "Luis Daniel Aragon Bermudez 416041271"
__credits__ = ["Luis Daniel Aragon Bermudez"]
__maintainer__ = "Luis Daniel Aragon Bermudez"
__email__ = "daniel.aragon@ciencias.unam.mx"
__status__ = "Production"

__MEDIA_DIR = '../../media/'
__CSV_DIR = 'csv_files/'
__INDICES = {'North America': 1,
             'Europe': 2,
             'Latin America': 3,
             'Africa': 4,
             'Asia & Pacific': 5
             }

__BARS = {'North America': 0,
          'Europe': 0,
          'Latin America': 0,
          'Africa': 0,
          'Asia & Pacific': 0
          }

__COLORS = {'Spanish': '#e6194b',
            'English': '#3cb44b',
            'Russian': '#ffe119',
            'Portuguese': '#0082c8',
            'Arabic': '#f58231',
            'Chinese': '#911eb4',
            'Hindustani': '#46f0f0',
            'Indonesian': '#f032e6',
            'Creole': '#d2f53c',
            'Ukrainian': '#fabebe',
            'Punjabi': '#008080',
            'Japanese': '#e6beff',
            'Turkish': '#aa6e28',
            'Bengali': '#fffac8',
            'French': '#800000',
            'German': '#aaffc3',
            'Polish': '#808000',
            'Kwa': '#ffd8b1',
            'Hausa': '#000080',
            'Swahili': '#808080',
            'Italian': '#FFFFFF',
            'Other': '#000000'}

__REGIONS = [('North America', (.7, .09, .03, .01, .17),
              ('English', 'Spanish', 'French', 'Chinese', 'Other')),
             ('Europe', (.22, .12, .09, .08, .08, .08, .06, .06, .04, .17),
              ('Russian', 'German', 'Turkish', 'English', 'Italian',
               'French', 'Polish', 'Spanish', 'Ukrainian', 'Other')),
             ('Latin America', (.58, .33, .02, .01, .06),
              ('Spanish', 'Portuguese', 'Creole', 'English', 'Other')),
             ('Africa', (.17, .08, .06, .04, .04, .03, .58),
              ('Arabic', 'Swahili', 'French', 'English', 'Kwa', 'Hausa',
               'Other')),
             ('Asia & Pacific', (.34, .12, .08, .06, .03, .03, .34),
              ('Chinese', 'Hindustani', 'Bengali', 'Indonesian', 'Japanese',
               'Punjabi', 'Other'))]


def plot_by_region(region, values, x_labels, bar_width):
    """Plots a region's percentage of speakers for each language (bar chart)

    :param region: the region.
    :param values: the percentages of speakers.
    :param x_labels: the corresponding language label for each value.
    :param bar_width: the width each bar should have
    """
    for point, language in enumerate(x_labels):
        index = np.arange(__INDICES[region] - 1, __INDICES[region])
        plt.bar(index + __BARS[region] * bar_width, (values[point],),
                bar_width,
                alpha=1,
                color=__COLORS[language],
                label=language)
        __BARS[region] = __BARS[region] + 1


def render_fig2(media_dir=__MEDIA_DIR, f_name='fig5.png', width=5, height=5,
                padding=0, dpi=120):
    """Renders the second figure.

    This figure shows a bar chart that measures what percentage of the
    inhabitants of each region speak a certain language.

    :param media_dir: Export directory for the figure.
    :param f_name: Export file name.
    :param width: Figure's width (inches).
    :param height: Figure's height (inches).
    :param padding: Figure's padding (inches).
    :param dpi: Figure's DPI.
    """
    # Gets current axis
    fig, ax = plt.subplots()

    # Default bar_width and data plotting
    bar_width = 0.09
    for region_name, values, labels in __REGIONS:
        plot_by_region(region_name, values, labels, bar_width)

    # Arrange and format ticks and axis labels
    ticks = ax.get_yticks()
    ax.set_yticklabels(['{:3.0f}%'.format(x * 100) for x in ticks])
    poss = [__INDICES[key] - 1 + ((value - 1) * bar_width) / 2
            for key, value in __BARS.items()]
    plt.grid(axis='x')
    plt.xticks(poss, ('North America', 'Europe', 'Latin America',
                      'Africa', 'Asia & Pacific'))
    plt.xlabel('Regions')
    plt.ylabel('Population that speaks the language')

    # Remove duplicate labels
    handles, labels = ax.get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)
    plt.legend(handle_list, label_list, bbox_to_anchor=(0., -.2, 1., .102),
               loc=3, ncol=11, mode="expand", borderaxespad=0., fontsize=6)

    # Set title
    plt.title('Languages of the world')

    # Export
    export(media_dir, f_name, fig, width, height, padding, dpi)


def render_fig3(media_dir=__MEDIA_DIR, f_name='fig5.png', width=5, height=5,
                padding=0, dpi=120):
    """Renders the third figure.

    This figure shows a pie chart that shows what percentage of the world's
    population (natively) speak a certain language.
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

    # Extracts data from csv
    csv_file = pd.read_csv(__CSV_DIR + 'languages.csv')
    percentages = csv_file['Percentage']
    languages = csv_file['Language']

    # Sets up color and labels
    fig = plt.figure()
    colors = plt.get_cmap('viridis')(np.linspace(1., 0., len(languages)))
    labels = [f'{i} - {j*100:2.2f} %' for i, j in zip(languages, percentages)]

    # Plots pie
    plt.subplot(121)
    plt.gca().axis('equal')
    patches, _ = plt.pie(percentages, startangle=90, colors=colors,
                         center=(0, .8), radius=1.7)

    # Shows labels on the side
    plt.subplot(122)
    plt.title("Percentage of native speakers")
    plt.axis('off')
    plt.legend(patches, labels, loc='center', fontsize=10, mode='expand')

    # Export
    export(media_dir, f_name, fig, width, height, padding, dpi)


if __name__ == '__main__':
    render_fig2()
    render_fig3()
