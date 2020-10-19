//1813130
grammar BKIT;
@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language = Python3;
}
program: declarations EOF ;
declarations: (var_decl)* (func_decl)*;

//var declaration

ID: [a-z] [_a-zA-Z0-9]*;

var_decl:
	VAR COLON many_var_decl SEMI; 
many_var_decl: one_var_decl (COMMA one_var_decl)* ;
one_var_decl: ID (LSB (INT_LIT) RSB)* (ASSIGN (INT_LIT | FLOAT_LIT | BOOLEAN_LIT | STRING_LIT | ARRAY_LIT))?;


//func declaration
func_decl:
	FUNCTION COLON func_name para_decl*  BODY COLON stm_list ENDBODY DOT ;
func_name: ID;
para_decl: PARAMETER COLON ((ID (LSB (INT_LIT) RSB)*)(COMMA (ID (LSB (INT_LIT) RSB)*))*);
//type
composit: ID (LSB INT_WITHOUT_0 INT* RSB)+;
scalar : ID;
//statement
stm_list: var_decl* stm_type*;
stm_type: 
	assign_stm
	| if_stm
	| for_stm (break_stm | continue_stm)?
	| while_stm (break_stm | continue_stm)?
	| do_while_stm (break_stm | continue_stm)?
	| call_stm 
	| return_stm
;

//assign_stm
assign_stm: (ID | (ID|func_call) index_op) ASSIGN exp SEMI;


//if statement

if_stm: IF exp THEN stm_list (ELSEIF exp THEN stm_list)* (ELSE stm_list)? ENDIF DOT;

//for statement

for_stm: FOR LP scalar ASSIGN INT_LIT COMMA exp COMMA exp RP DO stm_list ENDFOR DOT  ;

//while statment

while_stm: WHILE exp DO stm_list ENDWHILE DOT;

//do-while statement

do_while_stm: DO stm_list WHILE exp ENDDO DOT;

//break statement

break_stm: BREAK SEMI;

//continue statement

continue_stm: CONTINUE SEMI;

//call statement

call_stm: func_call SEMI;

//return statement

return_stm: RETURN exp SEMI;

//endstatement

//expression
INT_LIT: [0] | INT_WITHOUT_0 INT* | HEX | OCT;
BOOLEAN_LIT: TRUE | FALSE;
FLOAT_LIT: INT+ DEC? EXP | INT+ DEC EXP?;

exp:     exp1 EQUALINT exp1
        | exp1  NOT_EQUALINT exp1
        | exp1  LTHANINT exp1
        | exp1  GTHANINT exp1
        | exp1  LEQUALINT exp1
        | exp1  GEQUALINT exp1
        | exp1  NOT_EQUALFLOAT exp1
        | exp1  LTHANFLOAT exp1
        | exp1  GTHANFLOAT exp1
        | exp1  LEQUALFLOAT exp1
        | exp1  GEQUALFLOAT exp1
        | exp1;
exp1: exp1 AND exp2 | exp1 OR exp2 | exp2;
exp2: exp2 ADDINT exp3 | exp2 ADDFLOAT exp3 | exp2 SUBINT exp3 | exp2 SUBFLOAT exp3 | exp3;
exp3: exp3 MULINT exp4 | exp3 MULFLOAT exp4 | exp3 DIVINT exp4 | exp3 DIVFLOAT exp4 | exp3 MODINT exp4 | exp4;
exp4: NOT exp4 | exp5;
exp5: SUBINT exp5 | SUBFLOAT exp5 | exp6;
index_op: (LSB exp RSB)+ ;
exp6: INT_LIT | FLOAT_LIT | BOOLEAN_LIT | STRING_LIT | ARRAY_LIT | ID | func_call | LP exp RP | ((ID |func_call) index_op);
func_call: ID LP list_argument RP;
list_argument: (exp (COMMA exp)*)?;


// =====================LEXER==================\\


BODY: 'Body'; //Keyword
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
TRUE: 'True';
FALSE: 'False';
ENDDO: 'EndDo';
//EndKeyword
// Operators
ADDINT: '+';
ADDFLOAT: '+.';
SUBINT: '-';
SUBFLOAT: '-.';
MULINT: '*';
MULFLOAT: '*.';
DIVINT: '\\';
DIVFLOAT: '\\.';
MODINT: '%';
NOT: '!';
AND: '&&';
OR: '||';
NOT_EQUALINT: '!=';
EQUALINT: '==';
LTHANINT: '<';
GTHANINT: '>';
LEQUALINT: '<=';
GEQUALINT: '>=';
NOT_EQUALFLOAT: '=/=';
LTHANFLOAT: '<.';
GTHANFLOAT: '>.';
LEQUALFLOAT: '<=.';
GEQUALFLOAT: '>=.';
ASSIGN: '=';

//List operator

//endlist
//EndOperators
// Separators
LSB: '[';
RSB: ']';
LB: '{';
//angle bracket
RB: '}';
LP: '(';
//parenthesis
RP: ')';
COLON: ':';
SEMI: ';';
DOT: '.';
COMMA: ',';
//EndSeparators
COMMENT : '**' ((~'*') | ('*'~'*'))* '**' -> skip;
ARRAY_LIT: LB  ' '* (' '*(ARRAY_LIT | INT_LIT | FLOAT_LIT | BOOLEAN_LIT | STRING_LIT  ) ' '* 
(' '* COMMA ' '* (INT_LIT | FLOAT_LIT | BOOLEAN_LIT | STRING_LIT  | ARRAY_LIT ) ' '* )* ' '*)?  ' '* RB;
// Literal
INT: [0-9];
INT_WITHOUT_0: [1-9];

fragment HEX: '0' [xX]+ [1-9A-F]+ [0-9A-F]*;
// 0 must not begin after prefix
fragment OCT: '0' [oO]+ [1-7]+ [0-7]*;
// 0 must not begin after prefix
fragment EXP: [e|E] [+-]? INT+;
fragment DEC: '.' INT*;


WS: [ \t\r\n]+ -> skip;


// string
fragment STR_CHAR: ~[\n"'\\]|'\'' '"'| ESCAPE_SEQUENCES; 
fragment ESCAPE_SEQUENCES : ('\\' [bfrnt'\\]) ; 
fragment ESCAPE_ILLEGAL: '\\' ~[bfrnt'\\]|'\'';
STRING_LIT: '"' STR_CHAR* '"'{
        y = str(self.text)
        
        self.text = y[1:-1]
      
}; 
ILLEGAL_ESCAPE:'"' STR_CHAR* ESCAPE_ILLEGAL{
        y = str(self.text)
        
        raise IllegalEscape(y[1:]) 
};
UNCLOSE_STRING: '"' STR_CHAR* ([\n] | EOF){
        y = str(self.text)
        
        if y[-1] == '\n': 
                raise UncloseString(y[1:-1])
        else: 
                raise UncloseString(y[1:])
};


UNTERMINATED_COMMENT: '**'(~('*') ~('*'))*;
ERROR_CHAR:.{ 
        raise ErrorToken(self.text)
};
 