def arrayCheck(nums):
    for  i in range(len(nums)-2):
        if nums[i+1] == 2:
                if nums[i+2] == 3:
                    return True
    return False
x =  arrayCheck([1, 1, 2, 3, 1])
y = arrayCheck([1, 1, 2, 4, 1]) 
z = arrayCheck([1, 1, 2, 1, 2, 3])
print(x)
print(y)
print(z)

# PROBLEM 2                     
def stringBits(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i]
    return result

x = stringBits('Hello') 
print(x)
Y = stringBits('Hi') 
Z = stringBits('Heeololeo') 
print(Y)
print(Z)

# PROBLEM 3
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (b.endswith(a) or a.endswith(b))

x =  end_other('Hiabc', 'abc') 
y =  end_other('AbC', 'HiaBc') 
z =  end_other('abc', 'abXabc') 

print(x)
print(y)
print(z)

# PROBLEM 4

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(string):
    result = ""
    for i in  range(len(string)):
        result += string[i]
        result += string[i]
    return result

x = doubleChar('The') 
y = doubleChar('AAbb') 
z = doubleChar('Hi-There') 
print(y)
print(z)
print(x)   
   
# PROBLEM 5

# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    return a+b+c
x = no_teen_sum(1, 2, 3)
print(x)

# teen = 2, 13, 1
# def fix_teen(a,b,c):
#     if b == [13,14,17,18,19]:
#         return 0
    
#     return a+b+c
# y = fix_teen(2, 13, 1) 
# print(y)

a = 2
b = 13
c = 1
def fix_teen(n):
    if n >= 13 and n <= 19 and n != 15 and n != 16:
        return 0
    else:
        return n 
def no_teen_sum(a,b,c):
    return (fix_teen(a) + fix_teen(b) + fix_teen(c))

print(no_teen_sum(a, b, c))

# PROBLEM 6


# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    count = 0
    for element in nums:
        if element % 2 == 0:
            count += 1
    return count

x =  count_evens([2, 1, 2, 3, 4]) 

print(x)
y = count_evens([2, 2, 0]) 
print(y)

z =  count_evens([1, 3, 5]) 
print(z)




