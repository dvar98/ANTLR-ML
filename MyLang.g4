grammar MyLang;

program: stmt+ EOF;

TKN_PAR_IZ:'(';
TKN_PAR_DER:')';

stmt
    : assign_stmt
    | print_stmt
    | expr_stmt
    | for_stmt
    | cond_stmt
    | while_stmt
    | functiondef
    | array_append
    | import_stmt
    | file_open_stmt
    | file_read_stmt
    | file_write_stmt
    | file_close_stmt
    | return_stmt
    ;

print_stmt
    : 'cout' '(' expr (',' expr)* ')'
    ;

assign_stmt
    : IDENT '=' expr
    ;

expr_stmt
    : expr
    ;

cond_stmt
    : 'if' condition ':' stmt+ ('else' ':' stmt+)? 'end'
    ;

expr
    : expr ('+' | '-' | '*' | '/' | '%' | 'T' | 'inv') expr
    | array_op
    | array_expr
    | IDENT
    | NUMBER
    | STRING
    | expr 'T'
    | 'inv' expr
    | math_func
    | func_call
    ;

math_func
    : 'sin' '(' expr ')'
    | 'cos' '(' expr ')'
    | 'tan' '(' expr ')'
    | 'asin' '(' expr ')'
    | 'acos' '(' expr ')'
    | 'atan' '(' expr ')'
    | 'atan2' '(' expr ',' expr ')'
    | 'sinh' '(' expr ')'
    | 'cosh' '(' expr ')'
    | 'tanh' '(' expr ')'
    | 'sqrt' '(' expr ')'
    | 'log' '(' expr ')'
    | 'log10' '(' expr ')'
    | 'exp' '(' expr ')'
    | 'pow' '(' expr ',' expr ')'
    | 'fabs' '(' expr ')'
    | 'ceil' '(' expr ')'
    | 'floor' '(' expr ')'
    | 'trunc' '(' expr ')'
    | 'factorial' '(' expr ')'
    | 'gcd' '(' expr ',' expr ')'
    | 'comb' '(' expr ',' expr ')'
    | 'isfinite' '(' expr ')'
    | 'isinf' '(' expr ')'
    | 'isnan' '(' expr ')'
    | 'abs' '(' expr ')'
    | 'degrees' '(' expr ')'
    ;


return_stmt
    : 'return' expr
    ;

file_open_stmt
    : IDENT '=' 'open' '(' expr ',' expr ')'
    ;

file_read_stmt
    : IDENT '=' IDENT '.read' '(' ')'
    ;

file_write_stmt
    : IDENT '.write' '(' expr ')'
    ;

file_close_stmt
    : IDENT '.close' '(' ')'
    ;

import_stmt
    : 'import' IDENT (',' IDENT)*
    ;

array_expr
    : '[' (expr (',' expr)*)? ']'
    | IDENT '[' expr ']'
    ;

array_op
    : array_expr ('+' | '-' | '*' | '/') array_expr
    ;

array_append
    : IDENT '.append' '(' expr ')'
    ;

for_stmt
    : 'for' IDENT 'in' (range_ | expr) ':' stmt+ 'end'
    ;

range_
    : expr ',' expr (',' expr)?
    ;

functiondef
    : 'funcion' IDENT TKN_PAR_IZ parametros? TKN_PAR_DER '{' stmt+ '}'
    ;

parametros
    : IDENT (',' IDENT)*
    ;

func_call
    : IDENT TKN_PAR_IZ (expr (',' expr)*)? TKN_PAR_DER
    ;

while_stmt
    : 'while' condition ':' stmt+ 'end'
    ;

condition
    : expr ('>' | '<' | '==' | '!=') expr
    ;

IDENT
    : [a-zA-Z_][a-zA-Z0-9_]*( '.' [a-zA-Z_][a-zA-Z0-9_]* )*
    ;

NUMBER
    : '-'? [0-9]+ ('.' [0-9]+)?
    ;

STRING
    : '"' (~["\r\n])* '"'
    ;

WS
    : [ \t\n\r]+ -> skip
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;

NEWLINE
    : [\n]
    ;