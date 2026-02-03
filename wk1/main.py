from lark import Lark, Transformer


grammar = """
    ?start: expr
    ?expr: expr "+" term   -> add
         | expr "-" term   -> sub
         | term
    ?term: term "*" factor -> mul
         | term "/" factor -> div
         | term "%" factor -> mod
         | factor
    ?factor: NUMBER         -> number
           | "-" factor     -> neg
           | "(" expr ")"
    %import common.NUMBER
    %import common.WS
    %ignore WS
"""


class Calculate(Transformer):
    def number(self, n):
        return float(n[0])

    def add(self, args):
        return args[0] + args[1]

    def sub(self, args):
        return args[0] - args[1]

    def mul(self, args):
        return args[0] * args[1]

    def div(self, args):
        return args[0] / args[1]

    def mod(self, args):
        return args[0] % args[1]

    def neg(self, args):
        return args[0] * -1


expressions = [
    "1 + 3 * (2 - -4) / 5",
    "-(10 * 200 + 1)",
    "5 - 3 * 4 + 1",
    "1000 / 10 / 10",
    "10 - 20 - 30 - 40",
    "10 % 3"
]

# no embedded transformer
parser = Lark(grammar)
# embedded transformer
# parser = Lark(grammar, parser="lalr", transformer=Calculate())

for expr in expressions:
    # no embedded transformer so calculate now over tree
    tree = parser.parse(expr)
    print(tree)
    # apply Calculate using .transform() which Calculate inherited from Transform class from lark lib
    result = Calculate().transform(tree)

    # with embedded transformer result is just a float already instead of the tree
    # result = parser.parse(expr)

    print(f"{expr} = {result}")
