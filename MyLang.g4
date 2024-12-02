grammar MyLang;

program: stmt+ EOF;

stmt: assign_stmt
    | print_stmt
    | expr_stmt
    | plot_stmt
    | file_stmt
    | for_stmt
    | cond_stmt
    | func_stmt
    | while_stmt
    | regression_stmt
    ;

print_stmt: 'print' '(' expr (',' expr)* ')' ';';
assign_stmt: IDENT '=' expr ';';
expr_stmt: expr ';';
plot_stmt: 'plot' '(' IDENT ',' IDENT (',' STRING)* ')' ';';
file_stmt: ('read' | 'write' | 'append' | 'create') '(' STRING (',' STRING)* ')' ';';
cond_stmt: 'if' condition ':' stmt+ ('else:' stmt+)?;
func_stmt: 'regression' '(' IDENT ',' IDENT ')' ';';
regression_stmt: 'regression' '(' IDENT ',' IDENT ',' IDENT ',' IDENT ')' ';';

expr: expr ('+' | '-' | '*' | '/' | '%' | 'T' | 'inv') expr
    | array_op
    | array_expr
    | IDENT
    | NUMBER
    | STRING
    | expr 'T'
    | 'inv' expr
    | math_func
    ;

math_func:
    'sin' '(' expr ')'
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

array_expr
    : '[' (expr (',' expr)*)? ']'
    | IDENT '[' expr ']'
    ;

array_op
    : array_expr ('+' | '-' | '*' | '/') array_expr
    ;

for_stmt
    : 'for' IDENT 'in' (range_ | expr) ':' stmt+ 'end'
    ;

range_
    : expr ',' expr (',' expr)?  // Rango con inicio, fin y paso opcional
    ;

while_stmt: 'while' condition ':' stmt+ 'end';

condition: expr ('>' | '<' | '==' | '!=') expr;
IDENT: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["\r\n])* '"';
WS: [ \t\n\r]+ -> skip;