import timeit

print "-".join(str(n) for n in range(100))
print timeit.timeit('"-".join(str(n) for n in range(100))',number=10000)

print '\nusing list comprehension'
print timeit.timeit('"-".join([str(n) for n in range(100)])',number=10000)

print '\nusing map'
print timeit.timeit('"-".join(map(str,range(100)))',number=10000)

print 'use in jupyter (magic function):   %timeit "-".join(str(n) for n in range(100))'
