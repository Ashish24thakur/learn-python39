# how to initialize a string
a = ''  # empty String using string format
a = str()  # empty string using string class constructor
print(a)  # output:- ''


# method
# capitalize() capitalize the first letter
st = 'hello world'
re = st.capitalize()
print(re, type(re))  # output Hello world <class str>

# title()
st = 'hello 1g world'
re = st.title()
print(re, type(re))  # Output Hello 1G World

# upper()  work on ascii string
st = 'hello world 123@'
re = st.upper()
print(re)  # Output HELLO WORLD 123@

# lower() work on ascii string
st = 'Hello World 123@'
re = st.lower()
print(re)  # Output hello world 123@

# casefold() convert all alphabet into lower case (work on unicode string)
st = 'Hello World'
re = st.casefold()
print(re)  # Output hello world


# split()  split the string with given pattern and return the list of items
# example 1
st = 'hello world programming'
re = st.split(' ')
print(re, type(re))  # ['hello', 'world', 'programming'] <class 'list'>

# example 2
st = 'hello    pyth\ton progra\nmming'
re = st.split()  # default split pattern 'whitespace'
print(re)  # ['hello', 'pyth', 'on', 'progra', 'mming']


# centre
st = 'hello python'
re = st.center(100, '*')
print(re)

# count count the substring in a string
st = 'hello python'
re = st.count('hello')
print(re)

# encode : encode the string with given base

st = 'hello 😒 world 🔯😌'
re = st.encode(encoding='utf')
print(re)



# endswith
st = 'hello world'
re = st[:5].endswith('o')
print(re, type(re))  # output True <class 'bool'>

# find return index of searched item return -1 if item not found
st = 'hello world'
re = st.find('world')
print(re, type(re))  # output True <class 'bool'>











# split in user input
ls = input('enter the space sep data').split()
ls1 = list(map(int , ls))
print('after color', ls1)
print('sum of element', sum(ls1))


# use of eval

k = 'print("hello")'
eval(k)
print(k, type(k))

a = 'hello'
hello = 'a'
x = eval('hello')
l = eval(x)
print(eval(l))



k = eval(input())  # [3, 4, 32]
print(k)





a = eval(input())
print(a, type(a))





# slicing in sting
hs = 'hello world'

# k = hs[0]  # indexing
k = hs[2:5]  # range [2, 3, 4]
print(k)  # output llo

hs = 'hello world'
k = hs[-3:-1]  # range [-3, -2]
print(k)  # output  rl

k = hs[-10:-1]
print(k)  # output hello worl

hs = 'hello world'
k = hs[-3:]
print(k)  # output rld

# step size in negative
hs = 'hello world'
k = hs[5:1:-1]  # range [5, 4, 3, 2]
print(k)  # output  oll







