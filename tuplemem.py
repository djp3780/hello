# list are more occupied memory speace than tuple.
# programe implementation now:-
import sys

l = [1, 23, 4, 56, 4, 8, 5]
print("total occupied memory by the list=", sys.getsizeof(l))
t = (1, 2, 3, 4, 5, 6, 4)
print("total occupied memory by the tuple=", sys.getsizeof(t))
# list are more occupied memory speace than tuple.
a = ["anil", "shyam", "radha", "mohan", "sohan"]
print("how many occupied memory size by the list=", sys.getsizeof(a))
b = (1, 2, 4, 6, 5, "true", "ankush")
print("how many occupied memory size by the tuple=", sys.getsizeof(b))
