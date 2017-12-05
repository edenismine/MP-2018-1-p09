#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fourth Exercise: Polar coordinates"""

import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d

from .export import export

__author__ = "Luis Daniel Aragon Bermudez 416041271"
__credits__ = ["Luis Daniel Aragon Bermudez"]
__maintainer__ = "Luis Daniel Aragon Bermudez"
__email__ = "daniel.aragon@ciencias.unam.mx"
__status__ = "Production"

__MEDIA_DIR = '../../media/'


def render_fig5(media_dir=__MEDIA_DIR, f_name='fig5.png', width=5, height=5,
                padding=0, dpi=120):
    """Renders the fifth figure.

    This figure shows a paraboloid of revolution.

    :param media_dir: Export directory for the figure.
    :param f_name: Export file name.
    :param width: Figure's width (inches).
    :param height: Figure's height (inches).
    :param padding: Figure's padding (inches).
    :param dpi: Figure's DPI.
    """
    # Sets graphing style
    plt.style.use('ggplot')

    # Extract fig and ax
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    # Generate data points
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, 2 * np.pi, 50)
    U, V = np.meshgrid(u, v)
    X = np.sqrt(U) * np.cos(V)
    Y = np.sqrt(U) * np.sin(V)
    Z = U

    # Plot
    ax.plot_surface(X, Y, Z, cmap='magma')
    plt.title('Paraboloid of revolution')

    # Export
    export(media_dir, f_name, fig, width, height, padding, dpi)


if __name__ == '__main__':
    render_fig5()
