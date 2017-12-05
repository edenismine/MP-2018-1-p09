#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fourth Exercise: Polar coordinates"""
import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from .export import export

__author__ = "Luis Daniel Aragon Bermudez 416041271"
__credits__ = ["Luis Daniel Aragon Bermudez"]
__maintainer__ = "Luis Daniel Aragon Bermudez"
__email__ = "daniel.aragon@ciencias.unam.mx"
__status__ = "Production"

__MEDIA_DIR = '../../media/'


def render_movie1(media_dir=__MEDIA_DIR, f_name='movie1.mp4', width=5,
                  height=5, padding=0, dpi=120):
    """Renders the sixth figure.

    This figure shows a paraboloid of revolution.

    :param media_dir: Export directory for the figure.
    :param f_name: Export file name.
    :param width: Figure's width (inches).
    :param height: Figure's height (inches).
    :param padding: Figure's padding (inches).
    :param dpi: Figure's DPI.
    """

    def heartbeat(xs):
        return np.exp(-20 * np.power(np.mod(xs + 1, 2) - 1, 2)) * \
               np.sin( 20 * np.mod(xs + 1, 2) - 1)

    # Setup
    fig, ax = plt.subplots(facecolor='black')
    fig.set_size_inches(width, height)
    ax.set_facecolor('black')
    ax.axis(color='black')
    ax.grid('both', color='#303030')
    for ticx, ticy in zip(ax.xaxis.get_major_ticks(), ax.yaxis.get_major_ticks()):
        ticx.tick1On = ticx.tick2On = ticx.label1On = ticx.label2On = False
        ticy.tick1On = ticy.tick2On = ticy.label1On = ticy.label2On = False

    # Generate and plot data points
    x = np.arange(-2, 2, 0.01)
    line, = ax.plot(x, heartbeat(x), color='green')

    def update(i):
        line.set_ydata(heartbeat(x + i / 30))
        return line,

    def init():
        line.set_ydata(np.ma.array(x))
        return line,

    # PNG exporting
    export(media_dir, "fig06.png", fig, width, height, padding, dpi)

    # Video exporting
    path = os.path.join(media_dir, f_name)
    ani = animation.FuncAnimation(fig, update,
                                  init_func=init,
                                  frames=5 * 60,
                                  interval=1,
                                  blit=True)
    ani.save(path,
             fps=60,
             dpi=dpi,
             savefig_kwargs={'facecolor': 'black',
                             'pad_inches': padding})
    print(f"Saved {f_name} to {path}")


if __name__ == '__main__':
    render_movie1()
