from requests_html import HTMLSession


class col_methods:
    """A class used to carry out a switch case statement for different\
       properties in SBOL files
    """

    def __init__(self, prop_nm, prop_val, sbol_doc, role_dict, org_dict):
        # global varibales for dataframe switch statements
        self.prop_nm = prop_nm
        self.prop_val = prop_val
        self.sbol_doc = sbol_doc
        self.role_dict = role_dict
        self.org_dict = org_dict

        if type(self.prop_nm) is not str:
            raise TypeError
        # if the column name matches the function name, call the function
        try:
            return getattr(self, self.prop_nm)()
        # if the column name does not match the function name, call 'no_change'
        except AttributeError:
            return getattr(self, 'no_change')()

    def no_change(self):
        """Else case for the switch statement"""
        pass

    def role(self):
        """Uses prop_val as the key in a dictionary to get the new value.
        It is a way of converting an ontology term to a human readable one
        """
        role_val = str(self.prop_val)
        if role_val in self.role_dict:
            self.prop_val = self.role_dict[role_val]

    def types(self):
        """Split types uri to only be the last bit after the final hash
        """
        if type(self.prop_val) is not str:
            raise TypeError
        elif '#' not in self.prop_val:
            raise ValueError
        else:
            self.prop_val = self.prop_val.split('#')[-1]

    def sequence(self):
        """Gets the sequence from the document based on the sequence uri
        """
        self.prop_val = self.sbol_doc.getSequence(self.prop_val).elements

    def source_organism(self):
        """Converts a uri containing a txid into a human readable name
        either by using the ontology provided or by pulling the name from
        the ncbi database. If the name is pulled from the database it is added
        to the ontology for the rest of the program run (the assumption is
        that a rare organism may be used multiple times)
        """
        if type(self.prop_val) is not str:
            raise TypeError

        txid = str(self.prop_val).split(':')[-1]

        if txid in self.org_dict:
            self.prop_val = self.org_dict[txid]
        else:
            session = HTMLSession()
            r = session.get(self.prop_val)
            v = r.html.find('strong', first=True)
            self.prop_val = v.text
            self.org_dict[txid] = self.prop_val

    def targetOrganism(self):
        """Same function as source_organism"""
        self.source_organism()
