#pytest -v -s

import SBOL2Excel as s_e
import pytest
from pandas.testing import assert_frame_equal
import sbol2
import pandas as pd 
import os
from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Font, PatternFill, Border, Side
from requests_html import HTMLSession

file_dir = os.path.dirname(__file__)
test_files_path = os.path.join(file_dir, 'test_files')


class seqFile:
    def __init__(self, document):
        #global varibales for homespace, document, and sheet
        self.homeSpace = 'http://sys-bio.org'
        self.document = document
        self.sheet = 'ontologies.xlsx'

def test_seqClass():
    x = s_e.seqFile('pichia_toolkit_KWK_v002.xml')
    assert x.document == 'pichia_toolkit_KWK_v002.xml'
    assert x.sheet == 'ontologies.xlsx'
    assert x.homeSpace == 'http://sys-bio.org'
    
def test_roleVariables():
    x = s_e.seqFile('pichia_toolkit_KWK_v002.xml')
    roleDictionary = x.roleVariables()
    assert roleDictionary == {}