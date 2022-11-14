"""Задание 1"""
array = []
NUMBER = "1"
print("(please enter stop if you want to get a result)")

while NUMBER != "stop":
    NUMBER = input()
    array.append(NUMBER)
    
    

del array[-1]
array = [int(x) for x in array]
array.sort()

sum = array [0] + array [1]
print(sum)





