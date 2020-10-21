from plox.tool.Expr import *

class AstPrinter(Visitor):
    def __init__(self):
        pass

    def print(self, expr: Expr):
        print('I got this' + expr.__str__())
        return expr.accept(self)

    def visitBinaryExpr(self,expr:Binary):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visitGroupingExpr(self, expr:Grouping):
        return self.parenthesize("group", expr.expression)

    def visitLiteralExpr(self,expr:Literal):
        if expr.value:
            return expr.value
        return 'nil'

    def visitUnaryExpr(self,expr:Unary):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name: str, *exprs):
        returnString = ""
        returnString += f'({name}'
        for expr in exprs:
            returnString += f' {expr.accept(self)}'

        returnString += ')'
        return returnString

