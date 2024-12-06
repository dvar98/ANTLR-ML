# Generated from MyLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete listener for a parse tree produced by MyLangParser.
class MyLangListener(ParseTreeListener):

    # Enter a parse tree produced by MyLangParser#program.
    def enterProgram(self, ctx:MyLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLangParser#program.
    def exitProgram(self, ctx:MyLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLangParser#stmt.
    def enterStmt(self, ctx:MyLangParser.StmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#stmt.
    def exitStmt(self, ctx:MyLangParser.StmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#print_stmt.
    def enterPrint_stmt(self, ctx:MyLangParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#print_stmt.
    def exitPrint_stmt(self, ctx:MyLangParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#assign_stmt.
    def enterAssign_stmt(self, ctx:MyLangParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#assign_stmt.
    def exitAssign_stmt(self, ctx:MyLangParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#expr_stmt.
    def enterExpr_stmt(self, ctx:MyLangParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#expr_stmt.
    def exitExpr_stmt(self, ctx:MyLangParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#cond_stmt.
    def enterCond_stmt(self, ctx:MyLangParser.Cond_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#cond_stmt.
    def exitCond_stmt(self, ctx:MyLangParser.Cond_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#expr.
    def enterExpr(self, ctx:MyLangParser.ExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#expr.
    def exitExpr(self, ctx:MyLangParser.ExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#math_func.
    def enterMath_func(self, ctx:MyLangParser.Math_funcContext):
        pass

    # Exit a parse tree produced by MyLangParser#math_func.
    def exitMath_func(self, ctx:MyLangParser.Math_funcContext):
        pass


    # Enter a parse tree produced by MyLangParser#return_stmt.
    def enterReturn_stmt(self, ctx:MyLangParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#return_stmt.
    def exitReturn_stmt(self, ctx:MyLangParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#file_open_stmt.
    def enterFile_open_stmt(self, ctx:MyLangParser.File_open_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#file_open_stmt.
    def exitFile_open_stmt(self, ctx:MyLangParser.File_open_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#file_read_stmt.
    def enterFile_read_stmt(self, ctx:MyLangParser.File_read_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#file_read_stmt.
    def exitFile_read_stmt(self, ctx:MyLangParser.File_read_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#file_write_stmt.
    def enterFile_write_stmt(self, ctx:MyLangParser.File_write_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#file_write_stmt.
    def exitFile_write_stmt(self, ctx:MyLangParser.File_write_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#file_close_stmt.
    def enterFile_close_stmt(self, ctx:MyLangParser.File_close_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#file_close_stmt.
    def exitFile_close_stmt(self, ctx:MyLangParser.File_close_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#import_stmt.
    def enterImport_stmt(self, ctx:MyLangParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#import_stmt.
    def exitImport_stmt(self, ctx:MyLangParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#array_expr.
    def enterArray_expr(self, ctx:MyLangParser.Array_exprContext):
        pass

    # Exit a parse tree produced by MyLangParser#array_expr.
    def exitArray_expr(self, ctx:MyLangParser.Array_exprContext):
        pass


    # Enter a parse tree produced by MyLangParser#array_op.
    def enterArray_op(self, ctx:MyLangParser.Array_opContext):
        pass

    # Exit a parse tree produced by MyLangParser#array_op.
    def exitArray_op(self, ctx:MyLangParser.Array_opContext):
        pass


    # Enter a parse tree produced by MyLangParser#array_append.
    def enterArray_append(self, ctx:MyLangParser.Array_appendContext):
        pass

    # Exit a parse tree produced by MyLangParser#array_append.
    def exitArray_append(self, ctx:MyLangParser.Array_appendContext):
        pass


    # Enter a parse tree produced by MyLangParser#for_stmt.
    def enterFor_stmt(self, ctx:MyLangParser.For_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#for_stmt.
    def exitFor_stmt(self, ctx:MyLangParser.For_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#range_.
    def enterRange_(self, ctx:MyLangParser.Range_Context):
        pass

    # Exit a parse tree produced by MyLangParser#range_.
    def exitRange_(self, ctx:MyLangParser.Range_Context):
        pass


    # Enter a parse tree produced by MyLangParser#functiondef.
    def enterFunctiondef(self, ctx:MyLangParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by MyLangParser#functiondef.
    def exitFunctiondef(self, ctx:MyLangParser.FunctiondefContext):
        pass


    # Enter a parse tree produced by MyLangParser#parametros.
    def enterParametros(self, ctx:MyLangParser.ParametrosContext):
        pass

    # Exit a parse tree produced by MyLangParser#parametros.
    def exitParametros(self, ctx:MyLangParser.ParametrosContext):
        pass


    # Enter a parse tree produced by MyLangParser#func_call.
    def enterFunc_call(self, ctx:MyLangParser.Func_callContext):
        pass

    # Exit a parse tree produced by MyLangParser#func_call.
    def exitFunc_call(self, ctx:MyLangParser.Func_callContext):
        pass


    # Enter a parse tree produced by MyLangParser#while_stmt.
    def enterWhile_stmt(self, ctx:MyLangParser.While_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#while_stmt.
    def exitWhile_stmt(self, ctx:MyLangParser.While_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#condition.
    def enterCondition(self, ctx:MyLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by MyLangParser#condition.
    def exitCondition(self, ctx:MyLangParser.ConditionContext):
        pass



del MyLangParser