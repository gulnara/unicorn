import unicorn_lexer
tokens = []
token = None

global_env = {}

class Token(object):
    def __init__(self, val):
        self.val = val

#    def __repr__(self):
#        return "<%s %s>"%(self.__class__.__name__, self.val)

class StatementToken(Token):
    def __init__(self, val):
        self.val = val

class ExprToken(Token):
        pass

class ShowToken(StatementToken):
    lbp = None
    def std(self):
        next()
        self.second = expression(0)
        next(NewLineToken)
        return self
    def eval(self):
        print self.second.eval()
       

# class IsToken(StatementToken):
#         def std(self):
#                 self.first = expression(0)
#                 next(q_mark)
#                 next(then)
#                 self.second = stmt_list()
#                 next(endif)

class IdToken(Token):
    lbp = 10
    def nud (self):
        return self
    def eval(self):
        return global_env[self.val]

class StringToken(Token):
    def nud(self):
        return self
    def eval(self):
        return self.val

class ReservedToken(Token):
    pass

class AddToken(Token):
    lbp = 20
    def nud(self):
        return expression(100)
    def led(self, left):
        self.first = left
        self.second = expression(20)
        return self
    def eval(self):
        return self.first.eval() + self.second.eval()

class SubToken(Token):
    lbp = 20
    def nud(self):
        return -expression(100)
    def led(self, left):
        self.first = left
        self.second = expression(20)
        return self
    def eval(self):
        return self.first.eval() - self.second.eval()

class MulToken(Token):
    lbp = 30
    def led(self, left):
        self.first = left
        self.second = expression(30)
        return self
    def eval(self):
        return self.first.eval() * self.second.eval()

class DivToken(Token):
    lbp = 30
    def led(self, left):
        self.first = left
        self.second = expression(30)
        return self 
    def eval(self):
        return self.first.eval() / self.second.eval()

class IntToken(Token):
    def __init__(self, val):
        self.val = int(val)
    def nud(self):
        return self
    def eval(self):
        return self.val


        
class AssignToken(Token):
    lbp = 100
    def led (self, left):
        self.first = left
        self.second = expression(10)
        return self
    def eval(self):
        global_env[self.first.val] = self.second.eval()

class EndToken(object):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass


class NewLineToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass


RESERVED = ReservedToken

token_exprs = [
    (r'([ \t\r]+)',            None),
    (r'(#[^\n]*)',               None),
    (r'([0-9]+)',                IntToken),
    (r'"(.*)"',                  StringToken),
    (r"'(.*)'",                  StringToken),
    (r'(<-)',                    AssignToken),
    (r'(\?)',                    RESERVED),
    (r'(\n)',                    NewLineToken),
    (r'(\()',                    RESERVED),
    (r'(\))',                    RESERVED),
    (r'(;)',                     RESERVED),
    (r'(:)',                     RESERVED),
    (r'(\.)',                    RESERVED),
    (r'(\!)',                    RESERVED),
    (r'(\+)',                    AddToken),
    (r'(-)',                     SubToken),
    (r'(\*)',                    MulToken),
    (r'(\/)',                    DivToken),
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
    (r'(show)',                  ShowToken),
    (r'(stop)',                  RESERVED),
    (r'(end)',                   RESERVED),
    (r'(to)',                    RESERVED),
    (r'(using)',                 RESERVED),
    (r'(randomize)',             RESERVED),
    (r'(prompt)',                RESERVED),
    (r'([A-Za-z][A-Za-z0-9_]*)', IdToken),    
    (r'\'',                    None),
]

def unicorn_tokenize(characters):
    global tokens, token
    tokens = unicorn_lexer.lex(characters, token_exprs)
    token = tokens.pop(0)

def next(expected_token_type = None):
    global token

    if tokens:
        if expected_token_type is not None:
            if type(token) != expected_token_type:
                raise Exception("OMG THIS SUCKS")
        next_t = tokens.pop(0)
        token = next_t
        return token
    else:
        return EndToken()

def expression(rbp=0):
    global token
    t = token
    token = next()
    left = t.nud()
    if token.lbp is not None:

        while rbp < token.lbp:
            t = token
            token = next()
            left = t.led(left)
    else:
        statement()
    return left


def statement():
    global token
    if isinstance(token, StatementToken):
        return token.std()
    else:
        expr = expression(0)
        next(NewLineToken)
        if type(expr) not in [AssignToken]:
            raise Exception("OMG THIS SUCKS")
        else:
            return expr

class StatementList(StatementToken):
    def __init__(self, statements):
        self.statements = statements

    def std(self):
        pass

    def eval(self):
        for stmt in self.statements:
            stmt.eval()

def stmtlist():
    whatever = [] 
    while type(token) != EndToken:
        s = statement();
        whatever.append(s)

    stmt_list = StatementList(whatever)
    return stmt_list
    
        
def parse():
    return stmtlist()
   
