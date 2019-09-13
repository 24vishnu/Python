import Anagram_Palindrome_PrimeBL


def test_prime():
    assert Anagram_Palindrome_PrimeBL.prime(113) == True


def test_palindrome():
    value = 12321
    assert Anagram_Palindrome_PrimeBL.palind(value) == True


def test_anagram():
    value1 = 12321
    value2 = 23121
    assert Anagram_Palindrome_PrimeBL.anagram(value1, value2) == True


def test_prime1():
    assert Anagram_Palindrome_PrimeBL.prime('28') == False


def test_palindrome1():
    value = 13421
    assert Anagram_Palindrome_PrimeBL.palind(value) == False


def test_anagram1():
    value1 = 12321
    value2 = 12345
    assert Anagram_Palindrome_PrimeBL.anagram(value1, value2) == False
