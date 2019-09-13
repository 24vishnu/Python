# ---------------------------------- prg-----------------------------------------------
# BST.py
# date : 26/08/2019
# calculate number of BST can perform using N number of nodes


class BST:

    @staticmethod
    def fact(n):

        if n < 2:
            return 1

        pro = 1

        for i in range(1, n + 1, 1):
            pro = pro * i

        return pro


# Method to calculate number of BST
def calculate(n):
    print(BST.fact(2 * n) // (BST.fact(n + 1) * BST.fact(n)) % 100000007)
