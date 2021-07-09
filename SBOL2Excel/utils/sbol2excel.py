import os

# wasderivedfrom: source
# remove identity, persistenID, displayID, version
# remove attachment (if empty)
# add library sheets
# add postprocessing function to remove unecessaries


class seqFile:

    def __init__(self, file_path_in, output_path):
        # global varibales for homespace, document, and sheet
        self.homeSpace = 'https://sys-bio.org'
        self.document = file_path_in
        self.file_location_path = os.path.dirname(__file__)
        self.sheet = os.path.join(self.file_location_path, 'ontologies.xlsx')
        self.output_template = os.path.join(self.file_location_path, 'Template_to_Output_Into_v001.xlsx')
        self.output_path = output_path

    def overarching(self):
        df = self.readDocChart()
        df = self.reorder_columns(df)
        self.returnExcelChart(df)
        return
