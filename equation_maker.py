#! /usr/bin/env python3

import random
import sympy as sp

#  Set up symbolic variables
x = sp.symbols('x')

for i in range(10):
    #  Set up random coefficients for the first derivative
    #  ax(bx + c)(dx + e)
    a = random.randint(1, 1)
    b = random.randint(1, 3)
    c = random.randint(-9, 20)
    d = random.randint(1, 3)
    e = random.randint(-9, 20)
    f = random.randint(-15, 15)  # This will be const of integration.

    dy_dx_hidden = a*x*(b*x + c)*(d*x + e)
    dy_dx = sp.expand(dy_dx_hidden)
    y = sp.integrate(dy_dx, x)
    y = y + f

    print()
    print('y =', y)
    print('dy/dx =', dy_dx)
