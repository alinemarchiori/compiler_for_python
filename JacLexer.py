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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("M\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13\65")
        buf.write("\n\13\r\13\16\13\66\3\f\6\f:\n\f\r\f\16\f;\3\r\6\r?\n")
        buf.write("\r\r\r\16\r@\3\r\3\r\3\16\3\16\7\16G\n\16\f\16\16\16J")
        buf.write("\13\16\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\3\2\4\5\2\13\f\17\17")
        buf.write("\"\"\3\2\f\f\2P\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2")
        buf.write("\t\'\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2\17-\3\2\2\2\21/\3")
        buf.write("\2\2\2\23\61\3\2\2\2\25\64\3\2\2\2\279\3\2\2\2\31>\3\2")
        buf.write("\2\2\33D\3\2\2\2\35\36\7r\2\2\36\37\7t\2\2\37 \7k\2\2")
        buf.write(" !\7p\2\2!\"\7v\2\2\"\4\3\2\2\2#$\7-\2\2$\6\3\2\2\2%&")
        buf.write("\7/\2\2&\b\3\2\2\2\'(\7,\2\2(\n\3\2\2\2)*\7\61\2\2*\f")
        buf.write("\3\2\2\2+,\7\'\2\2,\16\3\2\2\2-.\7*\2\2.\20\3\2\2\2/\60")
        buf.write("\7+\2\2\60\22\3\2\2\2\61\62\7?\2\2\62\24\3\2\2\2\63\65")
        buf.write("\4c|\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67")
        buf.write("\3\2\2\2\67\26\3\2\2\28:\4\62;\298\3\2\2\2:;\3\2\2\2;")
        buf.write("9\3\2\2\2;<\3\2\2\2<\30\3\2\2\2=?\t\2\2\2>=\3\2\2\2?@")
        buf.write("\3\2\2\2@>\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\b\r\2\2C\32\3")
        buf.write("\2\2\2DH\7%\2\2EG\n\3\2\2FE\3\2\2\2GJ\3\2\2\2HF\3\2\2")
        buf.write("\2HI\3\2\2\2IK\3\2\2\2JH\3\2\2\2KL\b\16\2\2L\34\3\2\2")
        buf.write("\2\7\2\66;@H\3\b\2\2")
        return buf.getvalue()


class JacLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRINT = 1
    PLUS = 2
    MINUS = 3
    TIMES = 4
    OVER = 5
    REM = 6
    OP_PAR = 7
    CL_PAR = 8
    ATTRIB = 9
    NAME = 10
    NUMBER = 11
    SPACE = 12
    COMMENT = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", 
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", 
            "CL_PAR", "ATTRIB", "NAME", "NUMBER", "SPACE", "COMMENT" ]

    ruleNames = [ "PRINT", "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", 
                  "CL_PAR", "ATTRIB", "NAME", "NUMBER", "SPACE", "COMMENT" ]

    grammarFileName = "Jac.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


