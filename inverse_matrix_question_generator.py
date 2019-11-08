#! /usr/bin/env python3

"""
This program will generate a random matrix, and its inverse.
It is designed to generate question and answer sheets quickly.

First it prompts for a dimension. eg:
    3 -> a 3x3 matrix
    2 -> a 2x2 matrix

Then it prompts for the number of matries required.
It then calculates the matrix and its inverse, and
outputs a .docx with the matrix-inverse pairs layed
out for a question sheet.
"""

import sympy as sp
from sympy.matrices import Matrix
import random
import os

f = open('deleteme.markdown', 'w')

matrix_size = int(input('\nHow many rows in your square matrix?\n \
                    enter 3 for a 3 x 3 matrix: '))
quant = int(input('How many matrices do you want? '))

for i in range(quant):
    elements = [random.randint(-9, 9) for x in range(matrix_size * matrix_size)]
    A = Matrix(matrix_size, matrix_size, elements)
    try:
        inv_A = A.inv()
    except ValueError:
        inv_A = 'Singular matrix'
    row = str('{}. $A = {}$\t\t$inv(A) = {}$\n\n'.format
              (
                   i + 1,
                   sp.latex(A),
                   sp.latex(inv_A)
              ))

    f.write(row)

f.close()
os.system('pandoc -o questionsheets/inverse_matrix_questions.docx deleteme.markdown')
os.remove('deleteme.markdown')
