import re

poem = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

url = 'http://localhost/hello/Chris?query=regular%20expression'

print poem

# .
p = re.compile(r'.*')
r = p.findall(poem)
print r

print '#' * 30

# ^
p = re.compile(r'^http')
r = p.findall(url)
print r

print '#' * 30

# $
p = re.compile(r'end$')
r = p.findall(url)
print r

print '#' * 30

# *
p = re.compile(r'\w*$')
r = p.findall(url)
print r

print '#' * 30

# +
p = re.compile(r'/hello/\w+')
r = p.findall(url)
print r

print '#' * 30

# \b
p = re.compile(r'\b\w{6}\b')
r = p.findall(poem)
print len(r)
print r

print '#' * 30

# []
p = re.compile(r'[aeiouAEIOU]')
r = p.findall(poem)
print r

print '#' * 30

# |
p = re.compile(r'the|than|this')
r = p.findall(poem)
print r

print '#' * 30

# () this says grab me the name in here
p = re.compile(r'/hello/(?P<name>\w+)')
r = p.findall(url)
print r

print '#' * 30