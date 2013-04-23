import sys
from unicorn_tokenizer import *

if __name__ == '__main__':
	filename = sys.argv[1]
	file = open(filename)
	characters = file.read()
	file.close()
	tokens = unicorn_tokenizer(characters)
	for token in tokens:
		print token