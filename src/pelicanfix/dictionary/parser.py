import xml.etree.ElementTree as ElementTree
from typing import List

from pelicanfix.dictionary.metadata import FIXDictionary, FIXType, FIXField, FIXEnum, FIXElementRef, FIXComponent, \
    FIXRepeatingGroup, FIXFieldRef, FIXComponentRef, FIXElement, FIXHeader, FIXTrailer, FIXMessage


class FIXDictionaryParser:
    def __init__(self, spec_file):
        self.spec_file = spec_file

    def parse(self) -> FIXDictionary:
        dom = ElementTree.parse(self.spec_file)
        root = dom.getroot()

        major = int(root.attrib['major'])
        minor = int(root.attrib['minor'])
        service_pack = int(root.attrib['servicepack'])

        fields = []
        fields_elem = root.find('fields')
        for field_elem in fields_elem.findall('field'):
            number = field_elem.attrib['number']
            name = field_elem.attrib['name']
            fix_type_name = field_elem.attrib['type']
            fix_type = FIXType[fix_type_name]

            allowed_values = []
            for enum_elem in field_elem.findall('value'):
                value_enum = enum_elem.attrib['enum']
                value_desc = enum_elem.attrib['description']
                allowed_values.append(FIXEnum(value_enum, value_desc))

            field = FIXField(number, name, fix_type, allowed_values)
            fields.append(field)

        messages = []
        messages_elem = root.find('messages')
        for message_elem in messages_elem:
            name = message_elem.attrib['name']
            msg_type = message_elem.attrib['msgtype']
            category = message_elem.attrib['msgcat']
            nested_refs = FIXDictionaryParser.parse_fix_elements(message_elem)
            message = FIXMessage(name, msg_type, category, nested_refs)
            messages.append(message)

        components = []
        components_elem = root.find('components')
        for component_elem in components_elem:
            name = component_elem.attrib['name']
            nested_refs = FIXDictionaryParser.parse_fix_elements(component_elem)
            component = FIXComponent(name, nested_refs)
            components.append(component)

        header_elem = root.find('header')
        header = FIXHeader(FIXDictionaryParser.parse_fix_elements(header_elem))

        trailer_elem = root.find('trailer')
        trailer = FIXTrailer(FIXDictionaryParser.parse_fix_elements(trailer_elem))

        return FIXDictionary(major, minor, service_pack, header, trailer, messages, components, fields)

    @staticmethod
    def parse_fix_elements(root_elem: ElementTree.Element) -> List[FIXElement]:
        fix_elems = []
        for element_ref_elem in root_elem:
            name = element_ref_elem.attrib['name']
            required = element_ref_elem.attrib['required'] == 'Y'
            if element_ref_elem.tag == 'field':
                fix_elem = FIXFieldRef(name, required)
            elif element_ref_elem.tag == 'component':
                fix_elem = FIXComponentRef(name, required)
            elif element_ref_elem.tag == 'group':
                nested_refs = FIXDictionaryParser.parse_fix_elements(element_ref_elem)
                fix_elem = FIXRepeatingGroup(name, required, nested_refs)
            else:
                raise ValueError(f'Unknown FIX element tag: {element_ref_elem.tag}')

            fix_elems.append(fix_elem)

        return fix_elems
