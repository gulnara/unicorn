import sys
from unicorn_tokenizer import *
from unicorn_parser import *



if __name__ == '__main__':
	filename = sys.argv[1]
	file = open(filename)
	characters = file.read()
	file.close()
	tokens = unicorn_tokenizer(characters)
	tree = parse(tokens)
	print tree


