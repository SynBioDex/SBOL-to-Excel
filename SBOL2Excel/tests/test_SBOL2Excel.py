import S2X as s_e
import pytest
from pandas.testing import assert_frame_equal

@pytest.mark.parametrize(
        'homeSpace, document, sheet', [
            ('http://sys-bio.org', 'pichia_toolkit_KWK_v002.xml', 'ontologies.xlsx'),
            ('http://sys-bio.org', 'pichia_toolkit_KWK_collection.xml', 'ontologies.xlsx'),
            ('http://sys-bio.org', 'pichia_toolkit_KWK_collection.xml', 'pigeons.xlsx'),
            ('http://sbols.org/CRISPR_Example', 'pichia_toolkit_KWK_collection.xml', 'pigeons.xlsx'),
        ]
    )
def test_roleVars(homeSpace,  document, sheet):
    test1 = s_e.seqFile(homeSpace,  document, sheet)
    assert roleVars() == {}
                          