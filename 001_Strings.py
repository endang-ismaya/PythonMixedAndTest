# ------------------------------------
# String index
# ------------------------------------
# String:   a p p l e
# Index :   0 1 2 3 4

a = 'apple'[0]
e = 'apple'[-1]
fruit = 'apple'
first_character = fruit[0]
print(a)
print(e)
print(fruit)
print(first_character)

# ------------------------------------
# String length
# ------------------------------------
fruit = 'apple'
print(len(fruit))

# ------------------------------------
# Upper & Lower
# ------------------------------------
fruit = 'orange'
print(fruit.upper())
print(fruit.lower())

# ------------------------------------
# String concatenation
# ------------------------------------
print('I ' + 'love ' + 'Python.')
print('I' + 'love' + 'Python')

# ------------------------------------
# String concatenation using variable
# ------------------------------------
first = 'I'
second = 'love'
third = 'Python'
sentence = first + ' ' + second + ' ' + third + '.'
print(sentence)

# ------------------------------------
# Repeating Strings
# ------------------------------------
print('-' * 20)
happiness = 'happy ' * 3
print(happiness)

# ------------------------------------
# Casting number to string with str()
# ------------------------------------
version = 3
print('I love Python ' + str(version) + ".")

# ------------------------------------
# Formatting Strings
# ------------------------------------
print('I {} Python.'.format('love'))
print('{} {} {}'.format('I', 'love', 'Python'))

print('I {0} {1}. {1} {0}s me.'.format('love', 'Python'))

print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8}'.format('Apple', 3))
print('{0:8} | {1:8}'.format('Orange', 10))

# with left alignment
print('{0:8} | {1:<8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:<8}'.format('Apple', 3))
print('{0:8} | {1:<8}'.format('Orange', 10))

# floating
print('{0:8} | {1:<8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:<8.2f}'.format('Apple', 2.33333))
print('{0:8} | {1:<8.2f}'.format('Orange', 10))

