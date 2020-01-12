# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="labjack_u6",
    version="0.1.0",
    description="Helper Library for the u6",
    license="MIT",
    author="Lou Grossi",
    packages=find_packages(),
    install_requires=['LabJackPython'],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ]
)
