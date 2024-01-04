from Token import Token
from TokenType import TokenType

def is_alpha(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z')


class Scanner(object):
    # Container for all keywords in language
    keywords = {"print": TokenType.PRINT}

    def __init__(self, source: str):
        self.source = source
        self.tokens = list()

        # Start points to the first character in the lexeme being scanned
        self.start = 0

        # Current position currently being considered
        self.current = 0

        # Source line current is on to produce tokens that know their location
        self.line = 1

    # Function to check if end of source file
    def is_at_end(self):
        return self.current >= len(self.source)

    # Function to Tokenize source file
    def scan_tokens(self):

        # Construct token till EOF
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        # Append a special token to denote EOF
        self.tokens.append(Token(TokenType.EOF, None, None, self.line))
        return self.tokens

    # Return char at current and increment by 1
    def advance(self):
        output = self.source[self.current + 1]
        self.current += 1
        return output

    # Add token to the list of Tokens
    def add_token(self, token_type, literal=None):
        if not literal:
            text = self.source[self.start: self.current]
            self.tokens.append(Token(token_type, text, literal, self.line))
        else:
            self.add_token(token_type, None)

    # Scan a single character token from input file
    def scan_token(self):
        c = self.advance()

        # " denotes starting of a String literal
        if c == '"':
            self.string()
        if is_alpha(c):
            self.identifier()

    def string(self):
        while self.peek() != '"' and not is_alpha(self):
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        # Account for closing "
        self.advance()
        value = self.source[self.start + 1:self.current - 1]
        self.add_token(TokenType.STRING, value)

    def identifier(self):
        while is_alpha(self.peek()):
            self.advance()

        text = self.source[self.start: self.current]
        type = self.keywords.get(text)
        if not type:
            type = TokenType.IDENTIFIER
        self.add_token(type)

    def peek(self) -> object:
        if self.is_at_end():
            return '\0'
        return self.source[self.current]
