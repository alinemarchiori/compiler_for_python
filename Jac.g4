grammar Jac;

/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
import sys

symbol_table = []
symbols_used = []

stack_cur      = 0
stack_max      = 0

if_counter = 0
while_counter = 0

def emit(bytecode, delta):
    global stack_cur,stack_max
    print('    ' + str(bytecode) + '    ; delta = ' + str(delta) )
    stack_cur += delta
    if stack_cur > stack_max:
        stack_max = stack_cur
}

/*---------------- LEXER RULES ----------------*/

IF : 'if' ;
WHILE : 'while' ;
PRINT : 'print' ;
READINT : 'readint' ;

PLUS  : '+' ;
MINUS : '-' ;
TIMES : '*' ;
OVER  : '/' ;
REM   : '%' ;

OP_CUR: '{' ;
CL_CUR: '}' ;
OP_PAR: '(' ;
CL_PAR: ')' ;
ATTRIB: '=' ;
COMMA : ',' ;

LE    : '<=';
LT    : '<' ;
EQ    : '==';
NE    : '!=';
GT    : '>' ;
GE    : '>=';

NAME  : 'a'..'z'+ ;

NUMBER: '0'..'9'+ ;

SPACE : (' '|'\t'|'\r'|'\n')+ -> skip ;

COMMENT: '#' ~('\n')*         -> skip ;

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
    main
    ;

main:
    {if 1:
        print('.method public static main([Ljava/lang/String;)V\n')
    }

    ( statement )+
    {if 1:
        not_used = [elemento for elemento in symbol_table if elemento not in symbols_used]
        if len(not_used) > 0:  
            sys.stderr.write('warning: ' + not_used[0] + ' is defined but never used')
    }

    {if 1:
        print('    return')
        if len(symbol_table) > 0:
            print('.limit locals ' + str(len(symbol_table)))
        print('.limit stack 10')
        print('.end method')
        print('\n; symbol_table:', symbol_table)
    }
    ;

statement: st_print | st_attrib | st_if | st_while
    ;

st_print:
    PRINT OP_PAR
    {if 1:
        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
    }
    expression 
    {if 1:
        emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
    }
    ( COMMA
    {if 1:
        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
    }
    expression
    {if 1:
        emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
    }
    )*
    ?CL_PAR
    {if 1:
        emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
        emit('invokevirtual java/io/PrintStream/println()V\n', -1)
    }
    ;

st_attrib: 
    NAME ATTRIB expression
    {if 1:
        if $NAME.text not in symbol_table:
            symbol_table.append($NAME.text)

        emit('istore '+str(symbol_table.index($NAME.text)),-1)
    }
    ;

st_while:
    WHILE 
    {if 1:
        global while_counter
        local_counter = while_counter
        print(f'BEGIN_WHILE_{local_counter}:')
    }
    comparison_while
    {if 1:
        while_counter += 1
    }
    OP_CUR ( statement )+ CL_CUR
    {if 1:
        emit('goto BEGIN_WHILE_' + str(local_counter), 0)
        print(f'END_WHILE_{local_counter}:')
    }
    ;

comparison_while: expression op = ( LT | LE | EQ | NE | GT | GE ) expression
    {if 1:
        if $op.type == JacParser.EQ:
            emit('if_icmpne END_WHILE_' + str(while_counter), -2)
        elif $op.type == JacParser.NE:
            emit('if_icmpeq END_WHILE_' + str(while_counter), -2)
        elif $op.type == JacParser.GT:
            emit('if_icmple END_WHILE_' + str(while_counter), -2)
        elif $op.type == JacParser.GE:
            emit('if_icmplt END_WHILE_' + str(while_counter), -2)
        elif $op.type == JacParser.LT:
            emit('if_icmpge END_WHILE_' + str(while_counter), -2)
        elif $op.type == JacParser.LE:
            emit('if_icmpgt END_WHILE_' + str(while_counter), -2)
    }
    ;

st_if:
    IF comparison_if
    {if 1:
        global if_counter
        local_counter = if_counter
        if_counter += 1
    }
    OP_CUR ( statement )+ CL_CUR
    {if 1:
        print(f'NOT_IF_{local_counter}:')
    }
    ;

comparison_if: expression op = ( LT | LE | EQ | NE | GT | GE ) expression
    {if 1:
        if $op.type == JacParser.EQ:
            emit('if_icmpne NOT_IF_' + str(if_counter), -2)
        elif $op.type == JacParser.NE:
            emit('if_icmpeq NOT_IF_' + str(if_counter), -2)
        elif $op.type == JacParser.GT:
            emit('if_icmple NOT_IF_' + str(if_counter), -2)
        elif $op.type == JacParser.GE:
            emit('if_icmplt NOT_IF_' + str(if_counter), -2)
        elif $op.type == JacParser.LT:
            emit('if_icmpge NOT_IF_' + str(if_counter), -2)
        elif $op.type == JacParser.LE:
            emit('if_icmpgt NOT_IF_' + str(if_counter), -2)
    }
    ;

expression:
    term ( op = (PLUS | MINUS) term
    {if 1:
        if $op.type == JacParser.PLUS:
            emit('iadd', -1)
        else:
            emit('isub', -1)
    }
    )*
    ;

term: factor ( op = (TIMES | OVER | REM ) factor
    {if 1:
        if $op.type == JacParser.TIMES:
            emit('imul', -1)
        elif $op.type == JacParser.OVER:
            emit('idiv', -1)
        else:
            emit('irem', -1)
    }
    )*
    ;

factor: NUMBER
    {if 1:
        #print('    ldc ' + $NUMBER.text)
        emit('ldc ' + $NUMBER.text, +1)
    }
    | OP_PAR expression CL_PAR
    | NAME
    {if 1:
        if $NAME.text not in symbol_table:
            sys.stderr.write('error: ' + $NAME.text + ' is not declared in line '+ str($NAME.line))
            sys.exit(1)
        else:
            if $NAME.text not in symbol_table:
                symbols_used.append($NAME.text)
            emit('iload ' + str(symbol_table.index($NAME.text)), +1)
    }
    | READINT OP_PAR CL_PAR
    {if 1:
        emit('invokestatic Runtime/readInt()I', +1)
    }
    ;