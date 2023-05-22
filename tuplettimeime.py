import timeit

l = timeit.timeit(stmt="[1,2,3,4,6,5,78,7,8]", number=10000000)
print("time of list code of excution=", l)
t = timeit.timeit(stmt="(1,2,3,5,4,8,7,8)", number=1000000)
print("time of excute of the tuple=", t)
# list is take a more time to excute of code as comapre to tuple
