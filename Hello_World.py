# my comment
print "Hello World"

x = 5
if x > 5:
    print " x is greater"
elif x == 5:
    print "equal"
else:
    print "Less than"

print "\nexample of going deep into combo dictionary and list"

print "\nget hello\n"

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print d
print d['k1'][0]['nest_key'][1][0]

d = {'k1': [1, 2, {'k2': ['this is tricky', {'toughie': [1, 2, ['hello']]}]}]}
print d
print d['k1'][2]['k2'][1]['toughie'][2][0]

print '\nPrinting even numbers from a list[1,2,3,4,5]'
_list = [1, 2, 3, 4, 5]
for num in _list:
    if num % 2 == 0:
        print 'Even number {0!r:s}'.format(num)

print 'sum of the list'
list_sum = 0
for num in _list:
    list_sum += num
print list_sum

s = 'this is a string'
for letter in s:
    print letter

print '\nTuple Unpacking'
l = [(2, 4), (6, 8), (10, 12)]
for tup in l:
    print tup

for (t1, t2) in l:
    print t1

print '\niterate thru dictionary'
d = {'k1': 1, 'k2': 2, 'k3': 3}
for k,v in d.iteritems():  # python 3 for k,v in d.items():
    print k
    print v

print '\nWhile statements'
x = 0
while x < 5:
    print 'x is currently: ', x
    x += 1
else:
    print "Else statement reached, x is finally ", x

print "\nbreak, continue and pass"
x = 0
while x < 10:
    print 'x is currently: ', x
    print 'x is still less than 10, adding 1 to x'
    x += 1

    if x == 3:
        print ' Hey x equals 3!'
        break
    else:
        print 'continuing.....'
        continue

print '\nRange'
start = 5
stop = 20
print range(start, stop)

start = 0
step = 2
print range(start, stop, step)

# python 2 requires a generator(xrange()) for large lists or for loops.
# python 3 has range() as a generator.
# use xrange to generate a range consisting of a very large number of elements

x = range(1, 6)
print x
print 'Type of x', type(x)
print "Using xrange"
x = xrange(1, 6)
print x
print 'Did not save in memory, no output.  Type of x', type(x)
print 'printing x casting xrange as a list'
print list(x)

print '\nList Comprehensions\n'

print 'using for loop'
l = []
for letter in 'word':
    l.append(letter)
print l
print 'list comprehension'
l = [letter for letter in 'word']
print "l = [letter for letter in 'word']"
print l

lst = [x**2 for x in range(0, 11)]
print "lst = [x**2 for x in range(0, 11)]"
print lst

print 'nested list'
lst = [x**2 for x in [x**2 for x in range(0, 11)]]
print lst

lst = [number for number in range(11) if number % 2 == 0]
print 'lst = [number for number in range(11) if number % 2 == 0]'
print lst

celsius = [0, 10, 20.1, 34.5, 44, 100]
fahrenheit = [(temp * (9/5.0) + 32) for temp in celsius]
print '\nfahrenheit = [(temp * (9/5.0) + 32) for temp in celsius]'
print 'celsius:  ', celsius
print 'fahrenheit:  ', fahrenheit

print '\n\n Unit 5 test'

print "\nUse for, split() and if to create a Statement that will print out letters starting with 's'"
st = 'print only the words that start with s in this sentence.'
words = st.split(' ')
for word in words:
    if word[0] == 's':
        print word

print '\nUse range() to print all the even numbers from 0 to 10'
print range(0, 11, 2)

print '\nUse List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.'
lst = [number for number in range(1,51) if number % 3 == 0]
print lst

st = '\nPrint every word in the sentence that has an even number of letters'
print '\n', st
words = st.split(' ')
for word in words:
    if len(word) % 2 == 0:
        print 'even'

print 'FizzBuzz'
myArray = range(1, 101)
print myArray
for value in myArray:
    if value % 3 == 0 and value % 5 == 0:
        print 'FizzBuzz'
    elif value % 3 == 0:
        print 'Fizz'
    elif value % 5 == 0:
        print 'Buzz'
    else:
        print value

print '\n Using List comprehension'
st = 'Create a list of the first letters of every word in this string'
results = []
print st
results = [word[0] for word in st.split( )]
print results

