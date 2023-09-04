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

#