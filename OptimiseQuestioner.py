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
        self.a = random.randint(1, 1)
        self.b = random.randint(1, 1) * 2  # Avoic francion x^4 coef.
        self.c = random.randint(-4, 5) * 3  # Avoid fractions /3
        self.d = random.randint(1, 1) * 2  # Avoic francion x^4 coef
        self.e = random.randint(-9, 20) * 3  # Avoid fractions /3
        self.f = random.randint(-5, 10)  # Constant of integration.

    def get_question(self):
        dy_dx_hidden = self.a*x*(self.b*x + self.c)*(self.d*x + self.e)
        dy_dx = sp.expand(dy_dx_hidden)
        d2y_dx2 = sp.diff(dy_dx)
        y = sp.integrate(dy_dx, x)
        y = y + self.f
        c_points = self.order2_conditions(d2y_dx2)
        return y, dy_dx, c_points

    def order2_conditions(self, d2y_dx2):
        d2y_dx2 = str(d2y_dx2)
        crit_points = {0: '', -self.c/self.b: '', -self.e/self.d: ''}
        for pt in crit_points.keys():
            x = pt
            soc = eval(d2y_dx2)
            if soc > 0:
                crit_points[pt] = 'Minimum'
            elif soc < 0:
                crit_points[pt] = 'Maximum'
            elif soc == 0:
                crit_points[pt] = 'Stationary Point'
        return crit_points


for n in range(10):
    Eq = Quartic(level='easy')
    print(Eq.get_question())
#  print()
#  print('y =', y)
#  print('dy/dx =', dy_dx)
