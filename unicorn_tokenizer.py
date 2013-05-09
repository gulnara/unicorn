import unicorn_lexer
import random
tokens = []
token = None
loop_name = None
next_name = None

global_env = {}
loops = {}

# Defining classes of tokens.

class Token(object):
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return "<%s %r>"%(self.__class__.__name__, self.val)

class StatementToken(Token):
    def __init__(self, val):
        self.val = val

class StatementList(StatementToken):
    def __init__(self, statements):
        self.statements = statements

    def std(self):
        pass

    def eval(self):
        for stmt in self.statements:
            stmt.eval()

class ExprToken(Token):
        pass

class ShowToken(StatementToken):
    lbp = None
    def std(self):
        next()
        self.second = expression(0)
        if type(token) == ConcatToken:
            next()
            self.action = expression(0)
        else:
            self.action = None
            # next()
            # next(NewLineToken)
        next(NewLineToken)
        # next()
        return self
    def eval(self):
        if self.action is not None:
            if isinstance(self.action.eval(), int):
                print self.second.eval() + str(self.action.eval())
            else:
                print self.second.eval() + self.action.eval()
        else:
            print self.second.eval()

class NumberPromptToken(Token):
    lbp = 10
    def nud(self):
        return self
    def eval(self):
        self.val = int(raw_input())
        return self.val

class StringPromptToken(Token):
    lbp = 10
    def nud(self):
        return self
    def eval(self):
        self.val = raw_input()
        return self.val

class RandomToken(Token):
    lbp = 10
    def nud(self):
        next(UsingToken)
        self.first = expression(0)
        next(ToToken)
        self.second = expression(0)
        return self
    def eval(self):
        self.val = random.randint(self.first.eval(), self.second.eval())
        return self.val

class UsingToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass

class ToToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass

class IsToken(StatementToken):
    def std(self):
        next()
        self.conditionals = []
        self.cond = expression(0)
        next(QuestionToken)
        next(ThenToken)
        self.action = stmtlist()
        self.conditionals.append( (self.cond, self.action) )
        next(EndToken)  
        
        while type(token) == OrToken:
            next()
            self.cond = expression(0)
            next(QuestionToken)
            next(ThenToken)
            self.action = stmtlist()
            self.conditionals.append( (self.cond, self.action) )
            next(EndToken)
        if type(token) == OtherwiseToken:
            next()
            self.otherwise_action = stmtlist()
            next(EndToken)
        else:
            self.otherwise_action = None
        return self
    def eval(self): 
        for self.cond, self.action in self.conditionals:
            if self.cond.eval() == True:
                return self.action.eval()
 
        if self.otherwise_action:
            self.otherwise_action.eval()

class QuestionToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass

class ThenToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass

class OrToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass

class OtherwiseToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass

class EndToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass

class MoreToken(Token):
    lbp = 20
    def led(self, left):
        self.first = left
        self.second = expression(20)
        return self
    def eval(self):
        if self.first.eval() > self.second.eval():
            return True
        else:
            return False

class LessToken(Token):
    lbp = 20
    def led(self, left):
        self.first = left
        self.second = expression(20)
        return self
    def eval(self):
        if self.first.eval() < self.second.eval():
            return True
        else:
            return False           
class EqualToken(Token):
    lbp = 20
    def led(self, left):
        self.first = left
        self.second = expression(20)
        return self
    def eval(self):
        if self.first.eval() == self.second.eval():
            return True
        else:
            return False 

class MoreEqualToken(Token):
    lbp = 20
    def led(self, left):
        self.first = left
        self.second = expression(20)
        return self
    def eval(self):
        if self.first.eval() >= self.second.eval():
            return True
        else:
            return False 

class LessEqualToken(Token):
    lbp = 20
    def led(self, left):
        self.first = left
        self.second = expression(20)
        return self
    def eval(self):
        if self.first.eval() <= self.second.eval():
            return True
        else:
            return False 

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

class ConcatToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass


class AssignToken(Token):
    lbp = 100
    def led (self, left):
        self.first = left
        self.second = expression(10)
        return self
    def eval(self):
        global_env[self.first.val] = self.second.eval()


class LoopToken(StatementToken):
    global loop_name
    lbp = None
    def std (self):
        loop_name = next().val
        self.name = loop_name
        next()
        next(ColonToken)
        next(NewLineToken)
        self.loop_vars = []
        if type(token) == StartingToken:
            next()
            next(WithToken)
            while not type(token) == EndToken:
                self.lungs = stmtlist()
                self.loop_vars.append(self.lungs)
            next(EndToken)
        self.action = stmtlist()
        next(EndToken)
        return self
    def eval(self):
        loops[self.name] = True
        for self.lungs in self.loop_vars:
            self.lungs.eval()

        while loops[self.name]:
            self.action.eval()

class StopToken(StatementToken):
    global loop_name
    global next_name
    lbp = None
    def std(self):
        next_name = next().val
        self.name = next_name
        next()
        next(NewLineToken)
        return self
    def eval(self):
        if next_name == loop_name:
            loops[self.name] = False
            return

class ColonToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass

class StartingToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass

class WithToken(Token):
    lbp = 0
    def led(self):
        pass
    def nud(self):
        pass

class FinalToken(object):
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

# Lexer includes Reserved tokens, which have not been incorporated in the language yet.

RESERVED = ReservedToken

token_exprs = [
    (r'([ \t\r]+)',              None),
    (r'(#[^\n]*)',               None),
    (r'([0-9]+)',                IntToken),
    (r'"(.*)"',                  StringToken),
    (r"'(.*)'",                  StringToken),
    (r'(<-)',                    AssignToken),
    (r'(\?)',                    QuestionToken),
    (r'(\n+)',                   NewLineToken),
    (r'(\()',                    RESERVED),
    (r'(\))',                    RESERVED),
    (r'(;)',                     RESERVED),
    (r'(:)',                     ColonToken),
    (r'(\.)',                    RESERVED),
    (r'(\,)',                    ConcatToken),
    (r'(\!)',                    RESERVED),
    (r'(\+)',                    AddToken),
    (r'(-)',                     SubToken),
    (r'(\*)',                    MulToken),
    (r'(\/)',                    DivToken),
    (r'(<=)',                    LessEqualToken),
    (r'(>=)',                    MoreEqualToken),
    (r'(=)',                     EqualToken),
    (r'(<)',                     LessToken),
    (r'(>)',                     MoreToken),
    (r'(!=)',                    RESERVED),
    (r'(=/=)',                   RESERVED),
    (r'(and)',                   RESERVED),
    (r'(or)',                    OrToken),
    (r'(not)',                   RESERVED),
    (r'(is)',                    IsToken),
    (r'(then:(\n)+)',            ThenToken),
    (r'(loop)',                  LoopToken),
    (r'(list)',                  RESERVED),
    (r'(with(\n)+)',             WithToken),
    (r'(starting)',              StartingToken),
    (r'(otherwise:(\n)+)',       OtherwiseToken),
    (r'(show)',                  ShowToken),
    (r'(stop)',                  StopToken),
    (r'(end(\n)*)',              EndToken),
    (r'(to)',                    ToToken),
    (r'(using)',                 UsingToken),
    (r'(randomize)',             RandomToken),
    (r'(number_prompt)',         NumberPromptToken),
    (r'(string_prompt)',         StringPromptToken),
    (r'([A-Za-z][A-Za-z0-9_]*)', IdToken),    
    (r'\'',                    None),
]

# Tokenizer finds tokens in a string

def unicorn_tokenize(characters):
    global tokens, token
    tokens = unicorn_lexer.lex(characters, token_exprs)
    token = tokens.pop(0)
    # print tokens

# next() function generates new tokens for the parser.

def next(expected_token_type = None):
    global token
    if tokens:
        if expected_token_type is not None:
            if type(token) != expected_token_type:
                raise Exception("not the expected token")
        next_t = tokens.pop(0)
        token = next_t
        return token
    else:
        token = FinalToken()
        return token

# expression() function encapsulates the core of Pratt's algorithm.

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

# statement() function decides based on a token which parser to use - recursive decent or Pratt parser.

def statement():
    global token
    if isinstance(token, StatementToken):
        return token.std()
    else:
        expr = expression(0)
        next()
        if type(expr) not in [AssignToken, MoreToken, LessToken, MoreEqualToken, LessEqualToken, StringPromptToken, EqualToken, NumberPromptToken, RandomToken]:
            raise Exception("such expression doesn't exist")
        else:
            return expr



def stmtlist():
    whatever = [] 
    while type(token) != FinalToken and type(token) != EndToken:
        s = statement();
        whatever.append(s)
    stmt_list = StatementList(whatever)
    return stmt_list
    
        
def parse():
    return stmtlist()
   
