import sys
from antlr4 import *
from generated.MyLangLexer import MyLangLexer
from generated.MyLangParser import MyLangParser
from MyLangInterpreter import MyLangInterpreter
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(str(line) + ":" + str(column) + ": syntax ERROR, " + str(msg))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print("Ambiguity ERROR, " + str(configs))

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print("Attempting full context ERROR, " + str(configs))

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print("Context ERROR, " + str(configs))

def main():
    print('----- MyLang v1.0 -----\n')

    visitor = MyLangInterpreter()

    if len(sys.argv) > 1:
        try:
            input_stream = FileStream(sys.argv[1], encoding='utf-8')
            lexer = MyLangLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = MyLangParser(stream)
            parser.addErrorListener(MyErrorListener())
            tree = parser.program()  # Assuming 'program' is the entry point of your grammar
            print(tree.toStringTree(recog=parser))
            visitor.visit(tree)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: mylang.py <source-file>")

if __name__ == '__main__':
    main()
