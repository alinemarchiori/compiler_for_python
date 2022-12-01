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


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("M\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\3\3\3\6\3\30\n\3\r\3\16\3\31")
        buf.write("\3\3\3\3\3\3\3\4\3\4\5\4!\n\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7\64\n")
        buf.write("\7\f\7\16\7\67\13\7\3\b\3\b\3\b\3\b\3\b\7\b>\n\b\f\b\16")
        buf.write("\bA\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tK\n\t\3\t")
        buf.write("\2\2\n\2\4\6\b\n\f\16\20\2\4\3\2\4\5\3\2\6\b\2J\2\22\3")
        buf.write("\2\2\2\4\25\3\2\2\2\6 \3\2\2\2\b\"\3\2\2\2\n)\3\2\2\2")
        buf.write("\f.\3\2\2\2\168\3\2\2\2\20J\3\2\2\2\22\23\b\2\1\2\23\24")
        buf.write("\5\4\3\2\24\3\3\2\2\2\25\27\b\3\1\2\26\30\5\6\4\2\27\26")
        buf.write("\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32")
        buf.write("\33\3\2\2\2\33\34\b\3\1\2\34\35\b\3\1\2\35\5\3\2\2\2\36")
        buf.write("!\5\b\5\2\37!\5\n\6\2 \36\3\2\2\2 \37\3\2\2\2!\7\3\2\2")
        buf.write("\2\"#\7\3\2\2#$\7\t\2\2$%\b\5\1\2%&\5\f\7\2&\'\7\n\2\2")
        buf.write("\'(\b\5\1\2(\t\3\2\2\2)*\7\f\2\2*+\7\13\2\2+,\5\f\7\2")
        buf.write(",-\b\6\1\2-\13\3\2\2\2.\65\5\16\b\2/\60\t\2\2\2\60\61")
        buf.write("\5\16\b\2\61\62\b\7\1\2\62\64\3\2\2\2\63/\3\2\2\2\64\67")
        buf.write("\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\r\3\2\2\2\67\65")
        buf.write("\3\2\2\28?\5\20\t\29:\t\3\2\2:;\5\20\t\2;<\b\b\1\2<>\3")
        buf.write("\2\2\2=9\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\17\3\2")
        buf.write("\2\2A?\3\2\2\2BC\7\r\2\2CK\b\t\1\2DE\7\t\2\2EF\5\f\7\2")
        buf.write("FG\7\n\2\2GK\3\2\2\2HI\7\f\2\2IK\b\t\1\2JB\3\2\2\2JD\3")
        buf.write("\2\2\2JH\3\2\2\2K\21\3\2\2\2\7\31 \65?J")
        return buf.getvalue()


class JacParser ( Parser ):

    grammarFileName = "Jac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'('", "')'", "'='" ]

    symbolicNames = [ "<INVALID>", "PRINT", "PLUS", "MINUS", "TIMES", "OVER", 
                      "REM", "OP_PAR", "CL_PAR", "ATTRIB", "NAME", "NUMBER", 
                      "SPACE", "COMMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_attrib = 4
    RULE_expression = 5
    RULE_term = 6
    RULE_factor = 7

    ruleNames =  [ "program", "main", "statement", "st_print", "st_attrib", 
                   "expression", "term", "factor" ]

    EOF = Token.EOF
    PRINT=1
    PLUS=2
    MINUS=3
    TIMES=4
    OVER=5
    REM=6
    OP_PAR=7
    CL_PAR=8
    ATTRIB=9
    NAME=10
    NUMBER=11
    SPACE=12
    COMMENT=13

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
                
            self.state = 17
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
                
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==JacParser.PRINT or _la==JacParser.NAME):
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


        def getRuleIndex(self):
            return JacParser.RULE_statement




    def statement(self):

        localctx = JacParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.st_print()
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.st_attrib()
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

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def getRuleIndex(self):
            return JacParser.RULE_st_print




    def st_print(self):

        localctx = JacParser.St_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_st_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(JacParser.PRINT)
            self.state = 33
            self.match(JacParser.OP_PAR)
            if 1:
                    print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
                
            self.state = 35
            self.expression()
            self.state = 36
            self.match(JacParser.CL_PAR)
            if 1:
                    print('    invokevirtual java/io/PrintStream/println(I)V\n')
                
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
            self.state = 39
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 40
            self.match(JacParser.ATTRIB)
            self.state = 41
            self.expression()
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                        symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))

                    print('    istore ' + str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))))
                
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
        self.enterRule(localctx, 10, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.term()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.PLUS or _la==JacParser.MINUS:
                self.state = 45
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==JacParser.PLUS or _la==JacParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 46
                self.term()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.PLUS:
                            print('    iadd')
                        else:
                            print('    isub')
                    
                self.state = 53
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
        self.enterRule(localctx, 12, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.factor()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0):
                self.state = 55
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 56
                self.factor()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.TIMES:
                            print('    imul')
                        elif (0 if localctx.op is None else localctx.op.type) == JacParser.OVER:
                            print('    idiv')
                        else:
                            print('    irem')
                    
                self.state = 63
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

        def getRuleIndex(self):
            return JacParser.RULE_factor




    def factor(self):

        localctx = JacParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                localctx._NUMBER = self.match(JacParser.NUMBER)
                if 1:
                        print('    ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text))
                    
                pass
            elif token in [JacParser.OP_PAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(JacParser.OP_PAR)
                self.state = 67
                self.expression()
                self.state = 68
                self.match(JacParser.CL_PAR)
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                localctx._NAME = self.match(JacParser.NAME)
                if 1:
                        if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                            sys.stderr.write('error: ' + (None if localctx._NAME is None else localctx._NAME.text) + ' is not declared in line '+ str((0 if localctx._NAME is None else localctx._NAME.line)))
                            sys.exit(1)
                        else:
                            if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                                symbols_used.append((None if localctx._NAME is None else localctx._NAME.text))
                            print('    iload  ' + str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))))
                    
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





