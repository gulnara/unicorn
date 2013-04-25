import unicorn_lexer
tokens = []
token = None

global_env = {}

#
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
    def nud(self):
        return expression(100)
    def led(self, left):
        return left + expression(10)

class sub_token(Token):
    lbp = 10
    def nud(self):
        return -expression(100)
    def led(self, left):
        return left - expression(10)

class IntToken(Token):
    def __init__(self, val):
        self.val = int(val)
    def nud(self):
        return self.val

# class Symbol(Token):
#     def __init__(self, name):
#         self.name = name

#     def evaluate(self, env=global_env):
#         return env.get(self.name)

# class AssignStmt(Token):
#     def __init__(self, symbol, expr):
#         self.symbol = symbol
#         self.expr = expr

#     def evaluate(self, env=global_env):
#         env[self.symbol.name] = self.expr.evaluate(env)


# class Literal(Token):
#     def __init__(self, val):
#         self.val = val

#     def evaluate(self, env=global_env):
#         return self.val

class end_token:
        lbp = 0

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
    (r'(-)',                     sub_token),
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

def unicorn_tokenize(characters):
    global tokens, token
    tokens = unicorn_lexer.lex(characters, token_exprs)
    token = tokens.pop(0)

def next():
    global token
    if tokens:
        next_t = tokens.pop(0)
        token = next_t
        return token
    else:
        return end_token()
        # return None

def expression(rbp=0):
    global token
    t = token
    token = next()
    left = t.nud()
    while rbp < token.lbp:
        t = token
        token = next()
        left = t.led(left)
    return left

def parse():
    return expression()
   
