from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List


class FIXType(Enum):
    STRING = auto()
    CHAR = auto()
    PRICE = auto()
    INT = auto()
    AMT = auto()
    QTY = auto()
    CURRENCY = auto()
    MULTIPLEVALUESTRING = auto()
    MULTIPLESTRINGVALUE = auto()
    MULTIPLECHARVALUE = auto()
    EXCHANGE = auto()
    UTCTIMESTAMP = auto()
    BOOLEAN = auto()
    LOCALMKTDATE = auto()
    DATA = auto()
    FLOAT = auto()
    PRICEOFFSET = auto()
    MONTHYEAR = auto()
    DAYOFMONTH = auto()
    UTCDATE = auto()
    UTCDATEONLY = auto()
    UTCTIMEONLY = auto()
    NUMINGROUP = auto()
    PERCENTAGE = auto()
    SEQNUM = auto()
    LENGTH = auto()
    COUNTRY = auto()
    TZTIMEONLY = auto()
    TZTIMESTAMP = auto()
    XMLDATA = auto()
    LANGUAGE = auto()


class FIXEnum:
    def __init__(self, enum_value: str, description: str):
        self.enum_value = enum_value
        self.description = description

    def get_enum_value(self) -> str:
        return self.enum_value

    def get_description(self) -> str:
        return self.description


class FIXDictionary:
    pass


class FIXElement(ABC):
    @abstractmethod
    def resolve(self, dictionary: FIXDictionary):
        pass


class FIXElementRef(FIXElement, ABC):
    def __init__(self, name: str, required: bool):
        self.name = name
        self.required = required
        self.element = None

    def get_name(self) -> str:
        return self.name

    def is_required(self) -> bool:
        return self.required


class FIXField:
    def __init__(self, number: int, name: str, fix_type: FIXType, allowed_values: List[FIXEnum] = None):
        self.name = name
        self.number = number
        self.fix_type = fix_type
        self.allowed_values = allowed_values
        self.allowed_value_lookup = {x.get_enum_value(): x for x in allowed_values}

    def get_name(self) -> str:
        return self.name

    def get_number(self) -> int:
        return self.number

    def get_fix_type(self) -> FIXType:
        return self.fix_type

    def get_allowed_values(self) -> List[FIXEnum]:
        return self.allowed_values

    def is_allowed_value(self, value):
        if self.allowed_values is None or len(self.allowed_values) == 0:
            return True
        else:
            return value in self.allowed_value_lookup


class FIXFieldRef(FIXElementRef):
    def __init__(self, name: str, required: bool):
        super().__init__(name, required)
        self.field = None

    def resolve(self, dictionary: FIXDictionary):
        self.field = dictionary.get_field(self.get_name())

    def get_field(self) -> FIXField:
        return self.field


class FIXContainer(FIXElement):
    def __init__(self, elements: List[FIXElement]):
        self.elements = elements

    def get_elements(self) -> List[FIXElement]:
        return self.elements

    def resolve(self, dictionary: FIXDictionary):
        for element in self.elements:
            element.resolve(dictionary)


class FIXHeader(FIXContainer):
    def __init__(self, elements: List[FIXElement]):
        super().__init__(elements)


class FIXTrailer(FIXContainer):
    def __init__(self, elements: List[FIXElement]):
        super().__init__(elements)


class FIXComponent(FIXContainer):
    def __init__(self, name: str, elements: List[FIXElement]):
        super().__init__(elements)
        self.name = name

    def get_name(self):
        return self.name


class FIXComponentRef(FIXElementRef):
    def __init__(self, name: str, required: bool):
        super().__init__(name, required)
        self.component = None

    def resolve(self, dictionary: FIXDictionary):
        # noinspection PyUnresolvedReferences
        self.component = dictionary.get_component(self.get_name())

    def get_component(self) -> FIXComponent:
        return self.component


class FIXRepeatingGroup(FIXContainer):
    def __init__(self, name: str, required: bool, elements: List[FIXElement]):
        super().__init__(elements)
        self.name = name
        self.required = required

    def get_name(self) -> str:
        return self.name

    def is_required(self) -> bool:
        return self.required


class FIXMessage(FIXContainer):
    def __init__(self, name: str, msg_type: str, msg_category: str, elements: List[FIXElement]):
        super().__init__(elements)
        self.name = name
        self.msg_type = msg_type
        self.msg_category = msg_category

    def get_name(self) -> str:
        return self.name

    def get_msg_type(self) -> str:
        return self.msg_type

    def get_msg_category(self) -> str:
        return self.msg_category


# noinspection PyRedeclaration
class FIXDictionary:
    def __init__(self, major: int, minor: int, service_pack: int, header: FIXHeader, trailer: FIXTrailer,
                 messages: List[FIXMessage], components: List[FIXComponent], fields: List[FIXField]):
        self.major = major
        self.minor = minor
        self.service_pack = service_pack
        self.header = header
        self.trailer = trailer
        self.messages = messages
        self.components = components
        self.fields = fields

        self.messages_by_name = {x.get_name(): x for x in self.messages}
        self.components_by_name = {x.get_name(): x for x in self.components}
        self.fields_by_name = {x.get_name(): x for x in self.fields}

        self.header.resolve(self)
        self.trailer.resolve(self)
        for message in messages:
            message.resolve(self)
        for component in components:
            component.resolve(self)

    def get_major(self) -> int:
        return self.major

    def get_minor(self) -> int:
        return self.minor

    def get_service_pack(self) -> int:
        return self.service_pack

    def get_header(self) -> FIXHeader:
        return self.header

    def get_trailer(self) -> FIXTrailer:
        return self.trailer

    def get_message(self, msg_type: str) -> FIXMessage:
        return self.messages_by_name[msg_type]

    def get_messages(self) -> List[FIXMessage]:
        return self.messages

    def get_component(self, name: str) -> FIXComponent:
        return self.components_by_name[name]

    def get_components(self) -> List[FIXComponent]:
        return self.components

    def get_field(self, name: str) -> FIXField:
        return self.fields_by_name[name]

    def get_fields(self) -> List[FIXField]:
        return self.fields
