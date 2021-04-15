# 의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")

#3.1.3 Lists 
squares = [1, 4, 9, 16, 25] 
print(squares)

print(squares[0])
print(squares[-1])
print(squares[-3:])

print(squares[:])

print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125] 
print(4 ** 3)
cubes[3] = 64
print(cubes)

cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
#replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# now remove them
letters[2:5] = []
print(letters) 
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

letters = ['a', 'b', 'c', 'd']
print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3 ]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

# 5.1 More on Lists
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4)) # Find next banana starting a position 4 

fruits.reverse()
print(fruits) 

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())

# 5.1.1. Using Lists as Stacks
stack = [3, 4, 5]
stack.appned(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack.pop())
print(stack)
