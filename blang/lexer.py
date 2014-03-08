
def lex(lines):
    """yield a series of tokens derived from these lines."""
    for line in lines:
        yield line.rstrip()


def unlex(tokens):
    """yield a lines of tokens derived from these tokens."""
