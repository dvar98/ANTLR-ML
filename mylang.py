import sys
from antlr4 import *
from generated.MyLangLexer import MyLangLexer
from generated.MyLangParser import MyLangParser
from MyLangInterpreter import MyLangInterpreter


def main():
    print('----- MyLang v1.0 -----\n')

    visitor = MyLangInterpreter()

    if len(sys.argv) > 1:
        try:
            input_stream = FileStream(sys.argv[1], encoding='utf-8')
            lexer = MyLangLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = MyLangParser(stream)
            tree = parser.program()  # Assuming 'program' is the entry point of your grammar
            #print(tree.toStringTree(recog=parser))
            visitor.visit(tree)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: mylang.py <source-file>")

if __name__ == '__main__':
    main()
