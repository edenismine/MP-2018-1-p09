#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Runs all the solutions for the Modeling and Programming 2018-1's ninth lab
practice"""
import os
import ninth

__author__ = "Luis Daniel Aragon Bermudez 416041271"
__credits__ = ["Luis Daniel Aragon Bermudez"]
__maintainer__ = "Luis Daniel Aragon Bermudez"
__email__ = "daniel.aragon@ciencias.unam.mx"
__status__ = "Production"

if __name__ == '__main__':
    # Sets cwd to this file's location to ensure relative paths work as expected
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    media_dir = os.path.dirname(os.path.abspath('../media/*'))

    # Render all figures
    ninth.render_fig1(media_dir, 'fig01.png', 6, 4)
    ninth.render_fig2(media_dir, 'fig02.png', 10, 6)
    ninth.render_fig3(media_dir, 'fig03.png', 10, 6)
    ninth.render_fig4(media_dir, 'fig04.png', 10, 6)
    ninth.render_fig5(media_dir, 'fig05.png', 6, 4)
    ninth.render_movie1(media_dir, 'mov01.mp4', 8, 4.5)
