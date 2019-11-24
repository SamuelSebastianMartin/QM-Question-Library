#! /usr/bin/env python3

import random
import sympy as sp
sp.init_printing(use_unicode=True)

#  Set up symbols
x, y = sp.symbols('x y')

#  Set variables to use in symbolic expression
b = random.randint(0, 6)
c = random.randint(-10, 10)
d = random.randint(1,3)

#  Set up the function
a = x**d + b*x + c

#  Calculate the symbolic derivative
adash = sp.diff(a)

#  Get the numerical evaluation with 'N'
num = sp.N(adash)

#  Note coefficients are floats 'num'
print(num)
#  ...and ints in 'a' and 'adash'
print(a)
print(adash)


#  Do the calculation with non-symbolic
#  variables and 'eval()'
x = 2
print(a, '=', eval(str(a)))
print(adash, '=', eval(str(adash)))
