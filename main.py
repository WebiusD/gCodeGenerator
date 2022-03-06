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

    #output = open("DanaStaple.cnc")
    #output.close()

    collector = Collector(doLog=False)
    result = collector.visit(tree)
    print(result)


if __name__ == "__main__":
    main(sys.argv)
