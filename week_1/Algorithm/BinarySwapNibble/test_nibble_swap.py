import BinarySwapNibbleBL


def test_decimal_to_binary():
    result = BinarySwapNibbleBL.BaseConvertor.dcimalToBinary(25)
    expected = '11001'
    assert expected == result


def test_nibble_binary():
    result = BinarySwapNibbleBL.BaseConvertor.toBinary(25)
    expected = '00011001'
    assert expected == result


def test_swap_nibble():
    result = BinarySwapNibbleBL.BaseConvertor.swapNibbles('00011001')
    expected = '10010001'
    assert expected == result


def test_binary_decimal():
    result = BinarySwapNibbleBL.BaseConvertor.toDecimal('00011001')
    expected = 25
    assert expected == result
