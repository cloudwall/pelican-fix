from importlib_resources import files, as_file

from pelicanfix.dictionary.metadata import FIXFieldRef, FIXComponentRef, FIXRepeatingGroup
from pelicanfix.dictionary.parser import FIXDictionaryParser


def print_fields(elements, prefix=''):
    for element in elements:
        if isinstance(element, FIXFieldRef):
            print(prefix + element.get_field().get_name())
        elif isinstance(element, FIXComponentRef):
            print_fields(element.get_component().get_elements(), prefix)
        elif isinstance(element, FIXRepeatingGroup):
            print(f'+ {element.get_name()}')
            print_fields(element.get_elements(), prefix='  ')


def main():
    source = files('pelicanfix.dictionary').joinpath('FIX44.xml')
    with as_file(source) as dict_file:
        parser = FIXDictionaryParser(dict_file)
        fix_dict = parser.parse()

        header = fix_dict.get_header()
        msg = fix_dict.get_message('NewOrderSingle')
        trailer = fix_dict.get_trailer()

        print_fields(header.get_elements())
        print('------------')
        print_fields(msg.get_elements())
        print('------------')
        print_fields(trailer.get_elements())


if __name__ == '__main__':
    main()
