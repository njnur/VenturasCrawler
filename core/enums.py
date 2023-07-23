from enum import Enum, IntEnum


class BaseEnum(Enum):
    @classmethod
    def get_choices(cls):
        return [(item.name, item.value) for item in cls]


class BaseIntEnum(IntEnum):
    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def get_name(cls, value):
        return cls(value).name
