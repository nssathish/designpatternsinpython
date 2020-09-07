"""
    The factory pattern
    -------------------
    1.Pass a parameter that provides information about what we want and 
    as a result, the wanted object is created.

    Real-world eg.,
    ---------------
    1. a storage factory based on configuration creates the handler for different storage types
        - like blob, db, key-value store, cloud storage et.,
    2. 'forms' module in Django creates different kinds of fields for the web form

    Use cases
    ---------
    1. When the object creation cannot be managed by the application because the object gets
    created in multiple places rather than in a single place/method.
    2. When we want to decouple of object creation from object usage. 
    3. To improve the performance and memory usage of the application since the objects are
    created only on demand

    Example here
    ------------
"""
import json
import xml.etree.ElementTree as etree

class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)
        
    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def dataextraction_factory(filepath: str):
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError(f"Cannot extract data from {filepath}")

    return extractor(filepath)


def extract_data_from(filepath):
    factory_obj = None

    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as ve:
        print(ve)
    
    return factory_obj


def main():
    json_factory = extract_data_from('movies.json')
    json_data = json_factory.parsed_data
    print(f"Found: {len(json_data)} movies")
    print(json_data)

    xml_factory = extract_data_from('persons.xml')
    xml_data = xml_factory.parsed_data
    botanical = xml_data.findall(f".//PLANT[BOTANICAL='canadensis']")
    print(f'Found: {len(botanical)} entries')
    for canadensises in botanical:
        common = canadensises.find('COMMON').text
        print(f'common: {common}')
        price = canadensises.find('PRICE').text
        print(f'price: {price}')

    print(xml_data)


if __name__ == "__main__":
    main()