from TokenType import TokenType

class Token:
    def __init__(self,
                 type=None,
                 lexeme="",
                 literal=None,
                 line=-1):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def toString(self):
        return f"{type} {lexeme} {literal}"

