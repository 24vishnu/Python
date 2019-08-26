import BubbleSortBl as ob
with open("demo.txt") as f:
	data = f.read()
	ob.BSortingLogic(data)
f.close()