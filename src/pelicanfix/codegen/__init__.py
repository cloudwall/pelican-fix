import os
import re
from pathlib import Path

import fire as fire
import num2words as num2words
from importlib_resources import files, as_file

from pelicanfix.dictionary.metadata import FIXDictionary
from pelicanfix.dictionary.parser import FIXDictionaryParser


class ProtocolCodeGenerator:
    def __init__(self, dictionary: FIXDictionary, to_dir: Path, base_module: str, protocol: str):
        self.dictionary = dictionary
        self.to_dir = to_dir
        self.base_module = base_module
        self.protocol = protocol

    def generate(self):
        self.to_dir.mkdir(parents=True, exist_ok=True)
        module_parts = self.base_module.split('.')
        module_path = self.to_dir.joinpath(os.path.sep.join(module_parts))
        module_path.mkdir(parents=True, exist_ok=True)

        current_path = self.to_dir
        init_path = None
        for module_part in module_parts:
            current_path = current_path.joinpath(module_part)
            init_path = current_path.joinpath('__init__.py')
            open(init_path, 'a').close()

        src_lines = list()
        src_lines.append('from enum import Enum\n')
        src_lines.append('\n')
        src_lines.append('from pelicanfix.protocol import FIXField\n')
        src_lines.append('\n')
        src_lines.append('\n')
        src_lines.append(f'class Field(Enum):\n')
        fields = self.dictionary.get_fields()
        fields.sort(key=lambda x: x.get_name())
        for field in self.dictionary.get_fields():
            src_lines.append(f'    {ProtocolCodeGenerator.to_upper_snake_case(field.get_name())} '
                             f'= FIXField(\'{field.get_name()}\', {field.get_number()})\n')
        fields = self.dictionary.get_fields()
        fields.sort(key=lambda x: x.get_name())
        for field in self.dictionary.get_fields():
            if len(field.get_allowed_values()) == 0:
                continue

            src_lines.append('\n')
            src_lines.append('\n')
            src_lines.append(f'class {field.get_name()}(Enum):\n')
            for value in field.get_allowed_values():
                src_lines.append(f'    {ProtocolCodeGenerator.to_upper_snake_case(value.get_description())} '
                                 f'= \'{value.get_enum_value()}\'\n')

        with open(init_path, 'w') as f:
            f.writelines(src_lines)

    @staticmethod
    def to_upper_snake_case(txt: str):
        txt = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
        converted = re.sub('([a-z0-9])([A-Z])', r'\1_\2', txt).upper()
        match = re.match(r'(\d+)_(.+)', converted)
        if match:
            return f'{num2words.num2words(match.group(1)).upper().replace(" ", "_")}_{match.group(2)}'
        elif re.match(r'^\d+$', converted):
            return num2words.num2words(converted).upper().replace(" ", "_").replace("-", "_")
        else:
            return converted


def main(specification: str = 'FIX42.xml', to_dir: str = './src', base_module: str = 'pelicanfix.protocol.fix42',
         protocol: str = 'FIX42'):
    source = files('pelicanfix.dictionary').joinpath(specification)
    with as_file(source) as dict_file:
        parser = FIXDictionaryParser(dict_file)
        fix_dict = parser.parse()
        code_generator = ProtocolCodeGenerator(fix_dict, Path(to_dir), base_module, protocol)
        code_generator.generate()


if __name__ == '__main__':
    fire.Fire(main)
