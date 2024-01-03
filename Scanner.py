from Token import Token
from TokenType import TokenType


class Scanner(object):
    def __init__(self, source: str):
        self.source = source
        self.tokens = list()

        # Start points to the first character in the lexeme being scanned
        self.start = 0

        #Current position currently being considered
        self.current = 0

        #Source line current is on to produce tokens that know their location
        self.line = 1

    #Function to check if end of source file
    def is_at_end(self):
        return self.current >= len(self.source)

    #Function to Tokenize source file
    def scan_tokens(self):

        #Construct token till EOF
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        #Append a special token to denote EOF
        self.tokens.append(Token(TokenType.EOF, None, None, self.line))
        return self.tokens

    # Return char at current and increment by 1
    def advance(self):
        output = self.source[self.current + 1]
        self.current += 1
        return output

    #Add token to the list of Tokens
    def add_token(self, token_type, literal = None):
        if not literal:
            text = self.source[self.start: self.current]
            self.tokens.append(Token(token_type, text, literal, self.line))
        else:
            self.add_token(token_type, None)

    #Scan a single character token from input file
    def scan_token(self):
        c = self.advance()

        if c == '(':
            self.add_token(TokenType.LEFT_PARENTHESIS)
        elif c == ')':
            self.add_token(TokenType.RIGHT_PARENTHESIS)
        else:
            print("Unrecognized character")
