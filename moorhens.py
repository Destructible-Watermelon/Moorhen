import sys
import hashlib

class DataStructure(object):
	def __init__(self,args):
		self.stack = args
	def push(self):
		self.stack.append(0)
	def increment(self):
		if self.stack:
			self.stack[-1] += 1
		else:
			self.stack.append(1)
	def decrement(self):
		if self.stack:
			self.stack[-1] -= 1
		else:
			self.stack.append(-1)
	def roll(self):
		if self.stack:
			self.stack = self.stack[-1] + self.stack[:-1]
	def duplicate(self):
		if self.stack:
			self.stack = self.stack + self.stack[-1]
		else:
			self.stack.append(0)
	def peak(self):
		return bool(self.stack) and self.stack[-1]
	def __str__(self):
		return " ".join(map(str,self.stack))

class Interpreter(object):
	def __init__(self, source, args):
		self.source = map(lambda x: int(x%7),source)
		print self.source
		self.pointer = 0
		self.direction = 1
		self.data = DataStructure(map(int,args))
	def step(self):
		if 0 > self.pointer > len(self.source):return False
		command = self.source[self.pointer]
		if command == 0:
			self.data.push()
			self.pointer += self.direction
		elif command == 1:
			self.data.increment()
			self.pointer += self.direction
		elif command == 2:
			self.data.decrement()
			self.pointer += self.direction
		elif command == 3:
			self.data.roll()
			self.pointer += self.direction
		elif command == 4:
			self.data.duplicate()
			self.pointer += self.direction
		elif command == 5:
			self.pointer += self.direction
			if self.data.peak:
				self.pointer += self.direction
		elif command == 6:
			if self.data.peak:
				self.direction *= -1
			self.pointer += self.direction
	def __str__(self):
		return str(self.data)
		

def hash(string):
	hashObject = hashlib.md5()
	hashObject.update(string)
	return int(hashObject.hexdigest(),16)


if __name__ == "__main__":
	dict = open("ospd.txt").read().split()
	code = map(hash,filter(lambda x:x in dict,open(sys.argv[1]).read().split()))
	interpreter = Interpreter(code, *sys.argv[2:])
	while interpreter.step():pass
	print interpreter
