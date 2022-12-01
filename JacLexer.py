# Generated from Jac.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("l\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\6\21T\n\21\r\21\16\21U\3\22")
        buf.write("\6\22Y\n\22\r\22\16\22Z\3\23\6\23^\n\23\r\23\16\23_\3")
        buf.write("\23\3\23\3\24\3\24\7\24f\n\24\f\24\16\24i\13\24\3\24\3")
        buf.write("\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25\3\2\4")
        buf.write("\5\2\13\f\17\17\"\"\3\2\f\f\2o\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3")
        buf.write("\2\2\2\5,\3\2\2\2\7\62\3\2\2\2\t:\3\2\2\2\13<\3\2\2\2")
        buf.write("\r>\3\2\2\2\17@\3\2\2\2\21B\3\2\2\2\23D\3\2\2\2\25F\3")
        buf.write("\2\2\2\27H\3\2\2\2\31J\3\2\2\2\33L\3\2\2\2\35N\3\2\2\2")
        buf.write("\37P\3\2\2\2!S\3\2\2\2#X\3\2\2\2%]\3\2\2\2\'c\3\2\2\2")
        buf.write(")*\7k\2\2*+\7h\2\2+\4\3\2\2\2,-\7r\2\2-.\7t\2\2./\7k\2")
        buf.write("\2/\60\7p\2\2\60\61\7v\2\2\61\6\3\2\2\2\62\63\7t\2\2\63")
        buf.write("\64\7g\2\2\64\65\7c\2\2\65\66\7f\2\2\66\67\7k\2\2\678")
        buf.write("\7p\2\289\7v\2\29\b\3\2\2\2:;\7-\2\2;\n\3\2\2\2<=\7/\2")
        buf.write("\2=\f\3\2\2\2>?\7,\2\2?\16\3\2\2\2@A\7\61\2\2A\20\3\2")
        buf.write("\2\2BC\7\'\2\2C\22\3\2\2\2DE\7}\2\2E\24\3\2\2\2FG\7\177")
        buf.write("\2\2G\26\3\2\2\2HI\7*\2\2I\30\3\2\2\2JK\7+\2\2K\32\3\2")
        buf.write("\2\2LM\7?\2\2M\34\3\2\2\2NO\7.\2\2O\36\3\2\2\2PQ\7>\2")
        buf.write("\2Q \3\2\2\2RT\4c|\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3")
        buf.write("\2\2\2V\"\3\2\2\2WY\4\62;\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2")
        buf.write("\2\2Z[\3\2\2\2[$\3\2\2\2\\^\t\2\2\2]\\\3\2\2\2^_\3\2\2")
        buf.write("\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\b\23\2\2b&\3\2\2\2")
        buf.write("cg\7%\2\2df\n\3\2\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3")
        buf.write("\2\2\2hj\3\2\2\2ig\3\2\2\2jk\b\24\2\2k(\3\2\2\2\7\2UZ")
        buf.write("_g\3\b\2\2")
        return buf.getvalue()


class JacLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    PRINT = 2
    READINT = 3
    PLUS = 4
    MINUS = 5
    TIMES = 6
    OVER = 7
    REM = 8
    OP_CUR = 9
    CL_CUR = 10
    OP_PAR = 11
    CL_PAR = 12
    ATTRIB = 13
    COMMA = 14
    LT = 15
    NAME = 16
    NUMBER = 17
    SPACE = 18
    COMMENT = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'print'", "'readint'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'{'", "'}'", "'('", "')'", "'='", "','", "'<'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "PRINT", "READINT", "PLUS", "MINUS", "TIMES", "OVER", 
            "REM", "OP_CUR", "CL_CUR", "OP_PAR", "CL_PAR", "ATTRIB", "COMMA", 
            "LT", "NAME", "NUMBER", "SPACE", "COMMENT" ]

    ruleNames = [ "IF", "PRINT", "READINT", "PLUS", "MINUS", "TIMES", "OVER", 
                  "REM", "OP_CUR", "CL_CUR", "OP_PAR", "CL_PAR", "ATTRIB", 
                  "COMMA", "LT", "NAME", "NUMBER", "SPACE", "COMMENT" ]

    grammarFileName = "Jac.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


