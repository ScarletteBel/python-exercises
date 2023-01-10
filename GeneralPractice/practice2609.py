
array = [2, 3, 4, 6678, 12]
print(f'Array: {array}')

numbers = array
numbers1 = array.copy()
numbers1[3] = 90 
print(f'Array1: {numbers1}')
print(f'Numbers: {numbers}')

numbers[2]=3
print(f'Numbers edited: {numbers}')

print(f'Array: {array}')

g = 45
h = g

print(g)
print(h)

h = 78

print(g)
print(h)


