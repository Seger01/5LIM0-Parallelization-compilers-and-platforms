from lark import Lark, Transformer

grammar = """
    start: expr
    ?expr: expr "+" factor -> add
         | expr "-" factor -> min
         | factor
    ?factor: factor "*" term -> mult
         | factor "/" term -> div
         | term
    ?term: NUMBER
         | "-" term -> neg
         | "(" expr ")"
    %import common.NUMBER
    %import common.WS
    %ignore WS
"""


class Calculate(Transformer):
    def start(self, args):
        return args[0]

    def NUMBER(self, args):
        return int(args)

    def add(self, args):
        return args[0] + args[1]

    def min(self, args):
        return args[0] - args[1]

    def mult(self, args):
        return args[0] * args[1]

    def div(self, args):
        return args[0] / args[1]

    def neg(self, args):
        return -1 * args[0]


expressions = [
    "1 + 3 * (2 - -4) / 5",
    "-(10 * 200 + 1)",
    "5 - 3 * 4 + 1",
    "1000 / 10 / 10",
    "10 - 20 - 30 - 40",
    "10 + 3"
]

parser = Lark(grammar)

for expr in expressions:
    tree = parser.parse(expr)
    result = Calculate().transform(tree)
    print(f"{expr} = {result}")
