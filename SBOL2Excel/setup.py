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
      install_requires=['appdirs==1.4.4',
                        'beautifulsoup4==4.9.3',
                        'bs4==0.0.1',
                        'certifi==2021.5.30',
                        'chardet==4.0.0',
                        'cssselect==1.1.0',
                        'Deprecated==1.2.12',
                        'et-xmlfile==1.1.0',
                        'fake-useragent==0.1.11',
                        'idna==2.10',
                        'isodate==0.6.0',
                        'lxml==4.6.5',
                        'numpy==1.20.3',
                        'openpyxl==3.0.7',
                        'packaging==20.9',
                        'pandas==1.2.4',
                        'parse==1.19.0',
                        'pyee==8.1.0',
                        'pyparsing==2.4.7',
                        'pyppeteer==0.2.5',
                        'pyquery==1.4.3',
                        'python-dateutil==2.8.1',
                        'pytz==2021.1',
                        'rdflib==5.0.0',
                        'requests==2.25.1',
                        'requests-html==0.10.0',
                        'sbol2==1.2',
                        'six==1.16.0',
                        'soupsieve==2.2.1',
                        'tqdm==4.61.1',
                        'urllib3==1.26.5',
                        'w3lib==1.22.0',
                        'wrapt==1.12.1'],
      zip_safe=False)
