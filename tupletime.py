# list take more time to excute as compared to tuple
# programe implementation now:
import timeit

l = timeit.timeit(stmt="[1,2,34,6,5,6,7,8]", number=1000000)
print("list time to excute of code=", l)
r = timeit.timeit(stmt="[1,1,2,34,6]", number=100000)
print("list time to excute of code=", r)
w = timeit.timeit(stmt="(1,2,34,6,7,9)", number=200000)
print("tuple time to excute of code=", w)
u = timeit.timeit(stmt="[1,2,3,4,5,7,8,4,6,8,7,4,6,4,7,9,8]", number=4000000)
print("list1 time to excute of code=", u)
t = timeit.timeit(stmt="(1,2,4,3,5,4,7,69,7)", number=5000000)
print("tuple1 time to excute of code=", t)
