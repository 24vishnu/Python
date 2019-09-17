# ---------------------------------- prg-----------------------------------------------
# HashingClass.py
# date : 26/08/2019
# update the file data (numbers) using hashing property


class Hashing:

    def __init__(self):
        self.hashList = []
        i = 0
        while i < 10:
            self.hashList.append([])
            i += 1

    # we consider capacity of hash table 10
    def addData(self, n):
        if n not in self.hashList[n % 10]:
            self.hashList[n % 10].append(n)

    # create search function to find element
    def search(self, item):
        x = item % 10

        for i in range(len(self.hashList[x])):
            print(self.hashList[x][i], end=', ')
            if self.hashList[x][i] == item:
                return True

        return False

    # remove element from hash list
    def remove_item(self, item):
        if Hashing.search(item):
            self.hashList.remove(item)
        else:
            print('Element not present in hash list')