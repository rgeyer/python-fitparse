from distutils.core import setup
import sys
from setuptools import find_packages

import fitparse


setup(
    name='fitparse',
    version='0.0.1',
    description='Python library to parse ANT/Garmin .FIT files',
    author='David Cooper',
    author_email='dave@kupesoft.com',
    url='https://www.github.com/dtcooper/python-fitparse',
    license=open('LICENSE').read(),
    packages=find_packages(),
    )
