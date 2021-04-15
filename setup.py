from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'topo_covidnet',
    version          = '0.0.1',
    description      = 'An app to work with TS plugins',
    long_description = readme,
    author           = 'Mario Han',
    author_email     = 'hanmario@bu.edu',
    url              = 'http://wiki',
    packages         = ['topo_covidnet'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'topo_covidnet = topo_covidnet.__main__:main'
            ]
        }
)
