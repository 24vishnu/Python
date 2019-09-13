import copy

import BubbleSortBl


def test_file_data_sorting():
    list_data = BubbleSortBl.convert_words_list(BubbleSortBl.read_file())
    copy_list = copy.deepcopy(list_data)

    assert copy_list != BubbleSortBl.bubbleSort(list_data)


def test_file_data_sorting1():
    list_data = BubbleSortBl.convert_words_list(BubbleSortBl.read_file())

    expected_result = copy.deepcopy(list_data)
    expected_result.sort()

    assert expected_result == BubbleSortBl.bubbleSort(list_data)
