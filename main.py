# from math import pi,e
# fruits=["a","b","c","d"]
# # print(0,1,2,3,4,5,6,7,8,9,sep="  ")
# x="aabaac"
# y=9
# print("a" in x)
# s1="aabcc"
# s2="adcaa"
# c=0
# if(len(s1)<len(s2)):
#     for s in s1:
#         if(s in s2):
#           c+=1
# # print(c)
# else :
#         for s in s2:
#             if(s in s1):
#              c+=1
# print(c)

# a = [10, 20]
# b = a
# b += [30, 40]
# a=5
# b=a
# b+=5
# print(a)
# print(b)
# print(2 * 3 ** 3 * 4)
# x = 0
# for i in range(10):
#   for j in range(-1, -10, -1):
#     x += 1
#     print(type(("a","b")))
# fruit=["a","b"]
# fruits=["c","d"]
# #fruit.extend(fruits)
# name="hello"
# del name
# tup=("a","b")

# print(tup)
# def mul(n):
#     if(n<=1):
#         res=1
#     else:
#         res=n*mul(n-1)
#     return res


# print(mul(4))
# from typing import List


#code chief sum problem

# t=int(input())
# sum=0
# i=0
# n_list=[None] * t
# while t> 0 :
#     n_list[i]=input()
#     i+=1
#     t-=1
# for li in n_list:
#     j=0
#     listt=str(li)
#     while j<len(listt):
#         sum=sum+int(listt[j])
#         j+=1
#     print(sum)
#     sum=0
  
n=int(input())
j=0
sum=0
n_list=[None] * n
while n>0:
    n-=1
    n_list[j]=input()
    j+=1
for item in n_list:
    i_list=str(item).split(" ")
    for i in i_list:
        j=0
        sum=sum+int(i)
        j+=1
    print(sum)
    sum=0
    

