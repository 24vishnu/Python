import DecimalToBinaryBL


def test_32bit_binary_number():
    result = DecimalToBinaryBL.toBinary(7)
    expected = '00000000000000000000000000000111'
    assert result == expected
