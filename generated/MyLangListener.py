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


    # Enter a parse tree produced by MyLangParser#plot_stmt.
    def enterPlot_stmt(self, ctx:MyLangParser.Plot_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#plot_stmt.
    def exitPlot_stmt(self, ctx:MyLangParser.Plot_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#file_stmt.
    def enterFile_stmt(self, ctx:MyLangParser.File_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#file_stmt.
    def exitFile_stmt(self, ctx:MyLangParser.File_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#cond_stmt.
    def enterCond_stmt(self, ctx:MyLangParser.Cond_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#cond_stmt.
    def exitCond_stmt(self, ctx:MyLangParser.Cond_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#func_stmt.
    def enterFunc_stmt(self, ctx:MyLangParser.Func_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#func_stmt.
    def exitFunc_stmt(self, ctx:MyLangParser.Func_stmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#regression_stmt.
    def enterRegression_stmt(self, ctx:MyLangParser.Regression_stmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#regression_stmt.
    def exitRegression_stmt(self, ctx:MyLangParser.Regression_stmtContext):
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