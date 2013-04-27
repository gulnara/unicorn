# run this wil along with simple_test.txt in python shell to test parser

import sys
from unicorn_tokenizer import *
import unicorn_tokenizer



if __name__ == '__main__':
	filename = sys.argv[1]
	file = open(filename)
	characters = file.read()
	file.close()

	unicorn_tokenize(characters)
	tree = parse()
#	print tree
	print tree.eval()
	print unicorn_tokenizer.global_env
	
