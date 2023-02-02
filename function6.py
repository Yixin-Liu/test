#coding = utf-8

def f1(x):
    return x > 55

data1 = [21,341,44,4525, 53, 334, 343, 133]
filtered_data = filter(f1,data1)
data2 = list(filtered_data)
print(data2) 

def f2(x):
    return x * 2
data3 = [1,2,3,4,5,6,7,8,9]
mapped_data = map(f2,data3)
data4 = list(mapped_data)
print(data4)