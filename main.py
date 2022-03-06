import sys
from antlr4 import *
from gen.agCodeLexer import agCodeLexer
from gen.agCodeParser import agCodeParser
from Collector import Collector


def main(argv):
    inputFs = FileStream(argv[1])
    lexer = agCodeLexer(inputFs)
    stream = CommonTokenStream(lexer)
    parser = agCodeParser(stream)
    tree = parser.prog()

    output = open("DanaStack.cnc", "w")
    collector = Collector(doLog=False)
    gCode = collector.visit(tree)
    print(gCode)
    output.write(gCode)

    output.close()


if __name__ == "__main__":
    main(sys.argv)
