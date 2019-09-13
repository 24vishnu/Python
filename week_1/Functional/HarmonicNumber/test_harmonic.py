import Harmonic_NumberBL


def test_Nth_number():
    num = 5
    assert 2.28 == round(Harmonic_NumberBL.Nth_Number(num), 2)
