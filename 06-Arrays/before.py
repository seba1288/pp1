import math
import random
import array as np

arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
arr = np.array('i',(4,0,3))
arra2 = np.array('i',[i for i in range(1,51)])
arra3 = np.array('i',[i for i in range(1,31)])
arra4 = np.array('i',[random.randrange(0,2) for i in range(1,21)])
arra5 = np.array('l',[[False for i in range(1,6)] for j in range(1,3)])
#	an array with values: 4,0,3
#50-element array filled with zeros
#	an array with integer values in the range of <1,30>
#	20-element array filled with 0 or 1 randomly
#	two dimensional array with five rows and two columns filled with False

print(arra4)