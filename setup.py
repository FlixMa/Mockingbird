#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mockingbird-psd',
    version="1.0.4",
    author="Felix Maaß",
    author_email="mockingbird@flixma.de",
    description="Easily bulk embed your screenshots in Apple device mockups.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlixMa/Mockingbird",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='~=3.6',
    install_requires=['opencv-python', 'psd-tools'],
    scripts=['mockingbird']
)
