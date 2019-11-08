#! /usr/bin/env python3

"""
this produces random systems of equations, Ax = d,
along with:
    their solutions
    the inverse coefficient matrix
    the determinants for Cramer's rule calculations
"""

from sympy.matrices import Matrix
import sympy as sp
import random
import os

rows = int(input('\nHow many simultaneous equations do you want?\n \
        (No more than 6 is possible) enter an integer: '))
no_of_questions = int(input('How many matrices do you want? '))


questions = []  # Container for output questions.

for n in range(no_of_questions):
    #  Set up System Ax = b
    ans_values = [random.randint(-9, 9) for x in range(rows)]
    ans = Matrix(rows, 1, ans_values)  # Final answers: x in Ax = d.

    A_values = [random.randint(-3, 12) for x in range(rows * rows)]
    A = Matrix(rows, rows, A_values)  # Coefficient matrix: A in Ax = d.

    dbar = A * ans  # RHS of equations: d in Ax = d.
    indi_variables = ['x', 'y', 'z', 'u', 'v', 'w']  # The variables as names.
    if rows > len(indi_variables):
        raise Exception('There are not enough variable symbols for this size')
    x_bar = Matrix(rows, 1, [indi_variables[i] for i in range(rows)])

    #  Printable matrix equation.
    system_inner = str(sp.latex(A))  \
                    + str(sp.latex(x_bar))  \
                    + '='  \
                    + str(sp.latex(dbar))
    system_latex = sp.latex(system_inner)
    system_printable = '$' + system_latex + '$'

    answer_latex = sp.latex(ans)
    answer_printable = '$' + answer_latex + '$\n\n'

    #  Printable answer
    output = [system_printable, '\t\tAnswer = ', answer_printable]
    output = ''.join(output)
    questions.append(output)

with open('matrix_eq_system.markdown', 'w') as f:
    for question in questions:
        f.write(question)

os.system('pandoc -o questionsheets/matrix_eq_system.docx matrix_eq_system.markdown')
os.remove('matrix_eq_system.markdown')
