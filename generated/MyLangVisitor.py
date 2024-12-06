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


    # Visit a parse tree produced by MyLangParser#cond_stmt.
    def visitCond_stmt(self, ctx:MyLangParser.Cond_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#expr.
    def visitExpr(self, ctx:MyLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#math_func.
    def visitMath_func(self, ctx:MyLangParser.Math_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#return_stmt.
    def visitReturn_stmt(self, ctx:MyLangParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#file_open_stmt.
    def visitFile_open_stmt(self, ctx:MyLangParser.File_open_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#file_read_stmt.
    def visitFile_read_stmt(self, ctx:MyLangParser.File_read_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#file_write_stmt.
    def visitFile_write_stmt(self, ctx:MyLangParser.File_write_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#file_close_stmt.
    def visitFile_close_stmt(self, ctx:MyLangParser.File_close_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#import_stmt.
    def visitImport_stmt(self, ctx:MyLangParser.Import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#array_expr.
    def visitArray_expr(self, ctx:MyLangParser.Array_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#array_op.
    def visitArray_op(self, ctx:MyLangParser.Array_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#array_append.
    def visitArray_append(self, ctx:MyLangParser.Array_appendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#for_stmt.
    def visitFor_stmt(self, ctx:MyLangParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#range_.
    def visitRange_(self, ctx:MyLangParser.Range_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#functiondef.
    def visitFunctiondef(self, ctx:MyLangParser.FunctiondefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#parametros.
    def visitParametros(self, ctx:MyLangParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#func_call.
    def visitFunc_call(self, ctx:MyLangParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#while_stmt.
    def visitWhile_stmt(self, ctx:MyLangParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#condition.
    def visitCondition(self, ctx:MyLangParser.ConditionContext):
        return self.visitChildren(ctx)



del MyLangParser