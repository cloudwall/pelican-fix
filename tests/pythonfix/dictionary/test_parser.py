from importlib_resources import files, as_file

from pelicanfix.dictionary.parser import FIXDictionaryParser


def test_parse_fix42():
    source = files('pelicanfix.dictionary').joinpath('FIX42.xml')
    with as_file(source) as dict_file:
        parser = FIXDictionaryParser(dict_file)
        fix_dict = parser.parse()
        assert fix_dict.major == 4
        assert fix_dict.minor == 2
        assert fix_dict.service_pack == 0

        msg = fix_dict.get_message('NewOrderSingle')
        assert msg.get_msg_type() == 'D'
        assert msg.get_msg_category() == 'app'
        assert len(msg.get_elements()) == 71


def test_parse_fix44():
    source = files('pelicanfix.dictionary').joinpath('FIX44.xml')
    with as_file(source) as dict_file:
        parser = FIXDictionaryParser(dict_file)
        fix_dict = parser.parse()
        assert fix_dict.major == 4
        assert fix_dict.minor == 4
        assert fix_dict.service_pack == 0

        msg = fix_dict.get_message('NewOrderSingle')
        assert msg.get_msg_type() == 'D'
        assert msg.get_msg_category() == 'app'
        assert len(msg.get_elements()) == 76


def test_parse_fix50():
    source = files('pelicanfix.dictionary').joinpath('FIX50.xml')
    with as_file(source) as dict_file:
        parser = FIXDictionaryParser(dict_file)
        fix_dict = parser.parse()
        assert fix_dict.major == 5
        assert fix_dict.minor == 0
        assert fix_dict.service_pack == 0

        msg = fix_dict.get_message('NewOrderSingle')
        assert msg.get_msg_type() == 'D'
        assert msg.get_msg_category() == 'app'
        assert len(msg.get_elements()) == 92

