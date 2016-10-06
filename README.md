# Moorhen
A dadaist programming language

## How it works

Moorhen programs are made of english words.

Each word does one operation. Words are processed from left to right until the direction of the pointer changes.

Programs operate on a single stack of unbound integers.

At the start of the program, it takes input through an unbounded amount of arguments. At the end, it will output the stack, each item on stack joined by spaces. It doesn't do ascii output.

There are 11 operations in the following order.

* Push a zero to the stack

* Pop the top value of the stack

* Increment the top value of the stack

* Decrement the top value of the stack

* Move the top value of the stack to the bottom of the stack

* Duplicate the top value of the stack

* Skip the next word to be executed

* If the top of the stack is non-zero skip the next word to be executed

* Change the direction of the pointer

* Do nothing

* Output the top of the stack

A word's operation is its md5 hash modulo 11

The program halts execution when it exits the program space.
