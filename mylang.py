import sys
from antlr4 import *
from generated.MyLangLexer import MyLangLexer
from generated.MyLangParser import MyLangParser
from MyLangInterpreter import MyLangInterpreter


def main():
    input_file = sys.argv[1]
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)
    tree = parser.program()

    interpreter = MyLangInterpreter()
    interpreter.visit(tree)


if __name__ == "__main__":
    main()
