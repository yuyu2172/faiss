#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages
from setuptools.command.install import install

import os
import subprocess


description = """
A wrapper to make installation of faiss easily for Python users
"""

class CustomInstall(install):
    def run(self):
        subprocess.call(['./install.sh'], shell=True)


setup(
    name='faiss',
    version='0.0.1',
    packages=find_packages(),
    author='Yusuke Niitani',
    author_email='yuyuniitani@gmail.com',
    license='CC by NC',
    description=description,
    cmdclass={'install': CustomInstall}
    # install_requires=open('requirements.txt').readlines(),
)
