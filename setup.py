# setup.py

from setuptools import setup, find_packages

setup(
    name='h2o_ml_wrapper',
    version='0.1',
    description='Simple wrapper around H2O for training and prediction',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'h2o'
    ],
)
