#coding = utf-8

def sum(*numbers):
    totle = 0.0
    for number in numbers:
        totle += number
    
    return totle

print(sum(22,33,44))
print(sum(1,2,3,4,5,6,7,8,9))