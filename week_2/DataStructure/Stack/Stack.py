"""
Desc ­> Take an Arithmetic Expression such as
(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
performance of operations. Ensure parentheses must appear in a balanced
fashion.

I/P ­> read in Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)

Logic ­> Write a Stack Class to push open parenthesis “(“ and pop closed
parenthesis “)”. At the End of the Expression if the Stack is Empty then the
Arithmetic Expression is Balanced. Stack Class Methods are Stack(), push(),
pop(), peak(), isEmpty(), size()

O/P ­> True or False to Show Arithmetic Expression is balanced or not.
"""

import StackBL

# given Arithmetic expression
expression = '(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)'  # input()

# now check expression is balanced or not
st = StackBL
print(st.checkExpre(expression))
