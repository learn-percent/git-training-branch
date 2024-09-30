import sys
from src.add import add
from src.subtraction import subtraction
from src.division import division

if __name__ == '__main__':
    a, op, b = sys.argv[1].split(' ')
    result = ''
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtraction(a, b)
    elif op == '/':
        result = division(a, b)
    
    print(result)