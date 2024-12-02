# Generated from MyLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,346,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,4,0,36,8,0,11,0,12,0,37,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,2,1,2,
        1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,81,8,5,10,5,12,5,84,
        9,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
        4,7,101,8,7,11,7,12,7,102,1,7,1,7,4,7,107,8,7,11,7,12,7,108,3,7,
        111,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,3,9,130,8,9,1,9,1,9,1,9,1,9,1,9,5,9,137,8,9,10,9,12,
        9,140,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,285,8,10,1,11,1,11,1,11,1,11,5,11,291,8,11,10,11,
        12,11,294,9,11,3,11,296,8,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,
        304,8,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,315,8,
        13,1,13,1,13,4,13,319,8,13,11,13,12,13,320,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,3,14,330,8,14,1,15,1,15,1,15,1,15,4,15,336,8,15,11,
        15,12,15,337,1,15,1,15,1,16,1,16,1,16,1,16,1,16,0,1,18,17,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,4,1,0,8,9,1,0,14,20,1,
        0,14,17,1,0,54,57,383,0,35,1,0,0,0,2,50,1,0,0,0,4,52,1,0,0,0,6,65,
        1,0,0,0,8,70,1,0,0,0,10,73,1,0,0,0,12,88,1,0,0,0,14,96,1,0,0,0,16,
        112,1,0,0,0,18,129,1,0,0,0,20,284,1,0,0,0,22,303,1,0,0,0,24,305,
        1,0,0,0,26,309,1,0,0,0,28,324,1,0,0,0,30,331,1,0,0,0,32,341,1,0,
        0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,39,1,0,0,0,39,40,5,0,0,1,40,1,1,0,0,0,41,51,3,6,3,0,42,
        51,3,4,2,0,43,51,3,8,4,0,44,51,3,10,5,0,45,51,3,12,6,0,46,51,3,26,
        13,0,47,51,3,14,7,0,48,51,3,16,8,0,49,51,3,30,15,0,50,41,1,0,0,0,
        50,42,1,0,0,0,50,43,1,0,0,0,50,44,1,0,0,0,50,45,1,0,0,0,50,46,1,
        0,0,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,51,3,1,0,0,0,52,
        53,5,1,0,0,53,54,5,2,0,0,54,59,3,18,9,0,55,56,5,3,0,0,56,58,3,18,
        9,0,57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,
        1,0,0,0,61,59,1,0,0,0,62,63,5,4,0,0,63,64,5,5,0,0,64,5,1,0,0,0,65,
        66,5,58,0,0,66,67,5,6,0,0,67,68,3,18,9,0,68,69,5,5,0,0,69,7,1,0,
        0,0,70,71,3,18,9,0,71,72,5,5,0,0,72,9,1,0,0,0,73,74,5,7,0,0,74,75,
        5,2,0,0,75,76,5,58,0,0,76,77,5,3,0,0,77,82,5,58,0,0,78,79,5,3,0,
        0,79,81,5,60,0,0,80,78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,
        1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,5,4,0,0,86,87,5,5,0,0,
        87,11,1,0,0,0,88,89,7,0,0,0,89,90,5,2,0,0,90,91,5,60,0,0,91,92,5,
        3,0,0,92,93,5,60,0,0,93,94,5,4,0,0,94,95,5,5,0,0,95,13,1,0,0,0,96,
        97,5,10,0,0,97,98,3,32,16,0,98,100,5,11,0,0,99,101,3,2,1,0,100,99,
        1,0,0,0,101,102,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,110,
        1,0,0,0,104,106,5,12,0,0,105,107,3,2,1,0,106,105,1,0,0,0,107,108,
        1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,104,
        1,0,0,0,110,111,1,0,0,0,111,15,1,0,0,0,112,113,5,13,0,0,113,114,
        5,2,0,0,114,115,5,58,0,0,115,116,5,3,0,0,116,117,5,58,0,0,117,118,
        5,4,0,0,118,119,5,5,0,0,119,17,1,0,0,0,120,121,6,9,-1,0,121,130,
        3,24,12,0,122,130,3,22,11,0,123,130,5,58,0,0,124,130,5,59,0,0,125,
        130,5,60,0,0,126,127,5,20,0,0,127,130,3,18,9,2,128,130,3,20,10,0,
        129,120,1,0,0,0,129,122,1,0,0,0,129,123,1,0,0,0,129,124,1,0,0,0,
        129,125,1,0,0,0,129,126,1,0,0,0,129,128,1,0,0,0,130,138,1,0,0,0,
        131,132,10,9,0,0,132,133,7,1,0,0,133,137,3,18,9,10,134,135,10,3,
        0,0,135,137,5,19,0,0,136,131,1,0,0,0,136,134,1,0,0,0,137,140,1,0,
        0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,19,1,0,0,0,140,138,1,0,0,
        0,141,142,5,21,0,0,142,143,5,2,0,0,143,144,3,18,9,0,144,145,5,4,
        0,0,145,285,1,0,0,0,146,147,5,22,0,0,147,148,5,2,0,0,148,149,3,18,
        9,0,149,150,5,4,0,0,150,285,1,0,0,0,151,152,5,23,0,0,152,153,5,2,
        0,0,153,154,3,18,9,0,154,155,5,4,0,0,155,285,1,0,0,0,156,157,5,24,
        0,0,157,158,5,2,0,0,158,159,3,18,9,0,159,160,5,4,0,0,160,285,1,0,
        0,0,161,162,5,25,0,0,162,163,5,2,0,0,163,164,3,18,9,0,164,165,5,
        4,0,0,165,285,1,0,0,0,166,167,5,26,0,0,167,168,5,2,0,0,168,169,3,
        18,9,0,169,170,5,4,0,0,170,285,1,0,0,0,171,172,5,27,0,0,172,173,
        5,2,0,0,173,174,3,18,9,0,174,175,5,3,0,0,175,176,3,18,9,0,176,177,
        5,4,0,0,177,285,1,0,0,0,178,179,5,28,0,0,179,180,5,2,0,0,180,181,
        3,18,9,0,181,182,5,4,0,0,182,285,1,0,0,0,183,184,5,29,0,0,184,185,
        5,2,0,0,185,186,3,18,9,0,186,187,5,4,0,0,187,285,1,0,0,0,188,189,
        5,30,0,0,189,190,5,2,0,0,190,191,3,18,9,0,191,192,5,4,0,0,192,285,
        1,0,0,0,193,194,5,31,0,0,194,195,5,2,0,0,195,196,3,18,9,0,196,197,
        5,4,0,0,197,285,1,0,0,0,198,199,5,32,0,0,199,200,5,2,0,0,200,201,
        3,18,9,0,201,202,5,4,0,0,202,285,1,0,0,0,203,204,5,33,0,0,204,205,
        5,2,0,0,205,206,3,18,9,0,206,207,5,4,0,0,207,285,1,0,0,0,208,209,
        5,34,0,0,209,210,5,2,0,0,210,211,3,18,9,0,211,212,5,4,0,0,212,285,
        1,0,0,0,213,214,5,35,0,0,214,215,5,2,0,0,215,216,3,18,9,0,216,217,
        5,3,0,0,217,218,3,18,9,0,218,219,5,4,0,0,219,285,1,0,0,0,220,221,
        5,36,0,0,221,222,5,2,0,0,222,223,3,18,9,0,223,224,5,4,0,0,224,285,
        1,0,0,0,225,226,5,37,0,0,226,227,5,2,0,0,227,228,3,18,9,0,228,229,
        5,4,0,0,229,285,1,0,0,0,230,231,5,38,0,0,231,232,5,2,0,0,232,233,
        3,18,9,0,233,234,5,4,0,0,234,285,1,0,0,0,235,236,5,39,0,0,236,237,
        5,2,0,0,237,238,3,18,9,0,238,239,5,4,0,0,239,285,1,0,0,0,240,241,
        5,40,0,0,241,242,5,2,0,0,242,243,3,18,9,0,243,244,5,4,0,0,244,285,
        1,0,0,0,245,246,5,41,0,0,246,247,5,2,0,0,247,248,3,18,9,0,248,249,
        5,3,0,0,249,250,3,18,9,0,250,251,5,4,0,0,251,285,1,0,0,0,252,253,
        5,42,0,0,253,254,5,2,0,0,254,255,3,18,9,0,255,256,5,3,0,0,256,257,
        3,18,9,0,257,258,5,4,0,0,258,285,1,0,0,0,259,260,5,43,0,0,260,261,
        5,2,0,0,261,262,3,18,9,0,262,263,5,4,0,0,263,285,1,0,0,0,264,265,
        5,44,0,0,265,266,5,2,0,0,266,267,3,18,9,0,267,268,5,4,0,0,268,285,
        1,0,0,0,269,270,5,45,0,0,270,271,5,2,0,0,271,272,3,18,9,0,272,273,
        5,4,0,0,273,285,1,0,0,0,274,275,5,46,0,0,275,276,5,2,0,0,276,277,
        3,18,9,0,277,278,5,4,0,0,278,285,1,0,0,0,279,280,5,47,0,0,280,281,
        5,2,0,0,281,282,3,18,9,0,282,283,5,4,0,0,283,285,1,0,0,0,284,141,
        1,0,0,0,284,146,1,0,0,0,284,151,1,0,0,0,284,156,1,0,0,0,284,161,
        1,0,0,0,284,166,1,0,0,0,284,171,1,0,0,0,284,178,1,0,0,0,284,183,
        1,0,0,0,284,188,1,0,0,0,284,193,1,0,0,0,284,198,1,0,0,0,284,203,
        1,0,0,0,284,208,1,0,0,0,284,213,1,0,0,0,284,220,1,0,0,0,284,225,
        1,0,0,0,284,230,1,0,0,0,284,235,1,0,0,0,284,240,1,0,0,0,284,245,
        1,0,0,0,284,252,1,0,0,0,284,259,1,0,0,0,284,264,1,0,0,0,284,269,
        1,0,0,0,284,274,1,0,0,0,284,279,1,0,0,0,285,21,1,0,0,0,286,295,5,
        48,0,0,287,292,3,18,9,0,288,289,5,3,0,0,289,291,3,18,9,0,290,288,
        1,0,0,0,291,294,1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,296,
        1,0,0,0,294,292,1,0,0,0,295,287,1,0,0,0,295,296,1,0,0,0,296,297,
        1,0,0,0,297,304,5,49,0,0,298,299,5,58,0,0,299,300,5,48,0,0,300,301,
        3,18,9,0,301,302,5,49,0,0,302,304,1,0,0,0,303,286,1,0,0,0,303,298,
        1,0,0,0,304,23,1,0,0,0,305,306,3,22,11,0,306,307,7,2,0,0,307,308,
        3,22,11,0,308,25,1,0,0,0,309,310,5,50,0,0,310,311,5,58,0,0,311,314,
        5,51,0,0,312,315,3,28,14,0,313,315,3,18,9,0,314,312,1,0,0,0,314,
        313,1,0,0,0,315,316,1,0,0,0,316,318,5,11,0,0,317,319,3,2,1,0,318,
        317,1,0,0,0,319,320,1,0,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,
        322,1,0,0,0,322,323,5,52,0,0,323,27,1,0,0,0,324,325,3,18,9,0,325,
        326,5,3,0,0,326,329,3,18,9,0,327,328,5,3,0,0,328,330,3,18,9,0,329,
        327,1,0,0,0,329,330,1,0,0,0,330,29,1,0,0,0,331,332,5,53,0,0,332,
        333,3,32,16,0,333,335,5,11,0,0,334,336,3,2,1,0,335,334,1,0,0,0,336,
        337,1,0,0,0,337,335,1,0,0,0,337,338,1,0,0,0,338,339,1,0,0,0,339,
        340,5,52,0,0,340,31,1,0,0,0,341,342,3,18,9,0,342,343,7,3,0,0,343,
        344,3,18,9,0,344,33,1,0,0,0,18,37,50,59,82,102,108,110,129,136,138,
        284,292,295,303,314,320,329,337
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'('", "','", "')'", "';'", 
                     "'='", "'plot'", "'read'", "'write'", "'if'", "':'", 
                     "'else:'", "'regression'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'T'", "'inv'", "'sin'", "'cos'", "'tan'", "'asin'", 
                     "'acos'", "'atan'", "'atan2'", "'sinh'", "'cosh'", 
                     "'tanh'", "'sqrt'", "'log'", "'log10'", "'exp'", "'pow'", 
                     "'fabs'", "'ceil'", "'floor'", "'trunc'", "'factorial'", 
                     "'gcd'", "'comb'", "'isfinite'", "'isinf'", "'isnan'", 
                     "'abs'", "'degrees'", "'['", "']'", "'for'", "'in'", 
                     "'end'", "'while'", "'>'", "'<'", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENT", "NUMBER", "STRING", 
                      "WS" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_print_stmt = 2
    RULE_assign_stmt = 3
    RULE_expr_stmt = 4
    RULE_plot_stmt = 5
    RULE_file_stmt = 6
    RULE_cond_stmt = 7
    RULE_func_stmt = 8
    RULE_expr = 9
    RULE_math_func = 10
    RULE_array_expr = 11
    RULE_array_op = 12
    RULE_for_stmt = 13
    RULE_range_ = 14
    RULE_while_stmt = 15
    RULE_condition = 16

    ruleNames =  [ "program", "stmt", "print_stmt", "assign_stmt", "expr_stmt", 
                   "plot_stmt", "file_stmt", "cond_stmt", "func_stmt", "expr", 
                   "math_func", "array_expr", "array_op", "for_stmt", "range_", 
                   "while_stmt", "condition" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    IDENT=58
    NUMBER=59
    STRING=60
    WS=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MyLangParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StmtContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.stmt()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2028308682175948674) != 0)):
                    break

            self.state = 39
            self.match(MyLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(MyLangParser.Assign_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(MyLangParser.Print_stmtContext,0)


        def expr_stmt(self):
            return self.getTypedRuleContext(MyLangParser.Expr_stmtContext,0)


        def plot_stmt(self):
            return self.getTypedRuleContext(MyLangParser.Plot_stmtContext,0)


        def file_stmt(self):
            return self.getTypedRuleContext(MyLangParser.File_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MyLangParser.For_stmtContext,0)


        def cond_stmt(self):
            return self.getTypedRuleContext(MyLangParser.Cond_stmtContext,0)


        def func_stmt(self):
            return self.getTypedRuleContext(MyLangParser.Func_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MyLangParser.While_stmtContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MyLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.print_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.expr_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.plot_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.file_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.for_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 47
                self.cond_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 48
                self.func_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 49
                self.while_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = MyLangParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_print_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MyLangParser.T__0)
            self.state = 53
            self.match(MyLangParser.T__1)
            self.state = 54
            self.expr(0)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 55
                self.match(MyLangParser.T__2)
                self.state = 56
                self.expr(0)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(MyLangParser.T__3)
            self.state = 63
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MyLangParser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MyLangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MyLangParser.IDENT)
            self.state = 66
            self.match(MyLangParser.T__5)
            self.state = 67
            self.expr(0)
            self.state = 68
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_expr_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_stmt" ):
                listener.enterExpr_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_stmt" ):
                listener.exitExpr_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_stmt" ):
                return visitor.visitExpr_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expr_stmt(self):

        localctx = MyLangParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.expr(0)
            self.state = 71
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Plot_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.IDENT)
            else:
                return self.getToken(MyLangParser.IDENT, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.STRING)
            else:
                return self.getToken(MyLangParser.STRING, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_plot_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlot_stmt" ):
                listener.enterPlot_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlot_stmt" ):
                listener.exitPlot_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlot_stmt" ):
                return visitor.visitPlot_stmt(self)
            else:
                return visitor.visitChildren(self)




    def plot_stmt(self):

        localctx = MyLangParser.Plot_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_plot_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MyLangParser.T__6)
            self.state = 74
            self.match(MyLangParser.T__1)
            self.state = 75
            self.match(MyLangParser.IDENT)
            self.state = 76
            self.match(MyLangParser.T__2)
            self.state = 77
            self.match(MyLangParser.IDENT)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 78
                self.match(MyLangParser.T__2)
                self.state = 79
                self.match(MyLangParser.STRING)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(MyLangParser.T__3)
            self.state = 86
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class File_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.STRING)
            else:
                return self.getToken(MyLangParser.STRING, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_file_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_stmt" ):
                listener.enterFile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_stmt" ):
                listener.exitFile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_stmt" ):
                return visitor.visitFile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def file_stmt(self):

        localctx = MyLangParser.File_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_file_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 89
            self.match(MyLangParser.T__1)
            self.state = 90
            self.match(MyLangParser.STRING)
            self.state = 91
            self.match(MyLangParser.T__2)
            self.state = 92
            self.match(MyLangParser.STRING)
            self.state = 93
            self.match(MyLangParser.T__3)
            self.state = 94
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MyLangParser.ConditionContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StmtContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_cond_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_stmt" ):
                listener.enterCond_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_stmt" ):
                listener.exitCond_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond_stmt" ):
                return visitor.visitCond_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cond_stmt(self):

        localctx = MyLangParser.Cond_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cond_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(MyLangParser.T__9)
            self.state = 97
            self.condition()
            self.state = 98
            self.match(MyLangParser.T__10)
            self.state = 100 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 99
                    self.stmt()

                else:
                    raise NoViableAltException(self)
                self.state = 102 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 104
                self.match(MyLangParser.T__11)
                self.state = 106 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 105
                        self.stmt()

                    else:
                        raise NoViableAltException(self)
                    self.state = 108 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.IDENT)
            else:
                return self.getToken(MyLangParser.IDENT, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_func_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_stmt" ):
                listener.enterFunc_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_stmt" ):
                listener.exitFunc_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_stmt" ):
                return visitor.visitFunc_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_stmt(self):

        localctx = MyLangParser.Func_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(MyLangParser.T__12)
            self.state = 113
            self.match(MyLangParser.T__1)
            self.state = 114
            self.match(MyLangParser.IDENT)
            self.state = 115
            self.match(MyLangParser.T__2)
            self.state = 116
            self.match(MyLangParser.IDENT)
            self.state = 117
            self.match(MyLangParser.T__3)
            self.state = 118
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_op(self):
            return self.getTypedRuleContext(MyLangParser.Array_opContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(MyLangParser.Array_exprContext,0)


        def IDENT(self):
            return self.getToken(MyLangParser.IDENT, 0)

        def NUMBER(self):
            return self.getToken(MyLangParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def math_func(self):
            return self.getTypedRuleContext(MyLangParser.Math_funcContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 121
                self.array_op()
                pass

            elif la_ == 2:
                self.state = 122
                self.array_expr()
                pass

            elif la_ == 3:
                self.state = 123
                self.match(MyLangParser.IDENT)
                pass

            elif la_ == 4:
                self.state = 124
                self.match(MyLangParser.NUMBER)
                pass

            elif la_ == 5:
                self.state = 125
                self.match(MyLangParser.STRING)
                pass

            elif la_ == 6:
                self.state = 126
                self.match(MyLangParser.T__19)
                self.state = 127
                self.expr(2)
                pass

            elif la_ == 7:
                self.state = 128
                self.math_func()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 138
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 136
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 131
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 132
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2080768) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 133
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 134
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 135
                        self.match(MyLangParser.T__18)
                        pass

             
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Math_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_math_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_func" ):
                listener.enterMath_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_func" ):
                listener.exitMath_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_func" ):
                return visitor.visitMath_func(self)
            else:
                return visitor.visitChildren(self)




    def math_func(self):

        localctx = MyLangParser.Math_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_math_func)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(MyLangParser.T__20)
                self.state = 142
                self.match(MyLangParser.T__1)
                self.state = 143
                self.expr(0)
                self.state = 144
                self.match(MyLangParser.T__3)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(MyLangParser.T__21)
                self.state = 147
                self.match(MyLangParser.T__1)
                self.state = 148
                self.expr(0)
                self.state = 149
                self.match(MyLangParser.T__3)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.match(MyLangParser.T__22)
                self.state = 152
                self.match(MyLangParser.T__1)
                self.state = 153
                self.expr(0)
                self.state = 154
                self.match(MyLangParser.T__3)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.match(MyLangParser.T__23)
                self.state = 157
                self.match(MyLangParser.T__1)
                self.state = 158
                self.expr(0)
                self.state = 159
                self.match(MyLangParser.T__3)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 161
                self.match(MyLangParser.T__24)
                self.state = 162
                self.match(MyLangParser.T__1)
                self.state = 163
                self.expr(0)
                self.state = 164
                self.match(MyLangParser.T__3)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 6)
                self.state = 166
                self.match(MyLangParser.T__25)
                self.state = 167
                self.match(MyLangParser.T__1)
                self.state = 168
                self.expr(0)
                self.state = 169
                self.match(MyLangParser.T__3)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 7)
                self.state = 171
                self.match(MyLangParser.T__26)
                self.state = 172
                self.match(MyLangParser.T__1)
                self.state = 173
                self.expr(0)
                self.state = 174
                self.match(MyLangParser.T__2)
                self.state = 175
                self.expr(0)
                self.state = 176
                self.match(MyLangParser.T__3)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 8)
                self.state = 178
                self.match(MyLangParser.T__27)
                self.state = 179
                self.match(MyLangParser.T__1)
                self.state = 180
                self.expr(0)
                self.state = 181
                self.match(MyLangParser.T__3)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 9)
                self.state = 183
                self.match(MyLangParser.T__28)
                self.state = 184
                self.match(MyLangParser.T__1)
                self.state = 185
                self.expr(0)
                self.state = 186
                self.match(MyLangParser.T__3)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 10)
                self.state = 188
                self.match(MyLangParser.T__29)
                self.state = 189
                self.match(MyLangParser.T__1)
                self.state = 190
                self.expr(0)
                self.state = 191
                self.match(MyLangParser.T__3)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 11)
                self.state = 193
                self.match(MyLangParser.T__30)
                self.state = 194
                self.match(MyLangParser.T__1)
                self.state = 195
                self.expr(0)
                self.state = 196
                self.match(MyLangParser.T__3)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 12)
                self.state = 198
                self.match(MyLangParser.T__31)
                self.state = 199
                self.match(MyLangParser.T__1)
                self.state = 200
                self.expr(0)
                self.state = 201
                self.match(MyLangParser.T__3)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 13)
                self.state = 203
                self.match(MyLangParser.T__32)
                self.state = 204
                self.match(MyLangParser.T__1)
                self.state = 205
                self.expr(0)
                self.state = 206
                self.match(MyLangParser.T__3)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 14)
                self.state = 208
                self.match(MyLangParser.T__33)
                self.state = 209
                self.match(MyLangParser.T__1)
                self.state = 210
                self.expr(0)
                self.state = 211
                self.match(MyLangParser.T__3)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 15)
                self.state = 213
                self.match(MyLangParser.T__34)
                self.state = 214
                self.match(MyLangParser.T__1)
                self.state = 215
                self.expr(0)
                self.state = 216
                self.match(MyLangParser.T__2)
                self.state = 217
                self.expr(0)
                self.state = 218
                self.match(MyLangParser.T__3)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 16)
                self.state = 220
                self.match(MyLangParser.T__35)
                self.state = 221
                self.match(MyLangParser.T__1)
                self.state = 222
                self.expr(0)
                self.state = 223
                self.match(MyLangParser.T__3)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 17)
                self.state = 225
                self.match(MyLangParser.T__36)
                self.state = 226
                self.match(MyLangParser.T__1)
                self.state = 227
                self.expr(0)
                self.state = 228
                self.match(MyLangParser.T__3)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 18)
                self.state = 230
                self.match(MyLangParser.T__37)
                self.state = 231
                self.match(MyLangParser.T__1)
                self.state = 232
                self.expr(0)
                self.state = 233
                self.match(MyLangParser.T__3)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 19)
                self.state = 235
                self.match(MyLangParser.T__38)
                self.state = 236
                self.match(MyLangParser.T__1)
                self.state = 237
                self.expr(0)
                self.state = 238
                self.match(MyLangParser.T__3)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 20)
                self.state = 240
                self.match(MyLangParser.T__39)
                self.state = 241
                self.match(MyLangParser.T__1)
                self.state = 242
                self.expr(0)
                self.state = 243
                self.match(MyLangParser.T__3)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 21)
                self.state = 245
                self.match(MyLangParser.T__40)
                self.state = 246
                self.match(MyLangParser.T__1)
                self.state = 247
                self.expr(0)
                self.state = 248
                self.match(MyLangParser.T__2)
                self.state = 249
                self.expr(0)
                self.state = 250
                self.match(MyLangParser.T__3)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 22)
                self.state = 252
                self.match(MyLangParser.T__41)
                self.state = 253
                self.match(MyLangParser.T__1)
                self.state = 254
                self.expr(0)
                self.state = 255
                self.match(MyLangParser.T__2)
                self.state = 256
                self.expr(0)
                self.state = 257
                self.match(MyLangParser.T__3)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 23)
                self.state = 259
                self.match(MyLangParser.T__42)
                self.state = 260
                self.match(MyLangParser.T__1)
                self.state = 261
                self.expr(0)
                self.state = 262
                self.match(MyLangParser.T__3)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 24)
                self.state = 264
                self.match(MyLangParser.T__43)
                self.state = 265
                self.match(MyLangParser.T__1)
                self.state = 266
                self.expr(0)
                self.state = 267
                self.match(MyLangParser.T__3)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 25)
                self.state = 269
                self.match(MyLangParser.T__44)
                self.state = 270
                self.match(MyLangParser.T__1)
                self.state = 271
                self.expr(0)
                self.state = 272
                self.match(MyLangParser.T__3)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 26)
                self.state = 274
                self.match(MyLangParser.T__45)
                self.state = 275
                self.match(MyLangParser.T__1)
                self.state = 276
                self.expr(0)
                self.state = 277
                self.match(MyLangParser.T__3)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 27)
                self.state = 279
                self.match(MyLangParser.T__46)
                self.state = 280
                self.match(MyLangParser.T__1)
                self.state = 281
                self.expr(0)
                self.state = 282
                self.match(MyLangParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def IDENT(self):
            return self.getToken(MyLangParser.IDENT, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_array_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_expr" ):
                listener.enterArray_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_expr" ):
                listener.exitArray_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_expr" ):
                return visitor.visitArray_expr(self)
            else:
                return visitor.visitChildren(self)




    def array_expr(self):

        localctx = MyLangParser.Array_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_expr)
        self._la = 0 # Token type
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(MyLangParser.T__47)
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2018175583014354944) != 0):
                    self.state = 287
                    self.expr(0)
                    self.state = 292
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==3:
                        self.state = 288
                        self.match(MyLangParser.T__2)
                        self.state = 289
                        self.expr(0)
                        self.state = 294
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 297
                self.match(MyLangParser.T__48)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.match(MyLangParser.IDENT)
                self.state = 299
                self.match(MyLangParser.T__47)
                self.state = 300
                self.expr(0)
                self.state = 301
                self.match(MyLangParser.T__48)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.Array_exprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.Array_exprContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_array_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_op" ):
                listener.enterArray_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_op" ):
                listener.exitArray_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_op" ):
                return visitor.visitArray_op(self)
            else:
                return visitor.visitChildren(self)




    def array_op(self):

        localctx = MyLangParser.Array_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.array_expr()
            self.state = 306
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 307
            self.array_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MyLangParser.IDENT, 0)

        def range_(self):
            return self.getTypedRuleContext(MyLangParser.Range_Context,0)


        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StmtContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MyLangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(MyLangParser.T__49)
            self.state = 310
            self.match(MyLangParser.IDENT)
            self.state = 311
            self.match(MyLangParser.T__50)
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 312
                self.range_()
                pass

            elif la_ == 2:
                self.state = 313
                self.expr(0)
                pass


            self.state = 316
            self.match(MyLangParser.T__10)
            self.state = 318 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 317
                self.stmt()
                self.state = 320 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2028308682175948674) != 0)):
                    break

            self.state = 322
            self.match(MyLangParser.T__51)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_range_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_" ):
                listener.enterRange_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_" ):
                listener.exitRange_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_" ):
                return visitor.visitRange_(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = MyLangParser.Range_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_range_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.expr(0)
            self.state = 325
            self.match(MyLangParser.T__2)
            self.state = 326
            self.expr(0)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 327
                self.match(MyLangParser.T__2)
                self.state = 328
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MyLangParser.ConditionContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StmtContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = MyLangParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MyLangParser.T__52)
            self.state = 332
            self.condition()
            self.state = 333
            self.match(MyLangParser.T__10)
            self.state = 335 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 334
                self.stmt()
                self.state = 337 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2028308682175948674) != 0)):
                    break

            self.state = 339
            self.match(MyLangParser.T__51)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MyLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.expr(0)
            self.state = 342
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 270215977642229760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 343
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




