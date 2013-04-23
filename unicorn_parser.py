class Result:
	def __init__(self, value, pos):
		self.value = value
		self.pos = pos


	def __repr__(self):
		return 'Result(%s, %d)' % (self.value, self.pos)

class Parser:
	def __call__(self, tokens, pos):
		return None #subclasses will override this

	def __add__(self, other):
		return Concat(self, other)

	def __mul__(self, other):
        return Exp(self, other)

    def __or__(self, other):
        return Alternate(self, other)

    def __xor__(self, function):
        return Process(self, function)

class Reserved(Parser):
	def __init__(self, value, tag):
		self.value = value
		self.tag = tag

	 def __call__(self, tokens, pos):
        if pos < len(tokens) and \
           tokens[pos][0] == self.value and \
           tokens[pos][1] is self.tag:
            return Result(tokens[pos][0], pos + 1)
        else:
            return None

class Tag(Parser):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][1] is self.tag:
            return Result(tokens[pos][0], pos + 1)
        else:
            return None