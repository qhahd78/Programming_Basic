from math import pi
from collections import deque

# 의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")

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
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

# 5.1.2 Using Lists as Queues 
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft()) 
print(queue)

# 5.1.3 List Comprehensions 

squares = []
for x in range(10) : 
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]

print([(x,y) for x in [1,2,3] for y in [3,1,4] if x != y])

combs = []
for x in [1,2,3]: 
    for y in [3,1,4]: 
        if x != y : 
            combs.append((x,y))

print(combs)

vec = [-4, -2, 0, 2, 4] 
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
freshfruit = ['  banana','   loganberry', 'passion fruit   ']
print([weapon.strip() for weapon in freshfruit])
print([(x, x**2) for x in range(6)])
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
print([str(round(pi, i)) for i in range(1, 6)])

# 5.1.4. Nested List Comprehensions 

matrix = [
    [1,2,3,4], 
    [5,6,7,8,],
    [9,10,11,12],
]

print([[row[i] for row in matrix] for i in range(4)])
transposed = []
for i in range(4): 
    transposed.append([row[i] for row in matrix])

print(transposed)

transposed=[]
for i in range(4) : 
    transposed_row = []
    for row in matrix : 
        transposed_row.append(row[i])
    transposed_row.append(transposed_row)

print(transposed)

print(list(zip(*matrix)))