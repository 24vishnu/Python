# ---------------------------------- prg-----------------------------------------------
# sort_str_from_file2.py
# date : 26/08/2019
# sort the data using bubble sort algo and find requred time to sort data


import time


# bubble sort
def bubbleSort(all_values):
    startTime = time.time()

    for i in range(0, len(all_values), 1):
        for j in range(0, len(all_values) - (i + 1), 1):
            if all_values[j] > all_values[j + 1]:
                t = all_values[j]
                all_values[j] = all_values[j + 1]
                all_values[j + 1] = t

    print('Time : ', round(time.time() - startTime, 10))

    return all_values


# before sorting we convert string as a list of every word
def convert_words_list(data):
    word = ""
    string = data.strip().strip('.').strip(',')
    list_obj = []

    for i in range(len(string)):
        if string[i] == ' ':
            if len(word) > 0:
                list_obj.append(word)
                word = ""

        elif ('a' <= string[i] <= 'z') or ('A' <= string[i] <= 'Z'):
            word += string[i]

    if len(word) > 0:
        list_obj.append(word)

    print("\n")
    return list_obj


def read_file():
    with open("demo.txt") as f:
        data = f.read()
        return data
