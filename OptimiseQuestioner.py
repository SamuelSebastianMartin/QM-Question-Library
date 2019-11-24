#! /usr/bin/env python3

import random
import sympy as sp

#  Set up symbolic variables
x = sp.symbols('x')


class Quartic:
    """
    Returns a quartic Sympy equation, with optimsation data:
    y = f(x)
    Stationary points, with classification (max, min, inflection)
    dy/dx = f'(x),
    It starts by making dy/dx = ax(bx + c)(dx + e)
    If the kwarg level='easy', then a = b = d = 1
        and there will be no fractional coefficients.
    If the kwarg level='mid', then a = 1
    """
    def __init__(self, level='easy'):
        #  Set up random coefficients for the first derivative
        #  ax(bx + c)(dx + e)
        if level[0] == 'h' or level[0] == 3:
            self.a = random.randint(1, 4)
            self.b = random.randint(1, 3)
            self.c = random.randint(-9, 20)
            self.d = random.randint(1, 3)
            self.e = random.randint(-9, 20)
            self.f = random.randint(-15, 15)  # Constant of integration
        elif level[0] == 'm' or level[0] == 2:
            self.a = random.randint(1, 1)
            self.b = random.randint(1, 3)
            self.c = random.randint(-9, 20)
            self.d = random.randint(1, 3)
            self.e = random.randint(-9, 20)
            self.f = random.randint(-15, 15)  # Constant of integration
        else:
            self.a = random.randint(1, 1)
            self.b = random.randint(1, 1) * 2  # Avoic francion x^4 coef.
            self.c = random.randint(-4, 5) * 3  # Avoid fractions /3
            self.d = random.randint(1, 1) * 2  # Avoic francion x^4 coef
            self.e = random.randint(-9, 20) * 2  # Avoid fractions /2
            self.f = random.randint(-5, 10)  # Constant of integration.

    def get_question(self):
        dy_dx_hidden = self.a*x*(self.b*x + self.c)*(self.d*x + self.e)
        dy_dx = sp.expand(dy_dx_hidden)
        y = sp.integrate(dy_dx, x)
        y = y + self.f
        c_points = (0, -self.c/self.b, -self.e/self.d)
        return y, dy_dx, c_points


for n in range(10):
    Eq = Quartic(level='easy')
    print(Eq.get_question())
#  print()
#  print('y =', y)
#  print('dy/dx =', dy_dx)
