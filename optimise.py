#! /usr/bin/env python3

import sympy as sp
import os
import OptimiseQuestioner as op

questions = []


def add_question_string(order):
    """
    This produces a single question and answer for the
    order of equation that it is passed. It returns a
    printable Latex string including both Q & A.

    """
    eq = op.Optimiser(order)
    equation = eq.equation
    y = sp.latex(equation[0])
    dy = sp.latex(equation[1])
    critical_pts = equation[2]
    ans = ['$y = ', y, '$ : ']

    #  Loop through critical points, adding them to the ans list
    for x in critical_pts:
        ans.append(sp.latex(critical_pts[x]))
        ans.append(' at $x = ')
        ans.append(sp.latex(x))
        ans.append('$, ')
    #  Append the first derivative
    ans.append('$\\frac{dy}{dx} = ')
    ans.append(dy)
    ans.append('$\n\n')

    #  Join the question and answer into single, printable string.
    question = ''.join(ans)
    return question


def get_all_questions():
    """
    Asks user for the number of each question type, and
    returns a list of requested questions, as Latex strings.
    """
    no_quad = input('How many quadratic questions: ')
    no_cubic = input('How many cubic questions: ')
    no_quart = input('How many quartic questions: ')
    for n in range(int(no_quad)):
        question = add_question_string('quadratic')
        questions.append(question)
    for n in range(int(no_cubic)):
        question = add_question_string('cubic')
        questions.append(question)
    for n in range(int(no_quart)):
        question = add_question_string('quartic')
        questions.append(question)
    return questions


def print_question_sheet(questions):
    with open('temp3.md', 'w') as f:
        for question in questions:
            f.write(question)
    #  Convert to docx
    os.system('pandoc -o questionsheets/simple_optimisation.docx temp3.md')
    os.remove('temp3.md')


def main():
    questions = get_all_questions()
    print_question_sheet(questions)


if __name__ == '__main__':
    main()
