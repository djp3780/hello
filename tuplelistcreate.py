# once tuple is create then you can not change it because tuple is immutable or unchangeable
# but there is another way to create to achive this you can convert tuple to list
# programe imlemenmation:
x = ["ankush", "ankit", "anky", "ntitin"]
print(type(x))
x[1] = "yogesh"
y = tuple(x)
print(y, type(y))
# once tuple is create then you can not value change and becaseu tuple is immutable or unchangeable
# but there is another way to create  to achive this you can convert list to tuple
a = ["ahish kumar", "rohit", "royal chanlenger", " ankit"]
print(type(a))
a[2] = "ankush"
b = tuple(a)
print(b, type(b))
