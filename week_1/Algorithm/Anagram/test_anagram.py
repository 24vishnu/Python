import AnagramBL


def test_anagram1():
    str1 = 'vishnu'
    str2 = 'isuvhn'
    assert True == AnagramBL.isAnagram(str2, str1)


def test_anagram2():
    str1 = 'vishnu'
    str2 = 'hsuvvn'
    assert False == AnagramBL.isAnagram(str2, str1)
