from lark import Lark, Transformer

grammar = """
    start: value ("," value)*
    ?value: ESCAPED_STRING | SIGNED_NUMBER | BOOLEAN | UNQUOTED
    BOOLEAN: "true" | "false"
    UNQUOTED: /[^,]+/
    %import common.SIGNED_NUMBER
    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS
"""


class ToPythonList(Transformer):
    def start(self, items):
        return list(items)

    def BOOLEAN(self, s): return 1 if s == "true" else 0
    def ESCAPED_STRING(self, s): return s[1:-1]
    def UNQUOTED(self, s): return str(s)
    def SIGNED_NUMBER(self, s): return int(s)


parser = Lark(grammar)

# filename = "organizations-1000.csv"
filename = "small-test.csv"
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        tree = parser.parse(line)
        parsed = ToPythonList().transform(tree)
        # Now, get the second value (at index 1)
        print(parsed)
        print("Second value:", parsed[1])
        print()
