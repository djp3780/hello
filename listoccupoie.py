# list is occupie more memeory space as comparer to the tuple
import sys

a = [1, 2, 3, 4, 5, 6, 7, 8]
print("size of the list=", sys.getsizeof(a))
b = (12, 34, 6, 46, 856, 898, 64, 64, 65)
print("size of the tuple=", sys.getsizeof(b))
# list is the occupie more memeory space as compare to the tuple
v = [10, 12, 13, 14, 15, 16, 14, 18, 19, 17, 18, 1, 1]
print("size of the list", sys.getsizeof(v))
m = (11, 22, 11, 22, 11, 33, 55, 44, 88, 99, 88, 66, 77)
print("size of tuple ", sys.getsizeof(m))
