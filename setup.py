"""
setup.py file for temperature module
"""

from distutils.core import setup, Extension
from setuptools import setup, find_packages

setup(name='temperature',
      version='2.7',
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
      packages=['temperature', "cpp_build"],
      package_data={"cpp_build": ['*.exe', '*.dll']},
      description="Python module for temperature",
      python_requires='>=3',
      )
