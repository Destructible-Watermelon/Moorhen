import sys
import hashlib

class Stack(object):
	def __init__(self,*contents):
		self.contents = contents

class Interpreter(object):
	#Initializer
	def __init__(self,source,*args):
		self.source = source
		self.stack = map(int,args)
		self.pointer = 0
		self.direction = 1
	#Operations
	def roll(self):
		if self.stack: self.stack = self.stack[1:]+[self.stack[0]]
	def flip(self):
		self.stack = self.stack[::-1]
	def add(self):
		if len(self.stack) > 1: self.stack = self.stack[:-2]+[self.stack[-2]+self.stack[-1]]
		if not self.stack: self.stack = [0]
	def sub(self): 
		if len(self.stack) > 1: self.stack = self.stack[:-2]+[self.stack[-2]-self.stack[-1]]
		if not self.stack: self.stack = [0]
	def clone(self):
		if self.stack: self.stack = self.stack + [self.stack[-1]]
	def pop(self):
		if self.stack: self.stack = self.stack[:-1]
	def decr(self):
		if self.stack: self.stack[-1] -= 1
		else: self.stack = [-1]
	def reverse(self):
		direction *= -1
	def jump(self):
		pointer += direction
	#Public functions
	def run(self):
		ops = [self.roll,self.flip,self.add,self.sub,self.clone,self.pop,self.decr,self.reverse,self.jump]
		for codel in self.source:
			ops[int(codel.hexdigest(),16)%len(ops)]()
	def step(self):
		self.run()
		self.pointer += self.direction
		return 0 <= self.pointer < len(self.source)
	def __str__(self):
		return "%s "*len(self.stack) % self.stack

if __name__ == "__main__":
	dict = open("ospd.txt").read().split()
	code = map(hashlib.md5,filter(lambda x:x in dict,open(sys.argv[1]).read().split()))
	interpreter = Interpreter(code, *sys.argv[2:])
	while interpreter.step():pass
	print interpreter
