"""This file features information about modules and packages.

The packages areutilized by SBOL-to-Excel

"""

from setuptools import find_packages, setup


setup(name='sbol2excel',
      version='1.0.0-alpha-10',
      url='https://github.com/SynBioDex/SBOL-to-Excel',
      license='BSD 3-clause',
      maintainer='Julian Abam',
      maintainer_email='abamaj@gmail.com',
      include_package_data=True,
      description='convert sbol resources into excel',
      packages=find_packages(include=['sbol2excel']),
      long_description=open('README.md').read(),
      install_requires=['requests-html>=0.10.0',
                        'pandas>=1.4.2',
                        'openpyxl>=3.0.10',
                        'rdflib>=6.1.1',
                        'validators>=0.19.0'],
      zip_safe=False)
