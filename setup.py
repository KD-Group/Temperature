"""
setup.py file for temperature module
"""

import shutil
from distutils.core import setup, Extension
from setuptools import setup, find_packages

shutil.copy2("cpp_build/Temperature.dll", "temperature/Temperature.dll")
shutil.copy2("cpp_build/temperature.exe", "temperature/temperature.exe")

setup(name='temperature',
      version='2.5',
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
      package_data={"temperature": ['*.exe', '*.dll']},
      description="Python module for temperature",
      python_requires='>=3',
      )
