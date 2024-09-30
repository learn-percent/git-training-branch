import sys
from src.add import add

if __name__ == '__main__':
    a, op, b = sys.argv[1].split(' ')
    result = ''
    if op == '+':
        result = add(a, b)
    
    print(result)