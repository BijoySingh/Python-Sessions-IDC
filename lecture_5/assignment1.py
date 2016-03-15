def getHighest(a, b, c, d):
    highest = a
    if b > highest:
        highest = b
    if c > highest:
        highest = c
    if d > highest:
        highest = d
    return highest

def hasPairs(a, b, c):
    if a == b or b == c or c == a:
        return True
    return False

def isVowel(a):
    small_a = a.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    return small_a in vowels

def numberOfVowels(name):
    count = 0
    for c in name:
        if isVowel(c):
            count += 1
    return count

def isPrime(n):
    if n == 1:
        return False

    for num in range(2, n):
        if n % num == 0:
            return False
    return True

def printsNumber(num):
    if num <= 10:
        print(num)
        printsNumber(num + 2)

printsNumber(2)