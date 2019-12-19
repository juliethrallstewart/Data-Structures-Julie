# 

a = [1,2,3,4,5,6,7,8,9,10,11]
def middle(arr):
    
    count = 0
    temp = 0
    for i in range(0,len(arr),2):
        print(i, "middle")
        temp = i - 2
    return temp

print(middle(a))
def middle2(arr):
    for i in arr:
        print(i, "middle 2")

middle2(a)
# How do you reverse a singly linked list without recursion? 
# You may not store the list, or it’s values, in another data structure.

l = [1, 2, 3, 4, 5]

for i in l:
    if i % 3 == 0:
        print(i)