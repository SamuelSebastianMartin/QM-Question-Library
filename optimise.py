#! /usr/bin/env python3

import sympy as sp
import OptimiseQuestioner as op


Eq = op.Optimiser()
quad = Eq.quadratic()
y = sp.latex(quad[0])
dy = sp.latex(quad[1])
answers = quad[2]
ans = ['$y = ', y, '$: Answer: ']

for x in answers:
    ans.append(' {} at $x = {}$ '.format(sp.latex(answers[x]), sp.latex(x)))
ans.append('$\\frac{dy}{dx} = ')
ans.append(dy)
ans.append('$')

question = ''.join(ans)

cube = Eq.cubic()
quart = Eq.quartic()[0]
print(question)
