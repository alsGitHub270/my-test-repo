'''
    List comprehension allows us to build out lists using a
    different notation.  Think of it as essentially a one line loop
    built inside brackets.
'''

l = []
for letter in 'word':
    l.append(letter)
print l

lst = [letter for letter in 'word']
print "\nusing list comprehension: ", lst

lst = [x**2 for x in range(0,11)]
print lst

# check for even numbers
lst = [number for number in range(11) if number % 2 == 0]
print '\nlist of even numbers in a range:  ', lst

print '\nconverts celcuis to farhrenheit'
celsius = [0,10,20,34.5, 44,100]
fahrenheit = [(temp * (9/5.0) + 32) for temp in celsius]
print fahrenheit

print '\nnested list comprehension'
lst = [x**2 for x in [x**2 for x in range(11)]]
print lst
