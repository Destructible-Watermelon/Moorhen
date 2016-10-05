import sys
import hashlib

class Interpreter(object):
    def __init__(self, source, *args):
        self.source = source
        self.pointer = 0
        self.direction = 1
        self.stack = map(int,args)


    def step(self):
        if 0 > self.pointer or self.pointer >= len(self.source):return False
        [
            self.push,
            self.pop,
            self.increment,
            self.decrement,
            self.roll,
            self.duplicate,
            self.jump,
            self.conjump,
            self.reverse,
            self.noOp,
            self.output,
        ][self.source[self.pointer]]()
        self.pointer += self.direction
        return True

    def __str__(self):
        return ' '.join(str(x) for x in self.stack)

    # Stack functions
    def push(self):
        self.stack.append(0)
    def pop(self):
        self.stack.pop()
    def noOp(self):
	pass
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
            self.stack= [self.stack[-1]]+self.stack[:-1]
    def duplicate(self):
        if self.stack:
            self.stack.append(self.stack[-1])
        else:
            self.stack.append(0)
    def peek(self):
        return bool(self.stack) and self.stack[-1]
    def conjump(self):
	if self.peek():
	    self.pointer += self.direction
    def jump(self):
        self.pointer += self.direction
    def reverse(self):
        self.direction *= -1
    def output(self):
	print self.peek()

if __name__ == "__main__":
    wordList = open("ospd.txt").read().split()
    if len(sys.argv) < 2:
        print "Please provide source file."
    else:
        code = map(lambda x:int(int(hashlib.md5(x).hexdigest(),16)%12),filter(lambda x:x.lower() in wordList,open(sys.argv[1]).read().split()))
        interpreter = Interpreter(code, *sys.argv[2:])
        while interpreter.step():pass
        print interpreter
