# (2n!) / ((n+1)!*n!)
class BST:
    @staticmethod
    def fact(n):
        if n < 2:
            return 1
        pro = 1
        for i in range(1,n+1,1):
            pro = pro*i
        return pro


n = int(input())
print(BST.fact(2*n)//((BST.fact(n+1)*BST.fact(n)))%100000007)
