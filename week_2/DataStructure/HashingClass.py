class Hashing:
    def __init__(self):
        self.hashList = []
        i = 0
        while i < 10:
            self.hashList.append([])
            i += 1
# we consider capacity of hash table 10
    def addData(self,n):
        if n not in self.hashList[n%10]:
            self.hashList[n%10].append(n)
# create search function to find element 
    def search(self, item):
        x = item%10
        for i in range(len(self.hashList[x])):
            print(self.hashList[x][i],end=', ')
            if(self.hashList[x][i] == item):
                return True
        return False

obj = Hashing()
f = open("Number.txt","r")
data = f.read()
f.close()
num = ''
for i in data:
    if i == ' ':
        obj.addData(int(num))
        num=''
    else:
        num = num + i
for i in range(len(obj.hashList)):
    print(obj.hashList[i])
print('Enter the number to search!  ')
num = int(input())
print(obj.search(num))
f = open("Number.txt","a")
f.write('\n\n')
for i in range(len(obj.hashList)):
    for j in range(20):
        f.write(str(obj.hashList[i][j]))
        f.write(' ')
    f.write('\n')


    
