numbers = range(1, 11)
it = iter(numbers)
print(next(it))
import os
files = os.popen('dir *.py')
fileit = iter(files)
print(next(fileit))
print(next(fileit))

square = (10,8), (10,23), (25,23), (25,8)
for points in square:
    print(points)
squareit = iter(square)
print(next(squareit))
print(next(squareit))
print(next(squareit))
    