import MergeSortBL


def test_merge_sort_algo():
    unsorted_values = [62, 5, 2, 8, 23, 1, 67, 9, 3, 78, 19, 32, 53, 83]
    sorted_values = [62, 5, 2, 8, 23, 1, 67, 9, 3, 78, 19, 32, 53, 83]

    # sort by inbuilt method
    sorted_values.sort()

    # sort by own merge sort method
    MergeSortBL.merge_part(unsorted_values)
    assert sorted_values == unsorted_values
