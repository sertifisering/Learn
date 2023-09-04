
##No submission practice case
#TUPLE 1
#practice 1-1
result = []
a = ("apple", "banana", "peach", "melon", "kiwi")
b = (1, 2, 3, 4, 5)
 
# S1
# result.append(a[slice(1, 3)])

# S2
result.append(a[1:3])
print(result)


## pratice 1-2
#==================================================
# S1
# def sum_num(numbers):
#     result = 0
#     for each in b:
#         result += each
#     return result

# def main():
#     b = (1,2,3,4,5)
#     result = sum_num(b)
#     print("sum", result)

# if __name__ == "__main__":
#     main()

# S2
#print("sum", sum(b))

# S3
result = 0
for each in b:
    result += each
print("sum", result)


## practice 1-3
# S1
# c = a + b
# print("tuple", c)

# S2
# c = tuple(a) + tuple(b)
# print("tuple", c)

# S3
c = tuple(a + b)
print("tuple", c)


## practice 1-4
# S1
# d = list(a) + list(b)

# S2
d = list(a + b)
print("list", d)

## practice 1-5
# S1
e = dict(zip(a, b))
print("dict", e)


#LIST 2
#practice 2-1
str_1 = ['Thank']
str_1.append("you")
print(str_1)

#practice 2-2
str_2 = ['Thank', 'you', 'much']
str_2.insert(2, 'so')
print(str_2)

#practice 2-3
str_3 = ['Thank', 'you', 'so', 'very', 'much']
str_3.remove('very')
print(str_3)