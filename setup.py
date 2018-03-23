# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='spark-sample-code',
    version='0.1.0',
    description='Learning Spark and having a good time',
    long_description=readme,
    author='Jesse Rackliff',
    author_email='jrackliff@gmail.com',
    url='https://github.com/jrackliff/Spark-Sample-Code',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

