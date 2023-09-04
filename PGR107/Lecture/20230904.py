import pandas as pd

#1.3 function with array

a= [1,2,3]
b= [1,2]


def passing_value(b):
    #append 100 from b=[1,2] => b=[1,2,100]
    b.append(100)

    #reset only this function inside
    b=[2]
    print("function", b)

print(a) # [1,2,3]
print(b) # [1,2] 
passing_value(a) #using function based on a, #[1,2,100]
print(a) # [1,2,3, 100]
print(b) # [1,2]


# function with loop
a = [1, 2, 3, 4, 5]
new_list = []

for elem in a:
    elem = elem + 1
    print(elem)
    new_list.append(elem)

print(new_list)

# function with multi dementional data
a = [1, 2, 3, 4, 5]
b = [elem + 1 for elem in a]
print(b)


# use ;
a = 1; b =2
print('+', a + b)
print('-', a - b)
print('*', a * b)
print('/', a / b)
print('//', a // b)
print('**', a ** b)
print('&', a & b)
print('|', a | b)
print('^', a ^ b)


# use if
x = 5

if x < 0:
    print("negative")
elif x == 0:
    print("zero")
elif 0 < x < 5:
    print("positive but smaller than 5")
else:
    print("positive and larger than or equal to 5")


#1. data structure and sequences
#tuple
#list
#dict
#set

#2. functions
#namespaces, scope and local functions
#returning multiple values
#lambda functions

#tuple
tuples = (4,5,6),(7,8)
print(tuples[0])
print(tuples[1][1])



#tuple practice 1
nest = ((7,8), 9),(1, 2)
print("nest",nest[0][0][1])


#a simply initialize
t1 = tuple([1,2,3])
print(t1)
t2 = (1,2,3)
print(t2)

#practice 2
t1 == t2

#practice 3
# print(len(t1))
# t1.append(4)
# print('new length is ', len(t1))


#practice 4
