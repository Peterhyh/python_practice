import timeit

print(timeit.timeit("[x for x in range(1000000)]", number=1))
