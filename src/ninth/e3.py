#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Third Exercise: Polar coordinates"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

from .export import export

__author__ = "Luis Daniel Aragon Bermudez 416041271"
__credits__ = ["Luis Daniel Aragon Bermudez"]
__maintainer__ = "Luis Daniel Aragon Bermudez"
__email__ = "daniel.aragon@ciencias.unam.mx"
__status__ = "Production"

__MEDIA_DIR = '../../media/'


def render_fig4(media_dir=__MEDIA_DIR, f_name='fig5.png', width=5, height=5,
                padding=0, dpi=120):
    """Renders the fourth figure.

    This figure shows two functions graphed in the polar plane.

    :param media_dir: Export directory for the figure.
    :param f_name: Export file name.
    :param width: Figure's width (inches).
    :param height: Figure's height (inches).
    :param padding: Figure's padding (inches).
    :param dpi: Figure's DPI.
    """
    # Sets graphing style
    plt.style.use('ggplot')

    # Extract figure and create gridspec
    fig = plt.figure()
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

    # Generate data points
    theta = np.arange(0, np.pi * 2, np.pi / 10000)
    r1 = np.cos(3 * theta)
    r2 = np.power(np.power(np.sin(2 * theta), 4) - 1, 6)

    # First plot
    ax0 = plt.subplot(gs[0], projection='polar')
    ax0.plot(theta, r1, color='#e6194b')
    plt.title("$r=\\cos3\\theta$",
              color='#e6194b', y=1.1)

    # Second plot
    ax1 = plt.subplot(gs[1], projection='polar')
    ax1.plot(theta, r2, color='#800000')
    plt.title("$r=\\left(\\sin\\left(2\\theta\\right)^4-1\\right)^6$",
              color='#800000', y=1.1)

    # Format axes
    for ax in [ax0, ax1]:
        ax.set_rlabel_position(90)
        ax.set_rmin(0)
        ax.set_rmax(1.2)
        ax.set_rticks(np.arange(0, 1.2, 0.2))

    # Export
    export(media_dir, f_name, fig, width, height, padding, dpi)


if __name__ == '__main__':
    render_fig4()
