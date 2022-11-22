grammar Jac;

/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
import sys
symbol_table = []
symbols_used = []
}

/*---------------- LEXER RULES ----------------*/

PRINT : 'print' ;

PLUS  : '+' ;
MINUS : '-' ;
TIMES : '*' ;
OVER  : '/' ;
REM   : '%' ;

OP_PAR: '(' ;
CL_PAR: ')' ;
ATTRIB: '=' ;

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

statement: st_print | st_attrib
    ;

st_print:
    PRINT OP_PAR
    {if 1:
        print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
    }
    expression CL_PAR
    {if 1:
        print('    invokevirtual java/io/PrintStream/println(I)V\n')
    }
    ;

st_attrib: 
    NAME ATTRIB expression
    {if 1:
        if $NAME.text not in symbol_table:
            symbol_table.append($NAME.text)

        print('    istore ' + str(symbol_table.index($NAME.text)))
    }
    ;

expression:
    term ( op = (PLUS | MINUS) term
    {if 1:
        if $op.type == JacParser.PLUS:
            print('    iadd')
        else:
            print('    isub')
    }
    )*
    ;

term: factor ( op = (TIMES | OVER | REM ) factor
    {if 1:
        if $op.type == JacParser.TIMES:
            print('    imul')
        elif $op.type == JacParser.OVER:
            print('    idiv')
        else:
            print('    irem')
    }
    )*
    ;

factor: NUMBER
    {if 1:
        print('    ldc ' + $NUMBER.text)
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
            print('    iload  ' + str(symbol_table.index($NAME.text)))
    }
    ;