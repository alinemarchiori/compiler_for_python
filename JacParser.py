# Generated from Jac.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import sys

symbol_table = []
symbols_used = []

stack_cur      = 0
stack_max      = 0

if_counter = 0

def emit(bytecode, delta):
    global stack_cur,stack_max
    print('    ' + str(bytecode) + '    ; delta = ' + str(delta) )
    stack_cur += delta
    if stack_cur > stack_max:
        stack_max = stack_cur


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3\6\3")
        buf.write("\34\n\3\r\3\16\3\35\3\3\3\3\3\3\3\4\3\4\3\4\5\4&\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\62\n\5\f\5")
        buf.write("\16\5\65\13\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\6\7C\n\7\r\7\16\7D\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\7\tT\n\t\f\t\16\tW\13\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\7\n^\n\n\f\n\16\na\13\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13o\n")
        buf.write("\13\3\13\3\63\2\f\2\4\6\b\n\f\16\20\22\24\2\4\3\2\6\7")
        buf.write("\3\2\b\n\2p\2\26\3\2\2\2\4\31\3\2\2\2\6%\3\2\2\2\b\'\3")
        buf.write("\2\2\2\n9\3\2\2\2\f>\3\2\2\2\16I\3\2\2\2\20N\3\2\2\2\22")
        buf.write("X\3\2\2\2\24n\3\2\2\2\26\27\b\2\1\2\27\30\5\4\3\2\30\3")
        buf.write("\3\2\2\2\31\33\b\3\1\2\32\34\5\6\4\2\33\32\3\2\2\2\34")
        buf.write("\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2")
        buf.write("\37 \b\3\1\2 !\b\3\1\2!\5\3\2\2\2\"&\5\b\5\2#&\5\n\6\2")
        buf.write("$&\5\f\7\2%\"\3\2\2\2%#\3\2\2\2%$\3\2\2\2&\7\3\2\2\2\'")
        buf.write("(\7\4\2\2()\7\r\2\2)*\b\5\1\2*+\5\20\t\2+\63\b\5\1\2,")
        buf.write("-\7\20\2\2-.\b\5\1\2./\5\20\t\2/\60\b\5\1\2\60\62\3\2")
        buf.write("\2\2\61,\3\2\2\2\62\65\3\2\2\2\63\64\3\2\2\2\63\61\3\2")
        buf.write("\2\2\64\66\3\2\2\2\65\63\3\2\2\2\66\67\7\16\2\2\678\b")
        buf.write("\5\1\28\t\3\2\2\29:\7\22\2\2:;\7\17\2\2;<\5\20\t\2<=\b")
        buf.write("\6\1\2=\13\3\2\2\2>?\7\3\2\2?@\5\16\b\2@B\7\13\2\2AC\5")
        buf.write("\6\4\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2EF\3\2\2")
        buf.write("\2FG\7\f\2\2GH\b\7\1\2H\r\3\2\2\2IJ\5\20\t\2JK\7\21\2")
        buf.write("\2KL\5\20\t\2LM\b\b\1\2M\17\3\2\2\2NU\5\22\n\2OP\t\2\2")
        buf.write("\2PQ\5\22\n\2QR\b\t\1\2RT\3\2\2\2SO\3\2\2\2TW\3\2\2\2")
        buf.write("US\3\2\2\2UV\3\2\2\2V\21\3\2\2\2WU\3\2\2\2X_\5\24\13\2")
        buf.write("YZ\t\3\2\2Z[\5\24\13\2[\\\b\n\1\2\\^\3\2\2\2]Y\3\2\2\2")
        buf.write("^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\23\3\2\2\2a_\3\2\2\2b")
        buf.write("c\7\23\2\2co\b\13\1\2de\7\r\2\2ef\5\20\t\2fg\7\16\2\2")
        buf.write("go\3\2\2\2hi\7\22\2\2io\b\13\1\2jk\7\5\2\2kl\7\r\2\2l")
        buf.write("m\7\16\2\2mo\b\13\1\2nb\3\2\2\2nd\3\2\2\2nh\3\2\2\2nj")
        buf.write("\3\2\2\2o\25\3\2\2\2\t\35%\63DU_n")
        return buf.getvalue()


class JacParser ( Parser ):

    grammarFileName = "Jac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'print'", "'readint'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'{'", "'}'", "'('", "')'", 
                     "'='", "','", "'<'" ]

    symbolicNames = [ "<INVALID>", "IF", "PRINT", "READINT", "PLUS", "MINUS", 
                      "TIMES", "OVER", "REM", "OP_CUR", "CL_CUR", "OP_PAR", 
                      "CL_PAR", "ATTRIB", "COMMA", "LT", "NAME", "NUMBER", 
                      "SPACE", "COMMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_attrib = 4
    RULE_st_if = 5
    RULE_comparison = 6
    RULE_expression = 7
    RULE_term = 8
    RULE_factor = 9

    ruleNames =  [ "program", "main", "statement", "st_print", "st_attrib", 
                   "st_if", "comparison", "expression", "term", "factor" ]

    EOF = Token.EOF
    IF=1
    PRINT=2
    READINT=3
    PLUS=4
    MINUS=5
    TIMES=6
    OVER=7
    REM=8
    OP_CUR=9
    CL_CUR=10
    OP_PAR=11
    CL_PAR=12
    ATTRIB=13
    COMMA=14
    LT=15
    NAME=16
    NUMBER=17
    SPACE=18
    COMMENT=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(JacParser.MainContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_program




    def program(self):

        localctx = JacParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            if 1:
                    print('.source Test.src')
                    print('.class  public Test')
                    print('.super  java/lang/Object\n')
                    print('.method public <init>()V')
                    print('    aload_0')
                    print('    invokenonvirtual java/lang/Object/<init>()V')
                    print('    return')
                    print('.end method\n')
                
            self.state = 21
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_main




    def main(self):

        localctx = JacParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            if 1:
                    print('.method public static main([Ljava/lang/String;)V\n')
                
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.PRINT) | (1 << JacParser.NAME))) != 0)):
                    break

            if 1:
                    not_used = [elemento for elemento in symbol_table if elemento not in symbols_used]
                    if len(not_used) > 0:  
                        sys.stderr.write('warning: ' + not_used[0] + ' is defined but never used')
                
            if 1:
                    print('    return')
                    if len(symbol_table) > 0:
                        print('.limit locals ' + str(len(symbol_table)))
                    print('.limit stack 10')
                    print('.end method')
                    print('\n; symbol_table:', symbol_table)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def st_print(self):
            return self.getTypedRuleContext(JacParser.St_printContext,0)


        def st_attrib(self):
            return self.getTypedRuleContext(JacParser.St_attribContext,0)


        def st_if(self):
            return self.getTypedRuleContext(JacParser.St_ifContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_statement




    def statement(self):

        localctx = JacParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.st_print()
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.st_attrib()
                pass
            elif token in [JacParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.st_if()
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


    class St_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(JacParser.PRINT, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JacParser.ExpressionContext,i)


        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.COMMA)
            else:
                return self.getToken(JacParser.COMMA, i)

        def getRuleIndex(self):
            return JacParser.RULE_st_print




    def st_print(self):

        localctx = JacParser.St_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_st_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(JacParser.PRINT)
            self.state = 38
            self.match(JacParser.OP_PAR)
            if 1:
                    emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                
            self.state = 40
            self.expression()
            if 1:
                    emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
                
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 42
                    self.match(JacParser.COMMA)
                    if 1:
                            emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                        
                    self.state = 44
                    self.expression()
                    if 1:
                            emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
                         
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 52
            self.match(JacParser.CL_PAR)
            if 1:
                    emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    emit('invokevirtual java/io/PrintStream/println()V\n', -1)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_attribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def ATTRIB(self):
            return self.getToken(JacParser.ATTRIB, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_st_attrib




    def st_attrib(self):

        localctx = JacParser.St_attribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 56
            self.match(JacParser.ATTRIB)
            self.state = 57
            self.expression()
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                        symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))

                    emit('istore '+str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))),-1)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(JacParser.IF, 0)

        def comparison(self):
            return self.getTypedRuleContext(JacParser.ComparisonContext,0)


        def OP_CUR(self):
            return self.getToken(JacParser.OP_CUR, 0)

        def CL_CUR(self):
            return self.getToken(JacParser.CL_CUR, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_st_if




    def st_if(self):

        localctx = JacParser.St_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(JacParser.IF)
            self.state = 61
            self.comparison()
            self.state = 62
            self.match(JacParser.OP_CUR)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.statement()
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.PRINT) | (1 << JacParser.NAME))) != 0)):
                    break

            self.state = 68
            self.match(JacParser.CL_CUR)
            if 1:
                    global if_counter
                    print(f'NOT_IF_{if_counter}:')
                    if_counter += 1
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JacParser.ExpressionContext,i)


        def LT(self):
            return self.getToken(JacParser.LT, 0)

        def getRuleIndex(self):
            return JacParser.RULE_comparison




    def comparison(self):

        localctx = JacParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.expression()
            self.state = 72
            self.match(JacParser.LT)
            self.state = 73
            self.expression()
            if 1:
                    emit('if_icmpge NOT_IF_' + str(if_counter), -2)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.TermContext)
            else:
                return self.getTypedRuleContext(JacParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.PLUS)
            else:
                return self.getToken(JacParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.MINUS)
            else:
                return self.getToken(JacParser.MINUS, i)

        def getRuleIndex(self):
            return JacParser.RULE_expression




    def expression(self):

        localctx = JacParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.term()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.PLUS or _la==JacParser.MINUS:
                self.state = 77
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==JacParser.PLUS or _la==JacParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 78
                self.term()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.PLUS:
                            emit('iadd', -1)
                        else:
                            emit('isub', -1)
                    
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.FactorContext)
            else:
                return self.getTypedRuleContext(JacParser.FactorContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.TIMES)
            else:
                return self.getToken(JacParser.TIMES, i)

        def OVER(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.OVER)
            else:
                return self.getToken(JacParser.OVER, i)

        def REM(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.REM)
            else:
                return self.getToken(JacParser.REM, i)

        def getRuleIndex(self):
            return JacParser.RULE_term




    def term(self):

        localctx = JacParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.factor()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0):
                self.state = 87
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 88
                self.factor()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.TIMES:
                            emit('imul', -1)
                        elif (0 if localctx.op is None else localctx.op.type) == JacParser.OVER:
                            emit('idiv', -1)
                        else:
                            emit('irem', -1)
                    
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NUMBER = None # Token
            self._NAME = None # Token

        def NUMBER(self):
            return self.getToken(JacParser.NUMBER, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def READINT(self):
            return self.getToken(JacParser.READINT, 0)

        def getRuleIndex(self):
            return JacParser.RULE_factor




    def factor(self):

        localctx = JacParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_factor)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                localctx._NUMBER = self.match(JacParser.NUMBER)
                if 1:
                        #print('    ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text))
                        emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), +1)
                    
                pass
            elif token in [JacParser.OP_PAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(JacParser.OP_PAR)
                self.state = 99
                self.expression()
                self.state = 100
                self.match(JacParser.CL_PAR)
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                localctx._NAME = self.match(JacParser.NAME)
                if 1:
                        if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                            sys.stderr.write('error: ' + (None if localctx._NAME is None else localctx._NAME.text) + ' is not declared in line '+ str((0 if localctx._NAME is None else localctx._NAME.line)))
                            sys.exit(1)
                        else:
                            if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                                symbols_used.append((None if localctx._NAME is None else localctx._NAME.text))
                            emit('iload ' + str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), +1)
                    
                pass
            elif token in [JacParser.READINT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.match(JacParser.READINT)
                self.state = 105
                self.match(JacParser.OP_PAR)
                self.state = 106
                self.match(JacParser.CL_PAR)
                if 1:
                        emit('invokestatic Runtime/readInt()I', +1)
                    
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





