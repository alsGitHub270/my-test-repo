import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not the other term'
print re.search('hello','hello world!')

for pattern in patterns:
    print 'Searching for "%s" in : \n"%s"' % (pattern,text)

    # Check for match
    if re.search(pattern, text):
        print '\n'
        print 'Match found. \n'
    else:
        print '\n'
        print 'No Match was found.\n'

print 'If match cannot be found, re.search returns None'
print re.search('h','w')

match = re.search(patterns[0],text)
print type(match)

print match.start()
print match.end()

print '\nSPLIT\n'
split_term = '@'
phrase = 'What is your email, is it hello@gmail.com?'
print re.split(split_term,phrase)
print 'hello world'.split()

print '\nFINDING ALL INSTANCES OF A PATTERN\n'
print re.findall('match','Here is one match, here is another match')

print 'USING META CHARACTERS'


def multi_re_find(pattern1s,phrase1):
    '''
        Takes in a list of regex patterns
        Prints a list of all matches
    '''

    for pattern in pattern1s:
        print 'Searching the phrase using the re check: %r' % pattern
        print re.findall(pattern,phrase1)
        print '\n'


print '\nREPETITION\n'
'''
Repetition Syntax

There are five ways to express repetition in a pattern:
1.) A pattern followed by the metacharacter * is repeated zero or more times.
2.) Replace the * with + and the pattern must appear at least once.
3.) Using ? means the pattern appears zero or one time.
4.) For a specific number of occurrences, use {m} after the pattern, where m is replaced with the number of times
         the pattern should repeat.
5.) Use {m,n} where m is the minimum number of repetitions and n is the maximum. Leaving out n ({m,}) means the
        value appears at least m times, with no maximum.
'''
test_phrase = 'sdsd..sssddd...sdddsdddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)

print '\nCHARACTER SETS\n'
'''
Character Sets
Used when you wish to match any one of a group of characters at a point in the input.  Brackets are used to
construct character set inputs.  For example:  the input [ab] searches for occurrences of either a or b.
'''

test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns,test_phrase)

print '\nEXCLUSIONS\n'
'''
We can use ^ to exclude terms by incorporating it into the bracket syntax notation.  For example:
[^...] will match any single character not in the brackets.
'''
test_phrase = 'This is a string!  But it has punctuation.  How can we remove it?'
'''
Use [^!.? ] to check for matches that arae not a !, ., ?, or a space.  Add the  + to check that the
match appears at least once, this basicaly translates into finding the words.
'''
print re.findall('[^!.? ]+',test_phrase)

print '\nCHARACTER RANGES\n'
test_phrase = 'This is an example sentence. Lets see if we can find some letters.\n'

print test_phrase

test_patterns = ['[a-z]+',  # sequences of lower case letters
                 '[A-Z]+',  # sequences of upper case letters
                 '[a-zA-Z]+',  # sequences of lower or upper case letters
                 '[A-Z][a-z]+']  # one upper case letter followed by lower case letters

multi_re_find(test_patterns, test_phrase)

print '\nESCAPE CODES\n'
'''
Escape Codes

You can use special escape codes to find specific types of patterns in your data, such as digits,
non-digits,whitespace, and more. For example:

Code Meaning

\d a digit
\D a non-digit
\s whitespace (tab, space, newline, etc.)
\S non-whitespace
\w alphanumeric
\W non-alphanumeric

Escapes are indicated by prefixing the character with a backslash (). Unfortunately, a backslash must
itself be escaped in normal Python strings, and that results in expressions that are difficult to read.
Using raw strings, created by prefixing the literal value with r, for creating regular expressions
eliminates this problem and maintains readability.
'''
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns = [ r'\d+',     # sequence of digits
                r'\D+',     # sequence of non-digits
                r'\s+',     # sequence of whitespace
                r'\S+',     # sequence of non-whitespace
                r'\w+',     # alphanumeric characters
                r'\W+',     # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)
