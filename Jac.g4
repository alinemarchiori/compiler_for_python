grammar Jac;

/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
import sys

symbol_table = []
types_table  = []
symbols_used = []
stack_while    = []
list_functions = []
types_functions = []
list_quantidade_parametros = []

stack_cur      = 0
stack_max      = 0
has_error      = 0
flagInt        = False
quantidade_argumentos = 0
if_counter = 0
while_counter = 0
name_function = ""
return_used = False

def emit(bytecode, delta):
    global stack_cur,stack_max
    print('    ' + str(bytecode) + '    ; delta = ' + str(delta) )
    stack_cur += delta
    if stack_cur > stack_max:
        stack_max = stack_cur
}

/*---------------- LEXER INTERNALS ----------------*/

@lexer::header
{
from antlr_denter.DenterHelper import DenterHelper
from JacParser import JacParser
}

@lexer::members
{
class JacDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: JacLexer = lexer

    def pull_token(self):
        return super(JacLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.JacDenter(self, self.NL, JacParser.INDENT, JacParser.DEDENT, False)
    return self.denter.next_token()
}

/*---------------- LEXER RULES ----------------*/

IF      : 'if'      ;
WHILE   : 'while'   ;
PRINT   : 'print'   ;
READINT : 'readint' ;
INDENT  : 'indent'  ;
DEDENT  : 'dedent'  ;
BREAK   : 'break'   ; 
CONTINUE: 'continue'; 
READSTR : 'readstr' ;
DEF     : 'def'     ;
INT     : 'int'     ;
RETURN  : 'return'  ;

PLUS  : '+' ;
MINUS : '-' ;
TIMES : '*' ;
OVER  : '/' ;
REM   : '%' ;

OP_PAR: '(' ;
CL_PAR: ')' ;
ATTRIB: '=' ;
COMMA : ',' ;
COLON : ':' ;

LE    : '<=';
LT    : '<' ;
EQ    : '==';
NE    : '!=';
GT    : '>' ;
GE    : '>=';

NAME  : 'a'..'z'+ ;

NUMBER: '0'..'9'+ ;
STRING: '"' ~('"')* '"' ;

COMMENT: '#' ~('\n')* -> skip ;
NL     : ('\r'? '\n' ' '*) ;
SPACE  : (' '|'\t')+ -> skip ;

/*---------------- PARSER RULES ----------------*/

program:
    {if 1:
        print('.source Test.src')
        print('.class  public Test')
        print('.super  java/lang/Object\n')
        print('.method public <init>()V')
        print('    aload_0')
        print('    invokenonvirtual java/lang/Object/<init>()V')
        print('    return')
        print('.end method\n')
    }
    (function)* main
    {if 1:
        sys.exit(has_error)
    }
    ;

main:
    {if 1:
        print('.method public static main([Ljava/lang/String;)V\n')
    }

    ( statement )+
    {if 1:
        not_used = [elemento for elemento in symbol_table if elemento not in symbols_used]
        if len(not_used) > 0:  
            sys.stderr.write('warning: ' + not_used[0] + ' is defined but never used \n')
    }

    {if 1:
        print('    return')
        if len(symbol_table) > 0:
            print('.limit locals ' + str(len(symbol_table)))
        if stack_max > 0:
            print('.limit stack ' + str(stack_max))
        print('.end method')
        print('\n; symbol_table:', symbol_table)
    }
    ;

function: DEF NAME 

    {if 1:
        global list_functions, flagInt, stack_max, quantidade_argumentos, types_functions, name_function, return_used
        print(f'\n; {list_functions}, {$NAME.text}', list_functions)
        if $NAME.text in list_functions:
            sys.stderr.write(f'error: function {$NAME.text} is already declared \n')
            global has_error
            has_error = 1
        else:
            list_functions.append($NAME.text)
    }
    
    OP_PAR ( parameters ) CL_PAR 
    
    COLON ( INT 
    {if 1:
        flagInt = True
    })? 

    {if 1:
        if flagInt:
            print(f'.method public static {$NAME.text}({"I"*len(symbol_table)})I\n')
            types_functions.append("I")
            flagInt = False
        else:
            print(f'.method public static {$NAME.text}({"I"*len(symbol_table)})V\n')
            types_functions.append("V")

        name_function = $NAME.text
        list_quantidade_parametros.append(len(symbol_table))
    }
    INDENT ( statement )* DEDENT

    {if 1:
        not_used = [elemento for elemento in symbol_table if elemento not in symbols_used]
        if len(not_used) > 0:  
            sys.stderr.write('warning: ' + not_used[0] + ' is defined but never used \n')
    }

    {if 1:
        print('    return')
        if len(symbol_table) > 0:
            print('.limit locals ' + str(len(symbol_table)))
        print('.limit stack ' + str(stack_max))
        print('.end method')
    }
    
    {if 1:
        if not return_used and types_functions[list_functions.index(name_function)] == "I":
            sys.stderr.write('error: missing return statement in returning function \n')
            has_error = 1
        return_used = False
        symbol_table.clear()
        symbols_used.clear()
        types_table.clear()
        stack_max = 0
    }
    ;


parameters: ( NAME 
    {if 1:
        symbol_table.append($NAME.text)
        types_table.append('i')
        symbols_used.append($NAME.text)
    }
    ( COMMA NAME 
    {if 1:
        symbol_table.append($NAME.text)
        types_table.append('i')
        symbols_used.append($NAME.text)
    }
    )* )?
    ;

statement: NL | st_print | st_attrib | st_if | st_while | st_break | st_continue | st_call | st_return
    ;

st_print: PRINT OP_PAR
    {if 1:
        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
    }
    e1 = expression 
    {if 1:
        if $e1.type == 'i':
            emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
        elif $e1.type == 's':
            emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
        else:
            sys.stderr.write('error: cannot mix types\n')
    }
    ( COMMA
    {if 1:
        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
    }
    e2 = expression
    {if 1:
        if $e2.type == 'i':
            emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
        elif $e2.type == 's':
            emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
        else:
            sys.stderr.write('error: cannot mix types\n')
    }
    )*
    ?CL_PAR
    {if 1:
        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
        emit('invokevirtual java/io/PrintStream/println()V\n', -1)
    }
    ;

st_attrib: NAME ATTRIB e = expression
    {if 1:
        if $NAME.text not in symbol_table:
            symbol_table.append($NAME.text)
            types_table.append($e.type)
        address = symbol_table.index($NAME.text)
        if $e.type == types_table[address]:
            if $e.type == 'i':
                emit('istore '+str(symbol_table.index($NAME.text)),-1)
            else:
                emit('astore '+str(symbol_table.index($NAME.text)),-1)
        else:
            text = ""
            if types_table[address] == 'i':
                text += " is integer\n"
            else:
                text += " cannot receive an integer expression\n"
            sys.stderr.write('error: ' + symbol_table[address] + text)
            global has_error
            has_error = 1
    }
    ;

st_while: WHILE 
    {if 1:
        global while_counter, stack_while
        stack_while.append(while_counter)
        while_counter += 1
        print(f'BEGIN_WHILE_{stack_while[-1]}:')
    }
    cmp = comparison
    {if 1:
        emit($cmp.type + ' END_WHILE_' + str(stack_while[-1]), -2)
    }
    COLON INDENT ( statement )+ DEDENT
    {if 1:
        emit('goto BEGIN_WHILE_' + str(stack_while[-1]), 0)
        print(f'END_WHILE_{stack_while[-1]}:')
        stack_while.pop()
    }
    ;

st_if: IF cmp = comparison
    {if 1:
        global if_counter
        emit($cmp.type + ' NOT_IF_' + str(if_counter), -2)
        local_counter = if_counter
        if_counter += 1
    }
    COLON INDENT ( statement )+ DEDENT
    {if 1:
        print(f'NOT_IF_{local_counter}:')
    }
    ;

comparison returns [type]: e1 = expression op = ( LT | LE | EQ | NE | GT | GE ) e2 = expression
    {if 1:
        if $op.type == JacParser.EQ: $type = 'if_icmpne'
        elif $op.type == JacParser.NE: $type = 'if_icmpeq'
        elif $op.type == JacParser.GT: $type = 'if_icmple'
        elif $op.type == JacParser.GE: $type = 'if_icmplt'
        elif $op.type == JacParser.LT: $type = 'if_icmpge'
        elif $op.type == JacParser.LE: $type = 'if_icmpgt'
    }
    {if 1:
        if $e1.type != $e2.type:
            sys.stderr.write('error: ' + $e1.text + ' ' + $e2.text + ' diferent types\n')
            global has_error
            has_error = 1
    }
    ;

st_break: BREAK
    {if 1:
        global stack_while
        if len(stack_while) > 0:
            emit('goto END_WHILE_' + str(stack_while[-1]), -2)
        else:
            sys.stderr.write('error: cannot use break outside a loop')
    }
    ;

st_continue: CONTINUE
    {if 1:
        global stack_while
        if len(stack_while) > 0:
            emit('goto BEGIN_WHILE_' + str(stack_while[-1]), 0)
        else:
            sys.stderr.write('error: cannot use continue outside a loop')
    }
    ;

st_call: NAME {if 1: name_function = $NAME.text}
    {if 1:
        if $NAME.text not in list_functions:
            sys.stderr.write(f'error: function {$NAME.text} is not declared \n')
            global has_error
            has_error = 1
    }
    OP_PAR ( arguments ) CL_PAR
    {if 1:
        global quantidade_argumentos
        if quantidade_argumentos == list_quantidade_parametros[list_functions.index($NAME.text)]:
            emit(f'invokestatic Test/{$NAME.text}({"I"*quantidade_argumentos})V', -quantidade_argumentos)
            quantidade_argumentos = 0
        else:
            sys.stderr.write(f'error: wrong number of arguments \n')
            quantidade_argumentos = 0
            has_error = 1
    }
    ;

arguments: (e = expression 
    {if 1:
        global quantidade_argumentos, has_error
        quantidade_argumentos += 1
    }
    {if 1:
        if $e.type == 's':
            sys.stderr.write('error: all arguments must be integer\n')
            has_error = 1
    }
    (COMMA e1 = expression
    {if 1:
        quantidade_argumentos += 1
    }
    {if 1:
        if $e1.type == 's':
            sys.stderr.write('error: all arguments must be integer\n')
            has_error = 1
    }
    )*)?
    ;

st_return: RETURN 
    {if 1:
        global has_error, types_functions, name_function, return_used
        if types_functions[list_functions.index(name_function)] != "I":
            sys.stderr.write('error: a void function does not return a value \n')
            has_error = 1
    } 
    e = expression
    {if 1:
        if $e.type != 'i':
            sys.stderr.write('error: return value must be of integer type\n')
            has_error = 1
        else:
            emit('ireturn', -1)
        return_used = True
    }
    ;

expression returns [type]: t1 = term ( op = ( PLUS | MINUS ) t2 = term
    {if 1:
        if str($t1.type) == str($t2.type) and str($t1.type) != 's':
            if $op.type == JacParser.PLUS:
                emit('iadd', -1)
            else:
                emit('isub', -1)
        else:
            sys.stderr.write('error: ' + $t1.text + ' ' + $t2.text + ' diferent types\n')
            global has_error
            has_error = 1
    }
    )*
    {if 1:
        $type = $t1.type
    }
    ;

term returns [type]: f1 = factor ( op = ( TIMES | OVER | REM ) f2 = factor
    {if 1:
        if str($f1.type) == str($f2.type) and str($f1.type) != 's':
            if $op.type == JacParser.TIMES:
                emit('imul', -1)
            elif $op.type == JacParser.OVER:
                emit('idiv', -1)
            else:
                emit('irem', -1)
        else:
            sys.stderr.write('error: ' + $f1.text + ' ' + $f2.text + ' diferent types\n')
            global has_error
            has_error = 1
    }
    )*
    {if 1:
        $type = $f1.type
    }
    ;

factor returns [type]: NUMBER
    {if 1:
        global quantidade_argumentos, name_function
        emit('ldc ' + $NUMBER.text, +1)
        $type = 'i'
    }
    | STRING
    {if 1:
        emit('ldc ' + $STRING.text, +1)
        $type = 's'
    }
    | OP_PAR e = expression CL_PAR
    {if 1:
        $type = $e.type
    }
    | NAME {if 1: name_function = $NAME.text} OP_PAR ( arguments
    {if 1:
        emit(f'invokestatic Test/{$NAME.text}({"I"*quantidade_argumentos})I', -quantidade_argumentos+1)
        quantidade_argumentos = 0
        $type = 'i'
    }) CL_PAR
    | NAME
    {if 1:
        if $NAME.text not in symbol_table:
            sys.stderr.write('error: ' + $NAME.text + ' is not declared in line '+ str($NAME.line))
            sys.exit(1)
        elif $NAME.text not in symbols_used:
            symbols_used.append($NAME.text)

        address = symbol_table.index($NAME.text)
        if types_table[address] == 'i':
            emit('iload ' + str(address), +1)
            $type = 'i'
        else:
            emit('aload ' + str(address), +1)
            $type = 's'
    }
    | READINT OP_PAR CL_PAR
    {if 1:
        emit('invokestatic Runtime/readInt()I', +1)
        $type = 'i'
    }
    | READSTR OP_PAR CL_PAR
    {if 1:
        emit('invokestatic Runtime/readString()Ljava/lang/String;', +1)
        $type = 's'
    }
    ;