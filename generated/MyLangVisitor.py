# Generated from MyLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete generic visitor for a parse tree produced by MyLangParser.

class MyLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLangParser#program.
    def visitProgram(self, ctx:MyLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#stmt.
    def visitStmt(self, ctx:MyLangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#print_stmt.
    def visitPrint_stmt(self, ctx:MyLangParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MyLangParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#expr_stmt.
    def visitExpr_stmt(self, ctx:MyLangParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#plot_stmt.
    def visitPlot_stmt(self, ctx:MyLangParser.Plot_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#file_stmt.
    def visitFile_stmt(self, ctx:MyLangParser.File_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#cond_stmt.
    def visitCond_stmt(self, ctx:MyLangParser.Cond_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#func_stmt.
    def visitFunc_stmt(self, ctx:MyLangParser.Func_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#expr.
    def visitExpr(self, ctx:MyLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#math_func.
    def visitMath_func(self, ctx:MyLangParser.Math_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#array_expr.
    def visitArray_expr(self, ctx:MyLangParser.Array_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#array_op.
    def visitArray_op(self, ctx:MyLangParser.Array_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#for_stmt.
    def visitFor_stmt(self, ctx:MyLangParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#range_.
    def visitRange_(self, ctx:MyLangParser.Range_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#while_stmt.
    def visitWhile_stmt(self, ctx:MyLangParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#condition.
    def visitCondition(self, ctx:MyLangParser.ConditionContext):
        return self.visitChildren(ctx)



del MyLangParser