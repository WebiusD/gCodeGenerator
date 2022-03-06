grammar agCode;

//Parser rules:
prog        : statement+ EOF;

statement   : (gLine | logic | varDecl | assign | printLn) ;

gLine       : (gMove | gCirc | gWait) ;
gMove       : G01 (ML expr)? (ML expr)? (ML expr)? (ML MINUS? expr)? (ML expr)? ;
gCirc       : G23 CL expr ;
gWait       : 'G4' 'T' expr ;

logic       : repeatStmt | ifStmt ;
repeatStmt  : 'repeat' expr ':' statement+ 'end' ;
ifStmt      : 'if' condition ':' trueStats ('else' ':' falseStats)? 'end';
trueStats   : statement+ ;
falseStats  : statement+ ;

condition   : ID COMPAR expr ;

varDecl     : 'var' ID ('=' expr)? ;

assign      : ID '=' expr ;

printLn     : 'print' '(' TEXT? (',' expr)? ')' ;

expr        : ID                        #var
            | NUM                       #number
            | expr op=('*'|'/') expr    #mul
            | expr op=('+'|'-') expr    #add
            | '-' expr                  #unary
            | '(' expr ')'              #paren
            ;

//Lexer rules:
G01         : ('G0'|'G1') ;
ML          : ('X'|'Y'|'Z'|'F'|'H') ;
G23         : ('G2'|'G3') ;
CL          : ('J'|'K') ;
NUM         : [0-9]+ ('.' [0-9]+)? ;
ID          : [a-z_]+ ;
TEXT        : '"' .*? '"' ;
COMPAR      : ('>' | '>=' | '==' | '<=' | '<') ;
MINUS       : '-' ;
WHITESPACE  : [ \t\r\n]         -> skip ;
COMMENT     : '#' .*? '\n'     -> skip ;