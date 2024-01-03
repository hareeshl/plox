"""
Created on Jan 3 23
@author: Hareesh

Token is a wrapper to enclose a lexeme and its associated data.
Lexeme: Character blob that represents something. Raw substrings from the sourcecode.
Type: Kind of Lexeme this represents
Literal: Runtime object corresponding to the textual representation
Line: Line number at which the Token appears
"""


class Token(object):
    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return self.type + " " + self.lexeme + " " + self.literal
