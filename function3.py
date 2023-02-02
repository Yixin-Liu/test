#coding=utf-8

def sum(*numbers):
    total=0.0
    for number in numbers:
        total += number
    return total
print(sum(1,2,3,4))
print(sum(6,6,6,6,6,6,6))
        
