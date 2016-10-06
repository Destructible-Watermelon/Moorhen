import sys
import hashlib
from optparse import OptionParser

class Interpreter(object):
    def __init__(self, source, *args):
        self.source = source
        self.pointer = 0
        self.direction = 1
        self.stack = args


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

    #IO
    def __str__(self):
        #Depreciated
        return ' '.join(str(x) for x in self.stack)

    def ascii(self):
        return ''.join(map(lambda x:chr(x%128),self.stack))

    def decimal(self):
        return ' '.join(map(str,self.stack))

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
    parser = OptionParser()
    parser.add_option("-a","--ASCII-in",action="store_true",dest="ascii_in",help="Output as ASCII")
    parser.add_option("-A","--ASCII-out",action="store_true",dest="ascii_out",help="Input arguments as ASCII")
    parser.add_option("-c","--ASCII-io",action="store_true",dest="ascii_io",help="Input and output as ASCII")
    parser.add_option("-R","--read",action="store_true",dest="reading",help="Create a breif description of what the program does")
    options, args = parser.parse_args()
    wordList = open("ospd.txt").read().split()
    if not args:
        print "Please provide source file."
    elif options.reading:
        source = open(args[0]).read().split()
        ops = ["Push","Pop","Increment","Decrement","Roll","Duplicate","Jump","IfJump","Reverse","No-op","Out"]
        maximum = max(map(len,source))
        for word in source:
            print word.ljust(maximum)+":",ops[int(int(hashlib.md5(word).hexdigest(),16)%11)]
    else:
        code = map(lambda x:int(int(hashlib.md5(x).hexdigest(),16)%11),filter(lambda x:x.lower() in wordList,open(args[0]).read().split()))
        stacks = map(ord," ".join(args[1:])) if options.ascii_in or options.ascii_io else map(int,args[1:])
        interpreter = Interpreter(code, *stacks)
        while interpreter.step():pass
        print interpreter.ascii() if options.ascii_out or options.ascii_io else interpreter.decimal()
