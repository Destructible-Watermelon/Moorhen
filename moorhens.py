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
        command = self.source[self.pointer]
        if command == 0:
            self.push()
        elif command == 1:
            self.increment()
        elif command == 2:
            self.decrement()
        elif command == 3:
            self.roll()
        elif command == 4:
            self.duplicate()
        elif command == 5:
            if self.peek():
                self.pointer += self.direction
        elif command == 6:
            if self.peek():
                self.direction *= -1
        self.pointer += self.direction


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
            self.stack= [self.stack[-1]]+self.stack[:-1]
    def duplicate(self):
        if self.stack:
            self.stack.append(self.stack[-1])
        else:
            self.stack.append(0)
    def peek(self):
        return bool(self.stack) and self.stack[-1]



if __name__ == "__main__":
    word_dict = open("ospd.txt").read().split()
    code = map(lambda x:int(int(hashlib.md5(x).hexdigest(),16)%7),filter(lambda x:x.lower() in word_dict,open(sys.argv[1]).read().split()))
    interpreter = Interpreter(code, *sys.argv[2:])
    while interpreter.step()==None:pass
    print ' '.join(str(x) for x in interpreter.stack)
