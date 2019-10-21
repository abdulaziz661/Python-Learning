s = 'django'
print(s[0])
print(s[-1])
print(s[0:4])
print(s[1:4])
print(s[4:])

#problem 2
l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print(l)

#problem 3
d1 = {'simple_key':'hello'}
print(d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1])

#problem 4
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
x = set(mylist)
print(x)


#problem 5
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
x = "my dog's name is Sammy"
print("Hello" + ' ' + (x) + ' ' + "and he is 4 years old")