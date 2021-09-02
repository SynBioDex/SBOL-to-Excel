# SBOL-to-Excel

SBOL-to-Excel is an open source python library that converts [SBOL documents]() to [Excel templates]().

For further depth and information on SBOL-to-Excel, including how to contribute to the project, visit the SBOL-to-EXCEL wiki on github

# Table of Contents
- [Installation & How to Use](#installation--how-to-use)
  -  [Installation](#installation)
  -  [How to Use](#how-to-use)
- [Example Conversion](#example-conversion)
- [Architecture](#architecture)
- [Publishing](#publishing)

# SBOL-to-Excel: Installation & How to Use

## Installation

SBOL-to-Excel can be downloaded using `pip install sbol2excel`

To get the latest version you can use git clone https://github.com/SynBioDex/SBOL-to-Excel followed by cd .\sbol2excel and python setup.py install

## How to Use
**1) Choose an existing SBOL Sheet** Choose an existing SBOL Sheet that you would like to to convert. We suggest that you choose the latest version of that specific Sbol file. 

**2) Install the Converter** There are several ways to install the converter. The easiest is via `pip: pip install sbol2excel` but it can also be done by cloning the repository.

**3) Run the Converter** Use the code below substituting {things in curly brackets} with the appropriate values.

```
import utils.converter as conv
import os

cwd = os.getcwd()
sbol_doc_path = os.path.join(cwd, {file_path})
output_path = os.path.join(cwd, {output_excel_file})
conv.converter(sbol_doc_path, output_path)
```

An Example:

```
import utils.converter as conv
import os


cwd = os.getcwd()
sbol_doc_path = os.path.join(cwd, 'SBOL2Excel', 'tests', 'test_files',
                             'test_sbol.xml')
output_path = os.path.join(cwd, 'test.xlsx')
conv.converter(sbol_doc_path, output_path)
```
Tip: the use of `os.getcwd()` and `os.path.join` is reccommended for the creation of the file paths. This is safer from a cybersecurity stand point and provide better operating system interoperability.

**4) Use the Output File** The Excel file that is output can then be used to further analyze your given SBOL file. You can find more of SBOL files to convert into an Exel format by searching an SBOL repository like [SynBioHub](https://synbiohub.org/).

# Example Conversion

An [SBOL file](https://github.com/SynBioDex/SBOL-to-Excel/blob/master/SBOL2Excel/resources/templates/pichia_toolkit_KWK_v002.xml) from [SynBioHub](https://synbiohub.org/) was converted to a data-filled Excel spreadsheet.

**Example SBOL**
![example_sbol](https://user-images.githubusercontent.com/29416272/125694833-9aa804eb-7deb-4622-adc9-88f4cdb6ddcc.png)

**Example Spreadsheet**
![test](https://user-images.githubusercontent.com/29416272/125802728-ba119735-8940-4853-998c-b54e78a98d9c.png)

# Architecture
The [repository architecture and module architecture](https://github.com/SynBioDex/SBOL-to-Excel/wiki) are described in the wiki.

# Publishing
A new version of the python package is automatically published via the [python-publish GitHub action whenever](https://github.com/SynBioDex/SBOL-to-Excel/blob/master/.github/workflows/python-publish.yml) a new release is created.

Alternatively you can also make changes to the package and then use it locally:

1. Clone the directory: `git clone https://github.com/SynBioDex/SBOL-to-Excel`
2. Change your directory to the sbol2excel folder: cd .\sbo2excel
3. Install an editable version of the package: `python -m pip install -e .` (will overwrite the directory in site-packages with a symbolic link to the locations repository). If a virtual environment is being used the python -m can be left off.

