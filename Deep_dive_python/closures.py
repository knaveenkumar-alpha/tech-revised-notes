def adder(n):
    def inner(k):
        return k + n 
    return inner


f1 = adder(1)
f2 = adder(2)
f3 = adder(3)
# print(f1, f2, f3)
f1(10)
f2(20)
f3(30)
print(f1, f2, f3)
