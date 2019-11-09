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

import os
import MatrixQuestioner as mq

rows = int(input('\nHow many rows in matrices?\n \
    enter 3 for a 3 x 3 matrix: '))
quantity = int(input('How many matrices do you want? '))

questions = []
for i in range(quantity):
    matrix = mq.MatrixQuestioner(rows)
    A, inv_A = matrix.inverse()
    question = 'A = {}\t\tinv(A) = {}\n\n'.format(A, inv_A)
    questions.append(question)


with open('temp1.markdown', 'w') as f:
    for question in questions:
        f.write(question)

os.system('pandoc -o questionsheets/inverse_matrix.docx temp1.markdown')
os.remove('temp1.markdown')
