from blang.lexer import lex

def linereader(filename):
    # stdin buffering doesn't allow me to process each command otherwise.
    f = open(filename, buffering=1)
    line=' '
    while len(line)!=0:
        line=f.readline()
        yield line

def main():
    import sys
    args = sys.argv[1:]
    if not args:
        args = ['/proc/self/fd/0']

    for fname in args:
        for token in lex(linereader(fname)):
            print token

if __name__ == '__main__':
    exit(main())
