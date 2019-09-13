import copy

import BinarySearchBL


def test_insertion_sorting():
    unsorted_data = [1, 3, 7, 12, 978, 21, 54, 62, 65]
    sorted_data = [1, 3, 7, 12, 21, 54, 62, 65, 978]
    assert sorted_data == BinarySearchBL.insertionSort(unsorted_data)


def test_bubble_sorting():
    unsorted_data = [1, 3, 7, 12, 978, 21, 54, 62, 65]
    sorted_data = [1, 3, 7, 12, 21, 54, 62, 65, 978]
    assert sorted_data == BinarySearchBL.bubbleSort(unsorted_data)


def test_binary_search():
    sorted_data = [1, 3, 7, 12, 21, 54, 62, 65, 978]
    assert BinarySearchBL.bnarySerch(sorted_data, 54) == True


def test_binary_search1():
    sorted_data = [1, 3, 7, 12, 21, 54, 62, 65, 978]
    assert BinarySearchBL.bnarySerch(sorted_data, 100) == False


def test_insertion_sorting1():
    unsorted_data = [1, 3, 7, 12, 978, 21, 54, 62, 65]
    copy_list = copy.deepcopy(unsorted_data)
    assert BinarySearchBL.insertionSort(copy_list) != unsorted_data


def test_bubble_sorting1():
    unsorted_data = [1, 3, 7, 12, 978, 21, 54, 62, 65]
    copy_list = []
    for val in unsorted_data:
        copy_list.append(val)
    assert copy_list != BinarySearchBL.bubbleSort(unsorted_data)
