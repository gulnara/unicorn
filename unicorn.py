#!/usr/bin/env python

# Tokens are hard-coded, but the parser executes simple assignemtn and print statement.
global_env = {}

class ParseNode(object):
	def eval(self):
		pass

class Expr(ParseNode):
	pass

class Stmt(ParseNode):
	pass

class Symbol(Expr):
	def __init__(self, name):
		self.name = name

	def evaluate(self, env=global_env):
		return env.get(self.name)

class AssignStmt(Stmt):
	def __init__(self, symbol, expr):
		self.symbol = symbol
		self.expr = expr

	def evaluate(self, env=global_env):
		env[self.symbol.name] = self.expr.evaluate(env)


class Literal(Expr):
	def __init__(self, val):
		self.val = val

	def evaluate(self, env=global_env):
		return self.val

class ShowStmt(Stmt):
	def __init__(self, param):
		self.param = param

	def evaluate(self, env=global_env):
		print self.param.evaluate(env)

class Program(ParseNode):
	def __init__(self, instructions):
		self.instructions = instructions

	def evaluate(self, env=global_env):
		for instruction in self.instructions:
			instruction.evaluate(env)


class Token(object):
	def __init__(self, val):
		self.val = val
class StringToken(Token):
	pass
class SymbolToken(Token):
	pass
class QuoteToken(Token):
	pass
class NewlineToken(Token):
	pass

if __name__ == "__main__":
	"""
	x <- "Hello World"
	show x
	"""

	sym = Symbol("x")
	l = Literal("Hello World")
	assign = AssignStmt(sym, l)

	sym = Symbol("x")
	s = ShowStmt(sym)

	instructions  = [assign, s]
	p = Program(instructions)

	p.evaluate()

# [SymbolToken("x"), AssignToken(), QuoteToken(), StringToken("Hello World")...]

	# def evaluate(x, env=global_env):
# 	#Evaluate the expression in the environement
# 	if isinstance(x, ShowStmt):
# 		print evaluate(x.param)
# 	elif isinstance(x, Literal):
# 		return x.val
# 	elif isinstance(x, Program):
# 		for stmt in x.instructions:
# 			evaluate(stmt)
# 	elif isinstance(x, AssignStmt):
# 		sym = x.symbol
# 		env[sym.name] = evaluate(x.expr)
# 	elif isinstance(x, Symbol):
# 		return env.get(x.name)

	# elif isa(x, Conditional):
	# 	if eval(x.test):
	# 		return eval(x.conseq)
	# 	else:
	# 		return eval(x.alt)

# class Conditional(Stmt):
# 	def __init__(self, test, conseq, alt):
# 		self.test = test
# 		self.conseq = conseq
# 		self.alt = alt	
