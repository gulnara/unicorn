from unicorn_tokenizer import *


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

def parse(tokens):
    global token, next
    next = unicorn_tokenizer(tokens).next
    token = next()
    return expression()
