# SBOL-to-Excel

SBOL-to-Excel is an open source python library that converts [SBOL documents]() to [Excel templates]().

For further depth and information on SBOL-to-Excel, including how to contribute to the project, visit the SBOL-to-EXCEL wiki on github

# Table of Contents
- [Installation & How to Use]()
  -  [Installation](https://github.com/SynBioDex/SBOL-to-Excel#installation)
  -  [How to Use]()
- [Example Conversion]()
- [Architecture]()
- [Publishing]()

# SBOL-to-Excel: Installation & How to Use

## Installation

SBOL-to-Excel can be downloaded using `pip install sbol2excel`

To get the latest version you can use git clone https://github.com/SynBioDex/SBOL-to-Excel followed by cd .\sbol2excel and python setup.py install

## How to Use
**1) Choose an existing SBOL Sheet** Choose an existing SBOL Sheet that you would like to to convert. We suggest that you choose the latest version of that specific Sbol file. 

**2) Install the Converter** There are several ways to install the converter. The easiest is via `pip: pip install sbol2excel` but it can also be done by cloning the repository.

**3) Run the Converter** Use the code below substituting {things in curly brackets} with the appropriate values.

# Example Conversion

# Architecture
The [repository architecture and module architecture](https://github.com/SynBioDex/SBOL-to-Excel/wiki) are described in the wiki.

# Publishing
A new version of the python package is automatically published via the [python-publish GitHub action whenever](https://github.com/SynBioDex/SBOL-to-Excel/blob/master/.github/workflows/python-publish.yml) a new release is created.

Alternatively you can also make changes to the package and then use it locally:

1. Clone the directory: `git clone https://github.com/SynBioDex/SBOL-to-Excel`
2. Change your directory to the sbol2excel folder: cd .\sbo2excel
3. Install an editable version of the package: python -m pip install -e . (will overwrite the directory in site-packages with a symbolic link to the locations repository). If a virtual environment is being used the python -m can be left off.

