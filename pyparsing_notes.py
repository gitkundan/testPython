"""
pyparsing has lot of combination classes of words and alphabets e.g. alphanums, for parsing html use make_html_tags
resources:
https://rephrase.net/days/07/pyparsing
https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/pyparsing-presentation.html
https://pythonfix.com/code/pyparsing/internals/
https://scipy-cookbook.readthedocs.io/items/Reading_Custom_Text_Files_with_Pyparsing.html

steps:
(a) define the language grammar using BNF
(b) create stubs of phrases using pyparsing classes e.g. Word,WordEnd,WordStart,Literal,OneOrMore,oneOf
    each of these are called as parseElement 
    exclude certain characters like this : salutation=Word(alphanums+'!',exclude_chars='!')
    suppress punctuations/delimiters in resulting text : grammar=hello.suppress()+salutation will only grab things after hello word



(c) parse and create a parse object by replacing (a) with (b)

(d) post parsing it will be stored as list; rather than calling the list elements by index call by name:
>>> article = Word(printables).setResultsName("the_article")
>>> grammar = Literal("Hello,").suppress() + article
>>> results = grammar.parseString("Hello, nurse!")

Now, given this, you can do two things: you can either refer to the result as an element of a list,
>>> print results[0]
nurse!

or by name:
>>> print results.the_article
nurse!

by that the building blocks of the grammar can also be the name of the list index result

(e) Optional keyword 
>>> adjective = Word(printables).setResultsName('adjective')
>>> grammar = salutation + Optional(adjective) + article + StringEnd()

(f) feed std python expressions using [like pandas.apply()]
to remove exclamation at end of string:

>>> def remove_exclamation(x):
...    return x[0].rstrip('!')
>>> article = Word(printables)
>>> article = article.setParseAction(remove_exclamation)
>>> print article.parseString("nurse!")
['nurse']

(g) skip intermediate words to get to text of interest using SkipTo

>>> annoying = 
... SOMETHING
... SOMETHING ELSE
... END
... MORE STUFF THAT MATTERS
... 

>>> from pyparsing import SkipTo
>>> end_marker = SkipTo("END", include=True).suppress()
>>> (end_marker + "MORE STUFF THAT MATTERS").parseString(annoying)
(['MORE STUFF THAT MATTERS'], {})

(h) regex matches:
>>> from pyparsing import Regex
>>> hex_num = Regex("[0-9a-fA-F]+")
>>> hex_num.parseString("1f")
(['1f'], {})

(i) Multiple matches:
>>> hex_num = Regex("[0-9a-fA-F]+")
>>> from pyparsing import OneOrMore
>>> multiple = OneOrMore(hex_num)
>>> multiple.parseString('1f')
(['1f'], {})
>>> multiple.parseString('1f 2f 3f')
(['1f', '2f', '3f'], {})

(j) Parse actions:
Parse actions are functions that are run on parsed tokens; 
generally, the result of the parse action replaces the parsed token. 
For example,
>>> def convert_hex(x):
...   return eval('0x' + x[0])
>>> hex_num = hex_num.setParseAction(convert_hex).setResultsName('num')
>>> result = hex_num.parseString('1f')
>>> print result.num
31

As you can see, this sort of parse function allows you to convert parse results into objects
automagically (after all, there's no reason that convert_hex needs to return an integer;
it could return an object of any type).

(k) Whitespace: unlike regex whitespace is automatically ignored
(l) code comments ignored: 
Imagine trying to match a function in which the developer had
inserted a comment to document each parameter in the argument list. With
pyparsing, this is accomplished with the code:
cFunction = Word(alphas)+ "(" + \
Group( Optional(delimitedList(Word(nums)|Word(alphas))) ) + ")"
cFunction.ignore( cStyleComment )

(j) stats.dump() to be used for debugging
print (stats.dump())

(k) give the individual parse result name
schoolAndScore =
Group( schoolName("school") +
score("score") )
gameResult = date("date") +
schoolAndScore("team1") +
schoolAndScore("team2")

in the above use schoolName("school")  or schoolName.setResultsName("team1")

(l) end your grammar with stringEnd

    data="AAA AA AAA BA AAA"
    word=Word('AB')
    grammar=OneOrMore(word)+StringEnd()
    result=grammar.parseString(data)

    print(result)

Make sure there is no dangling input text by ending your grammar with
stringEnd, or by appending stringEnd to the grammar used to call parse
String. If the grammar does not match all of the given input text, it will raise
a ParseException at the point where the parser stopped parsing

To check whether your grammar has processed the entire string, pyparsing pro-
vides a class StringEnd (and a built-in expression stringEnd) that you can add to
the end of the grammar. This is your way of signifying, "at this point, I expect there
to be no more text—this should be the end of the input string." If the grammar
has left some part of the input unparsed, then StringEnd will raise a ParseE
xception. Note that if there is trailing whitespace, pyparsing will automatically skip
over it before testing for end-of-string.

(m) parseString vs scanString:
scanString is another parsing method that is especially useful when testing gram-
mar fragments. While parseString works only with a complete grammar, begin-
ning with the start of the input string and working until the grammar is completely
matched, scanString scans through the input text, looking for bits of the text that
match the grammar. Also, scanString is a generator function, which means it will
return tokens as they are found rather than parsing all of the input text, so your
program begins to report matching tokens right away. 



"""

from pyparsing import *
# identifier=Word(alphas,alphanums+'_') # defines programming variable starting with alphabets and then alphanumerics
# number=Word(nums+".")
# assignmentExpr=identifier + "=" + (identifier|number) #will catch pi=3.14

# assignmentTokens=assignmentExpr.parseString('pi=.14159')
# print (assignmentTokens) #=> ['pi', '=', '3.14159']

# Example 2 : Hello world
"""
Hello, World!
Hi, Mom!
Good morning, Miss Crabtree!
Yo, Adrian!
Whattup, G?
How's it goin', Dude?
Hey, Jude!
Goodbye, Mr. Chips!
"""

"""
BNF : 
greeting ::= salutation comma greetee endpunc
salutation ::= word+
comma ::= ,
greetee ::= word+
word ::= a collection of one or more characters, which are any alpha or ' or .  
endpunc ::= ! | ?
"""

#create pyparsing stubs
word=Word(alphas+"'.")
salutation=OneOrMore(word)
comma=Literal(',')
greetee=OneOrMore(word)
endpunc=oneOf('! ?')
greeting=salutation+comma+greetee+endpunc #constructor of the pattern


data="Hello, World!"
# for i in data:
#     results=greeting.parseString(i)
#     salutation=[]
#     for token in results:
#         if token ==',':break
#         print(salutation)
#         salutation.append(token)

#alternative
word=Word(alphas+"'.")
salutation=Group(OneOrMore(word)) #Group is similar to regex ()
greetee=Group(OneOrMore(word)) #Group is similar to regex ()



salutation,dummy,greete,endpunc=greeting.parseString(data)
print(type(salutation))
