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

    def inverse(self):
        """
        Creates a random square matrix and returns it with its inverse.
        The size of the matix is determined when the class is instantiated.
        The matrix, A, is comprised of integers from -9 to 9, and if
        'symbols' is non-zero, then that many non numberial elements
        will be added.
        """
        elmnt_count = self.rows * self.rows
        elements = [random.randint(-9, 9) for x in range(elmnt_count)]
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
        syms = ['a', '(1-a)', 'b', '(b+1)', 'ab', '2(a-b)']
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


a = MatrixQuestioner(3)
A, inv_A = a.inverse()
print(A)
print(inv_A)

b = MatrixQuestioner(3, symbols=65)
B, inv_B = b.inverse()
print(B)
print(inv_B)
