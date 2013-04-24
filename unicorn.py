import sys
import re

def lex(characters, token_exprs):
	pos = 0
	tokens = []
	while pos < len(characters):
		match = None
		for token_expr in token_exprs:
			pattern, token_type = token_expr
			regex = re.compile(pattern)
			match = regex.match(characters, pos)
			if match:
				text = match.group(1)
				if token_type:
					# token = (text, tag)
					token = token_type(text)
					tokens.append(token)
				break
		if not match:
			sys.stderr.write('Illegal character: %s\n' % characters[pos])
			sys.exit(1)
		else:
			pos = match.end(0)
	return tokens
	print tokens
	

# RESERVED = 'reserved'
# INT = 'int'
# STR = 'str'
# ID = 'id'

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

class operator_add_token(Token):
    lbp = 10
    def led(self, left):
        right = expression(10)
        return left + right

class IntToken(Token):
    def __init__(self, value):
        self.value = int(value)
    def nud(self):
        return self.value

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
    (r'(\+)',                    operator_add_token),
    (r'(\-)',                     RESERVED),
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

def unicorn_tokenizer(program):
	return lex(program, token_exprs)

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

def parse(program):
    global token, next
    next = unicorn_tokenizer(program).next
    token = next()
    return expression()

parse("1+1")


