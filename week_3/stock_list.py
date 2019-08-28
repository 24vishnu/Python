import json

class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

class singleLinkedList:
    def __init__(self):
        self.head = None
        return
    
    def add_list(self, item):
        if not isinstance(item,LinkedList):
            item = LinkedList(item)                             
        if self.head is None:
            self.head = item
        else:   
            temp = self.head        
            while temp.next != None:
                temp = temp.next
            
            if temp.next == None:
                temp.next = item
        return
    
    def print_list(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def readFileData(self):
        with open('personal.json',"r") as file_obj:
            fileData = json.load(file_obj)
        return fileData
    
    def writeFile(self):
        with open('newFile.json',"w") as file_obj:
            temp = self.head
            while(temp != None):
                json.dump(temp.data,file_obj)
                temp = temp.next


obj = singleLinkedList()
daata = obj.readFileData()

for i in daata:
    obj.add_list(i)

obj.print_list()
obj.writeFile()