import random
from math import *
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""

    def fun(x,y):
        return sin(tan(x)+tan(y))
    def fun2(x,y):
        return cos(sin(x)-cos(y))
    def fun3(x,y):
        ret = '{0}*{0}*{0}'.format(random.choice([sin(x), tan(x),cos(x),sin(y),tan(x),cos(y)]))
        return eval(ret)
    return random.choice([fun,fun2,fun3])

def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
