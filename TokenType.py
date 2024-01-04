from enum import Enum, auto


class TokenType(Enum):
    #Keywords
    PRINT = auto()

    #Literals
    IDENTIFIER = auto()
    STRING = auto()
    EOF = auto()
