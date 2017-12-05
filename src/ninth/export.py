#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Figure export"""
import os

__author__ = "Luis Daniel Aragon Bermudez 416041271"
__credits__ = ["Luis Daniel Aragon Bermudez"]
__maintainer__ = "Luis Daniel Aragon Bermudez"
__email__ = "daniel.aragon@ciencias.unam.mx"
__status__ = "Production"

def export(media_dir, f_name, fig, width=5, height=5, padding=0, dpi=120):
    """Exports the provided figure.
    :param media_dir: Export directory for the figure.
    :param f_name: Export file name.
    :param fig: The provided figure.
    :param width: Figure's width (inches).
    :param height: Figure's height (inches).
    :param padding: Figure's padding (inches).
    :param dpi: Figure's DPI.
    """
    path = os.path.join(media_dir, f_name)
    fig.set_size_inches(width, height)
    fig.savefig(path, bbox_inches='tight', pad_inches=padding, dpi=dpi)
    print(f"Saved {f_name} to {path}")