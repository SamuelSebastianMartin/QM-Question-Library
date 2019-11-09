#! /usr/bin/env python3

"""
this produces random systems of equations, Ax = d,
along with:
    their solutions
    the inverse coefficient matrix
    the determinants for Cramer's rule calculations
"""

import os
import MatrixQuestioner as mxq

rows = int(input('\nSize of equation system?\n \
    (No more than 6 is possible) enter an integer: '))
quantity = int(input('How many equations do you want? '))

questions = []  # Container for output questions.

for n in range(quantity):
    system = mxq.MatrixQuestioner(rows)
    A, x, d, ans = system.solve_system()
    question = '{}{} = {} \tanswer: {}\n\n'.format(A, x, d, ans)

    questions.append(question)

with open('temp.markdown', 'w') as f:
    for question in questions:
        f.write(question)

os.system('pandoc -o questionsheets/system_solve.docx temp.markdown')
os.remove('temp.markdown')
