#! /usr/bin/env python3

import sympy as sp
from sympy.matrices import Matrix
import random


class MatrixQuestioner:
    """
    This class produces Latex printable questions and answers
    for common basic matrix topics
    Usage:
        A = MatrixQuestioner(3) # setup for 3 rows
        A.inverse() # Returns a 3x3 matrix and its inverse
        #A.simultaneous() # Returns a system of 3 simultaneous
        #                 equations, and the answer vector.

    Two keyword argumets are available:
      * 'symbols' (default=0) is the number of non-numberic symbols
        to be included in the matrix, A.
      * 'latex_dollar_wrap' (default=True) ensures that the returned
        strings begin and end with a '$', for Latex printing.
    """
    def __init__(self, rows, symbols=0, latex_dollar_wrap=True):
        self.rows = rows
        self.symbols = symbols
        self.wrap = latex_dollar_wrap
        self.elmnt_count = self.rows * self.rows

    def inverse(self):
        """
        Creates a random square matrix and returns it with its inverse.
        The size of the matix is determined when the class is instantiated.
        The matrix, A, is comprised of integers from -9 to 9, and if
        'symbols' is non-zero, then that many non numberial elements
        will be added.
        """
        elements = [random.randint(-9, 9) for x in range(self.elmnt_count)]
        if self.symbols > 0:
            elements = self.insert_symbols(elements)
        A = Matrix(self.rows, self.rows, elements)
        try:
            inv_A = A.inv()
        except ValueError:
            inv_A = 'Singular matrix'
        A = self.printable(A)
        inv_A = self.printable(inv_A)
        return A, inv_A

    def insert_symbols(self, elements):
        """
        Relplaces matrix elements with one from a range
        of symbols. Both the element replaced and the
        symbol chosen are random.
        The number of exements replaced will be between
        1 and the instance variable, 'symbols'.
        """
        a, b = sp.symbols('a b')
        syms = ['a', '(1-a)', 'b', '(b+1)', 'a*b', '2*(a-b)']
        for s in range(self.symbols):
            sym_indx = random.randint(0, len(syms) - 1)
            elmt_indx = random.randint(0, len(elements) - 1)
            elements[elmt_indx] = syms[sym_indx]
        return elements

    def printable(self, M):
        """
        Returns a printable string of the Latex representation of
        the matrix.
        If latex_dollar_wrap is True (default), then the string
        returned will begin and end with a $ sign.
        """
        M = sp.latex(M)
        M = str(M)
        if self.wrap:
            M = '$' + M + '$'
        return M

    def simultaneous_setup(self):
        """
        Sets up a system of equations Ax = d, plus ans (a
        vector representing the values of the x vector.
        All vectors remain sympy objects (not strings), so
        they can be passed to other functions to return
        printable strings.
        """
        #  Set up 'ans'
        ans_values = [random.randint(-9, 9) for x in range(self.rows)]
        ans = Matrix(self.rows, 1, ans_values)  # Final answers: x in Ax = d.

        #  Set up 'A'
        A_values = [random.randint(-3, 12) for x in range(self.elmnt_count)]
        A = Matrix(self.rows, self.rows, A_values)  # Coefficient matrix: A in Ax = d.

        #  Set up 'd'
        d = A * ans  # RHS of equations: d in Ax = d.

        #  Set up 'x'  (Using strings, not symbols)
        var_names = ['x', 'y', 'z', 'u', 'v', 'w']  # The variables as names.
        if self.rows > len(var_names):
            raise Exception('Insufficient variable symbols for this size')
        x = Matrix(self.rows, 1, [var_names[i] for i in range(self.rows)])
        return A, x, d, ans

    def solve_system(self):
        A, x, d, ans = a.simultaneous_setup()
        A = self.printable(A)
        x = self.printable(x)
        d = self.printable(d)
        ans = self.printable(ans)
        return A, x, d, ans


a = MatrixQuestioner(3)
A, x, d, ans = a.solve_system()
print(A)
print(x)
print(d)
print(ans)
