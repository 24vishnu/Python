import VendingMachineBL


def test_vending_machine():
    my_money = 123
    expected_result = 4
    result = VendingMachineBL.change(my_money)
    assert expected_result == result
