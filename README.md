# Moorhen
A dadaist programming language

## How it works

Moorhen programs are made of english words.

Each word does one operation. Words are processed from left to right until the direction of the pointer changes.

Programs operate on a single stack of unbound integers.
There are 7 operations in the following order.

* Push a zero to the stack

* Increment the top value of the stack

* Decrement the top value of the stack

* Move the top value of the stack to the bottom of the stack

* Duplicate the top value of the stack

* If the top of the stack is non-zero skip the next word to be executed

* If the top of the stack is non-zero change the direction of the pointer

A word's operation is its md5 hash modulo 7

The program halts execution when it exits the program space.
