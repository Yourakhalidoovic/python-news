numbers = [1, 2, 3, 4, 5]
evens = list(filter(, numbers))
print(evens)
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda num: num % 2 == 0, numbers))
print(evens)
=========================
words = ['hello', 'world']
uppercase_words = list(map(lambda x: x.upper(), words))
print(uppercase_words)