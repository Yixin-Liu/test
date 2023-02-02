#coding = utf-8

def cal(opr):
    if opr == '+':
        return lambda a,b: a+b
    else:
        return lambda a,b: a-b

f1 = cal('+')
f2 = cal('-')

print('5 + 8 = {0}'.format(f1(5,8)))
print('5 - 8 = {0}'.format(f2(5,8)))
