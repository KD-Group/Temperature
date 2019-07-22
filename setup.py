"""
setup.py file for temperature module
"""

from setuptools import setup, find_packages
from distutils.core import setup, Extension

setup(name='temperature',
      version='2.4',
      author="WingC, SF Zhou",
      author_email="1018957763@qq.com",
      url="https://gitlab.com/KD-Group/temperature",

      license='GPL',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',

          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Programming Language :: Python :: 3',
      ],
      packages=['temperature'],
      data_files=['cpp_build/temperature.exe', 'cpp_build/Temperature.dll'],

      description="Python module for temperature",
      python_requires='>=3',
      )
