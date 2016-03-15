some_list = [1, 3, 'Hi']
print(some_list)

some_list.append('Yo')
some_list.append(32)
some_list.append('Yo')
print(some_list)

# remove the (i + 1)th element pop(i)
some_list.pop(2)
print(some_list)

# remove the element by it's value
some_list.remove('Yo')
print(some_list)

some_list.insert(2, 42)
print(some_list)

print(some_list[4])
print(some_list[1:3])
print(some_list[2:])
print(some_list[:3])

print(some_list.index('Yo'))
print(len(some_list))

for position in range(0, len(some_list)):
    print(some_list[position])

b = [] # Empty list (b = [1, 3, 5] is not empty, b = [], is empty)
for item in some_list:
    b.append(item)

def listOfEvens(start, stop):
    even_numbers = []
    for num in range(start, stop):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def removeFirstEven(some_list):
    for item in some_list:
        if item % 2 == 0:
            some_list.remove(item)
            break