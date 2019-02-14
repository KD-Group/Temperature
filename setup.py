"""
setup.py file for temperature module
"""

from setuptools import setup, find_packages
from distutils.core import setup, Extension


setup(name='temperature',
      version='1.3',
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

      description="Python module for temperature",
      packages=['temperature'],
      data_files=['cpp_build/temperature.exe', 'cpp_build/Temperature.dll'],
      python_requires='>=3',
      )
