import sys
import re

class Book(object):
    def __init__(self, v):
        self.v = v

def read_data():
    lines = sys.stdin.read().split('\n')
    N, K = map(int, lines[0].split())
    operations = lines[1:]

    return N, K, operations

def find_max(stack, K):
    stack = stack[:-K]
    max_i, max_v, max_book = -1, 0, None
    if len(stack) == 0:
        return max_i
    for i, book in enumerate(stack):
        if book.v > max_v:
            max_i = i
            max_book = book
            max_v = book.v
    return max_i, max_book

def main():
    N, K, operations = read_data()
    stack = []

    for ope in operations:
        m = re.match('^buy (\d)+$', ope)
        if m is not None:
            v = int(m.group(1))
            print(v)
            stack.append(Book(v))
        elif ope == 'read':
            max_book_i, max_book = find_max(stack, K)
            if max_book_i < 0:
                return    # no books to read
            print(max_book.v)
            stack.remove(max_book)
            stack.append(max_book)
        else:
            raise ValueError(f'Invalid Operation {ope}')

if __name__ == '__main__':
    main()