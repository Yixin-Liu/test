#coding=utf-8
def makecoffee(name="cappuccino"):
    return "制作一杯{0}咖啡".format(name)

coffee1 = makecoffee("latte")
coffee2 = makecoffee()

print(coffee1)
print(coffee2)