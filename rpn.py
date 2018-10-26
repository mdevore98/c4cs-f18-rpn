#!/usr/bin/env python3

def calculate(arg):
    stack = []

    tokens = arg.split()

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()
            result = val1 + val2

def main():
    while True:
        calculate(input('rpn calc> '))

if __name__ ==  '__main__':
    main()
