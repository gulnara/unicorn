import unicorn_lexer

RESERVED = 'reserved'
INT = 'int'
STR = 'str'
ID = 'id'

class Token(object):
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return "<%s %s>"%(self.__class__.__name__, self.val)

class IdToken(Token):
    pass

class StringToken(Token):
    pass

class ReservedToken(Token):
    pass

class add_token(Token):
    lbp = 10
    def led(self, left):
        right = expression(10)
        return left + right

class IntToken(Token):
    def __init__(self, val):
        self.val = int(val)
    def nud(self):
        return self.val

RESERVED = ReservedToken

token_exprs = [
    (r'([ \n\t]+)',              None),
    (r'(#[^\n]*)',               None),
    (r'([0-9]+)',                IntToken),
    (r'"(.*)"',                  StringToken),
    (r"'(.*)'",                  StringToken),
    (r'(<-)',                    RESERVED),
    (r'(\?)',                    RESERVED),
    (r'(\()',                    RESERVED),
    (r'(\))',                    RESERVED),
    (r'(;)',                     RESERVED),
    (r'(:)',                     RESERVED),
    (r'(\.)',                    RESERVED),
    (r'(\!)',                    RESERVED),
    (r'(\+)',                    add_token),
    (r'(-)',                     RESERVED),
    (r'(\*)',                    RESERVED),
    (r'(/)',                     RESERVED),
    (r'(<)',                     RESERVED),
    (r'(<=)',                    RESERVED),
    (r'(>)',                     RESERVED),
    (r'(>=)',                    RESERVED),
    (r'(=)',                     RESERVED),
    (r'(!=)',                    RESERVED),
    (r'(=/=)',                   RESERVED),
    (r'(and)',                   RESERVED),
    (r'(or)',                    RESERVED),
    (r'(not)',                   RESERVED),
    (r'(is)',                    RESERVED),
    (r'(then)',                  RESERVED),
    (r'(loop)',                  RESERVED),
    (r'(list)',                  RESERVED),
    (r'(starting)',              RESERVED),
    (r'(otherwise)',             RESERVED),
    (r'(show)',                  RESERVED),
    (r'(stop)',                  RESERVED),
    (r'(end)',                   RESERVED),
    (r'(to)',                    RESERVED),
    (r'(using)',                 RESERVED),
    (r'(randomize)',             RESERVED),
    (r'(prompt)',             RESERVED),
    (r'([A-Za-z][A-Za-z0-9_]*)', IdToken),    
    (r'\'',                    None),
]

def unicorn_tokenizer(characters):
	return unicorn_lexer.lex(characters, token_exprs)
