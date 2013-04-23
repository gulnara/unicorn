import unicorn_lexer

RESERVED = 'RESERVED'
INT = 'INT'
STR = 'STR'
ID = 'ID'


token_exprs = [
    (r'([ \n\t]+)',              None),
    (r'(#[^\n]*)',               None),
    (r'([0-9]+)',                INT),
    (r'"(.*)"',                  STR),
    (r"'(.*)'",                  STR),
    (r'(<-)',                    RESERVED),
    (r'(\?)',                    RESERVED),
    (r'(\()',                    RESERVED),
    (r'(\))',                    RESERVED),
    (r'(;)',                     RESERVED),
    (r'(:)',                     RESERVED),
    (r'(\.)',                    RESERVED),
    (r'(\!)',                    RESERVED),
    (r'(\+)',                    RESERVED),
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
    (r'([A-Za-z][A-Za-z0-9_]*)', ID),    
    (r'\'',                    None),
]

def unicorn_tokenizer(characters):
	return unicorn_lexer.lex(characters, token_exprs)
