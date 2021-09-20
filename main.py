from typing import List


s1='abacef'
s2='abcd'
list1=list(s1)
list2=list(s2)
index=0
while index<len(list1)-1:
    if(list1[index]==list1[index+1]):
        list1.remove(list1[index+1])
    index=+1

print(list1)
# list1.remove(list1[3])
# print(list1)


