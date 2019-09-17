import StackBL


def test_Arithmetic():
    arithmetic_expression = '(((0)))'
    expected = True
    result = StackBL.checkExpre(arithmetic_expression)
    assert expected == result


def test_Arithmetic1():
    arithmetic_expression = '((())))'
    expected = False
    result = StackBL.checkExpre(arithmetic_expression)
    assert expected == result
