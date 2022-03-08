# Generated from C:/Users/dennis.schwebius/PycharmProjects/advGcode\agCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .agCodeParser import agCodeParser
else:
    from agCodeParser import agCodeParser

# This class defines a complete listener for a parse tree produced by agCodeParser.
class agCodeListener(ParseTreeListener):

    # Enter a parse tree produced by agCodeParser#prog.
    def enterProg(self, ctx:agCodeParser.ProgContext):
        pass

    # Exit a parse tree produced by agCodeParser#prog.
    def exitProg(self, ctx:agCodeParser.ProgContext):
        pass


    # Enter a parse tree produced by agCodeParser#statement.
    def enterStatement(self, ctx:agCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by agCodeParser#statement.
    def exitStatement(self, ctx:agCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by agCodeParser#gLine.
    def enterGLine(self, ctx:agCodeParser.GLineContext):
        pass

    # Exit a parse tree produced by agCodeParser#gLine.
    def exitGLine(self, ctx:agCodeParser.GLineContext):
        pass


    # Enter a parse tree produced by agCodeParser#gMove.
    def enterGMove(self, ctx:agCodeParser.GMoveContext):
        pass

    # Exit a parse tree produced by agCodeParser#gMove.
    def exitGMove(self, ctx:agCodeParser.GMoveContext):
        pass


    # Enter a parse tree produced by agCodeParser#gCirc.
    def enterGCirc(self, ctx:agCodeParser.GCircContext):
        pass

    # Exit a parse tree produced by agCodeParser#gCirc.
    def exitGCirc(self, ctx:agCodeParser.GCircContext):
        pass


    # Enter a parse tree produced by agCodeParser#gWait.
    def enterGWait(self, ctx:agCodeParser.GWaitContext):
        pass

    # Exit a parse tree produced by agCodeParser#gWait.
    def exitGWait(self, ctx:agCodeParser.GWaitContext):
        pass


    # Enter a parse tree produced by agCodeParser#logic.
    def enterLogic(self, ctx:agCodeParser.LogicContext):
        pass

    # Exit a parse tree produced by agCodeParser#logic.
    def exitLogic(self, ctx:agCodeParser.LogicContext):
        pass


    # Enter a parse tree produced by agCodeParser#repeatStmt.
    def enterRepeatStmt(self, ctx:agCodeParser.RepeatStmtContext):
        pass

    # Exit a parse tree produced by agCodeParser#repeatStmt.
    def exitRepeatStmt(self, ctx:agCodeParser.RepeatStmtContext):
        pass


    # Enter a parse tree produced by agCodeParser#ifStmt.
    def enterIfStmt(self, ctx:agCodeParser.IfStmtContext):
        pass

    # Exit a parse tree produced by agCodeParser#ifStmt.
    def exitIfStmt(self, ctx:agCodeParser.IfStmtContext):
        pass


    # Enter a parse tree produced by agCodeParser#trueStats.
    def enterTrueStats(self, ctx:agCodeParser.TrueStatsContext):
        pass

    # Exit a parse tree produced by agCodeParser#trueStats.
    def exitTrueStats(self, ctx:agCodeParser.TrueStatsContext):
        pass


    # Enter a parse tree produced by agCodeParser#falseStats.
    def enterFalseStats(self, ctx:agCodeParser.FalseStatsContext):
        pass

    # Exit a parse tree produced by agCodeParser#falseStats.
    def exitFalseStats(self, ctx:agCodeParser.FalseStatsContext):
        pass


    # Enter a parse tree produced by agCodeParser#condition.
    def enterCondition(self, ctx:agCodeParser.ConditionContext):
        pass

    # Exit a parse tree produced by agCodeParser#condition.
    def exitCondition(self, ctx:agCodeParser.ConditionContext):
        pass


    # Enter a parse tree produced by agCodeParser#varDecl.
    def enterVarDecl(self, ctx:agCodeParser.VarDeclContext):
        pass

    # Exit a parse tree produced by agCodeParser#varDecl.
    def exitVarDecl(self, ctx:agCodeParser.VarDeclContext):
        pass


    # Enter a parse tree produced by agCodeParser#assign.
    def enterAssign(self, ctx:agCodeParser.AssignContext):
        pass

    # Exit a parse tree produced by agCodeParser#assign.
    def exitAssign(self, ctx:agCodeParser.AssignContext):
        pass


    # Enter a parse tree produced by agCodeParser#printLn.
    def enterPrintLn(self, ctx:agCodeParser.PrintLnContext):
        pass

    # Exit a parse tree produced by agCodeParser#printLn.
    def exitPrintLn(self, ctx:agCodeParser.PrintLnContext):
        pass


    # Enter a parse tree produced by agCodeParser#add.
    def enterAdd(self, ctx:agCodeParser.AddContext):
        pass

    # Exit a parse tree produced by agCodeParser#add.
    def exitAdd(self, ctx:agCodeParser.AddContext):
        pass


    # Enter a parse tree produced by agCodeParser#number.
    def enterNumber(self, ctx:agCodeParser.NumberContext):
        pass

    # Exit a parse tree produced by agCodeParser#number.
    def exitNumber(self, ctx:agCodeParser.NumberContext):
        pass


    # Enter a parse tree produced by agCodeParser#not.
    def enterNot(self, ctx:agCodeParser.NotContext):
        pass

    # Exit a parse tree produced by agCodeParser#not.
    def exitNot(self, ctx:agCodeParser.NotContext):
        pass


    # Enter a parse tree produced by agCodeParser#paren.
    def enterParen(self, ctx:agCodeParser.ParenContext):
        pass

    # Exit a parse tree produced by agCodeParser#paren.
    def exitParen(self, ctx:agCodeParser.ParenContext):
        pass


    # Enter a parse tree produced by agCodeParser#bool.
    def enterBool(self, ctx:agCodeParser.BoolContext):
        pass

    # Exit a parse tree produced by agCodeParser#bool.
    def exitBool(self, ctx:agCodeParser.BoolContext):
        pass


    # Enter a parse tree produced by agCodeParser#mul.
    def enterMul(self, ctx:agCodeParser.MulContext):
        pass

    # Exit a parse tree produced by agCodeParser#mul.
    def exitMul(self, ctx:agCodeParser.MulContext):
        pass


    # Enter a parse tree produced by agCodeParser#var.
    def enterVar(self, ctx:agCodeParser.VarContext):
        pass

    # Exit a parse tree produced by agCodeParser#var.
    def exitVar(self, ctx:agCodeParser.VarContext):
        pass


    # Enter a parse tree produced by agCodeParser#unary.
    def enterUnary(self, ctx:agCodeParser.UnaryContext):
        pass

    # Exit a parse tree produced by agCodeParser#unary.
    def exitUnary(self, ctx:agCodeParser.UnaryContext):
        pass


    # Enter a parse tree produced by agCodeParser#compar.
    def enterCompar(self, ctx:agCodeParser.ComparContext):
        pass

    # Exit a parse tree produced by agCodeParser#compar.
    def exitCompar(self, ctx:agCodeParser.ComparContext):
        pass



del agCodeParser