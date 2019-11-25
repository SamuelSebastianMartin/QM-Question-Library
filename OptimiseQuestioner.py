#! /usr/bin/env python3

import random
import sympy as sp

#  Set up symbolic variables
x = sp.symbols('x')


class Optimiser:
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
    def __init__(self, order):
        self.order = order
        if self.order == 'quadratic':
            self.equation = self.quadratic()
        elif self.order == 'cubic':
            self.equation = self.cubic()
        elif self.order == 'quartic':
            self.equation = self.quartic()
        else:
            raise Exception('Pass an equation type:  \
                    quadratic, cubic or quartic')

    def __repr__(self):
        return self.order

    def quadratic(self):
        #  Set up random coefficients for the first derivative
        #  (bx + c)
        self.b = random.randint(-9, 10) * 2
        if self.b == 0:
            self.b += 2
        #  Set c as multiple of b to avoid fractional roots.
        self.c = random.randint(-3, 6) * self.b
        if self.c == 0:
            self.c = self.b
        self.f = random.randint(-5, 10)  # Constant of integration.
        #  Get question data
        dy_dx_hidden = self.b*x + self.c
        y, dy_dx, d2y_dx2 = self.all_derivatives(dy_dx_hidden)
        crit_points = {-self.c/self.b: ''}
        c_points = self.classify(d2y_dx2, crit_points)
        return y, dy_dx, c_points

    def cubic(self):
        #  Set up random coefficients for the first derivative
        #  (bx + c)(dx + e)
        self.b = random.randint(-1, 1) * 3  # Avoid fractions /3
        if self.b == 0:
            self.b += 3
        #  Set c as multiple of b to avoid fractional roots.
        self.c = random.randint(-3, 6) * self.b
        if self.c == 0:
            self.c = self.b
        self.d = random.randint(1, 1)
        #  Set e as multiple of d to avoid fractional roots.
        self.e = random.randint(-3, 6) * self.d
        if self.e == 0:
            self.e = self.d
        self.f = random.randint(-5, 10)  # Constant of integration.
        #  Get question data
        dy_dx_hidden = (self.b*x + self.c)*(self.d*x + self.e)
        y, dy_dx, d2y_dx2 = self.all_derivatives(dy_dx_hidden)
        crit_points = {-self.c/self.b: '', -self.e/self.d: ''}
        c_points = self.classify(d2y_dx2, crit_points)
        return y, dy_dx, c_points

    def quartic(self):
        #  Set up random coefficients for the first derivative
        #  ax(bx + c)(dx + e)
        self.a = random.randint(1, 1)
        if self.a == 0:
            self.a += 1
        self.b = random.randint(1, 1) * 2  # Avoic francion x^4 coef.
        self.c = random.randint(-4, 5) * 3  # Avoid fractions /3
        self.d = random.randint(1, 1) * 2  # Avoic francion x^4 coef
        self.e = random.randint(-9, 20) * 3  # Avoid fractions /3
        self.f = random.randint(-5, 10)  # Constant of integration.
        #  Get question data
        dy_dx_hidden = self.a*x*(self.b*x + self.c)*(self.d*x + self.e)
        y, dy_dx, d2y_dx2 = self.all_derivatives(dy_dx_hidden)
        crit_points = {0: '', -self.c/self.b: '', -self.e/self.d: ''}
        c_points = self.classify(d2y_dx2, crit_points)
        return y, dy_dx, c_points

    def all_derivatives(self, dy_dx_hidden):
        dy_dx = sp.expand(dy_dx_hidden)
        d2y_dx2 = sp.diff(dy_dx)
        y = sp.integrate(dy_dx, x)
        y = y + self.f
        return y, dy_dx, d2y_dx2

    def classify(self, d2y_dx2, crit_points):
        """
        Uses 'eval()' to check the 2nd order conditions.
        Returns a dictionary with critical-x-value as key,
        and max-min-stationary as value.
        """
        d2y_dx2 = str(d2y_dx2)
        for x in crit_points.keys():  # x is the key AND the variable.
            soc = eval(d2y_dx2)
            if soc > 0:
                crit_points[x] = 'Min'
            elif soc < 0:
                crit_points[x] = 'Max'
            elif soc == 0:
                crit_points[x] = 'Inflect'
        return crit_points
