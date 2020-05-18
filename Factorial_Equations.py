
'''
You are given two numbers  and . Your task is to find the last digit of the following equation: 

Input format

The first line contains two integers  and .

Output format

Print the last digit of the given equation.

Constraints


SAMPLE INPUT 
5 2
SAMPLE OUTPUT 
5
Explanation
factorial of (2) is 2*1=2  ,So 5^2=25 the last digit in 25 is 5
'''

import math
value = list(map(int,input().split(' ')))
index = value[0]%10
Value2 = [0,1,4,9,6,5,6,9,4,1]
Value4 = [0,1,6,1,6,5,6,1,6,1]
#print(values[0]**(math.factorial(values[1])%10)%10)
if(value[0]==0):
    print(1)
elif(value[1]>4):
    print(1)
elif(value[1]==4):
    print(Value4[index])
elif(value[1]==3 or value[1]==2):
    print(Value2[index])
elif(value[1]==1 or value[1]==0):
    print(index)
