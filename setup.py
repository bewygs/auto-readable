# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    install_requires = f.read()

setup(
    name='auto-read',
    version='1.0',
    description='Simple package for automatically reading the text inside an image',
    long_description=readme,
    author='bewygs',
    author_email='benoit.wgs@protonmail.com',
    url='https://github.com/',
    license=license,
    packages=find_packages(),
    install_requires=install_requires,
)