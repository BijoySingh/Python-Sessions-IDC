def firstFive(name):
    return name[:5]

name = input('Enter Name')
print(firstFive(name))


def cube(num):
    return num * num * num


def easyCube(num):
    return num ** 3

print(cube(10))
print(easyCube(10))