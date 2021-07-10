from requests_html import HTMLSession
import sbol2
import rdflib


class col_methods:
    """A class used to carry out a switch case statement for different\
       properties in SBOL files
    """

    def __init__(self, prop_nm, prop_val, sbol_doc, role_dict, org_dict):
        """The switch statement to call different methods based on prop_nm

        Args:
            prop_nm (str): the name of the property
            prop_val (str): the value of the property
            sbol_doc (sbol document): sbol document containing the properties
                                being passed in
            role_dict (dictionary): maps sequence ontology terms to human
                                readable names
            org_dict (dictionary): maps ncbi txids to human readable names

        """
        # global varibales for dataframe switch statements
        self.prop_nm = prop_nm
        self.prop_val = prop_val
        self.sbol_doc = sbol_doc
        self.role_dict = role_dict
        self.org_dict = org_dict

        function_call_dict = {'Role': 'role', 'Types': 'types',
                              'Sequence': 'sequence',
                              'Source Organism': 'organism',
                              'Target Organism': 'organism'}
        if self.prop_nm in function_call_dict:
            self.prop_nm = function_call_dict[self.prop_nm]
        # if the column name matches the function name, call the function
        try:
            getattr(self, self.prop_nm)()
        # if the column name does not match the function name, call 'no_change'
        except AttributeError:
            getattr(self, 'no_change')()

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

        Raises:
            ValueError: If self.prop_val does not contain a #
        """
        self.prop_val = str(self.prop_val)
        if '#' not in self.prop_val:
            raise ValueError
        else:
            self.prop_val = self.prop_val.split('#')[-1]

    def sequence(self):
        """Gets the sequence from the document based on the sequence uri

        Raises:
            TypeError: If the prop_val from initialisation is not a uri
                        or string
            ValueError: If the prop_val from initialisation is not a uri
                    in the sbol document provided at initialisation
        """
        if type(self.prop_val) not in [rdflib.term.URIRef, str]:
            raise TypeError
        else:
            try:
                temp = self.sbol_doc.getSequence(self.prop_val)
                self.prop_val = temp.elements
            except sbol2.sbolerror.SBOLError:
                # if uri not found in document
                raise ValueError

    def organism(self):
        """        Converts a uri containing a txid into a human readable name
        either by using the ontology provided or by pulling the name from
        the ncbi database. If the name is pulled from the database it is added
        to the ontology for the rest of the program run (the assumption is
        that a rare organism may be used multiple times)

        Raises:
            TypeError: if self.prop_val is not a string or uri
            ValueError: if self.prop_val doesn't contain
                        'https://identifiers.org/taxonomy:'
            TypeError: if self.org_dict is not a dictionary
        """
        if type(self.prop_val) not in [rdflib.term.URIRef, str]:
            raise TypeError
        elif 'https://identifiers.org/taxonomy:' not in self.prop_val:
            raise ValueError
        if type(self.org_dict) is not dict:
            raise TypeError

        txid = str(self.prop_val).split(':')[-1]

        if txid in self.org_dict:
            self.prop_val = self.org_dict[txid]
        else:
            session = HTMLSession()
            r = session.get(f'https://identifiers.org/taxonomy:{txid}')
            v = r.html.find('strong', first=True)
            self.prop_val = v.text
            self.org_dict[txid] = self.prop_val
