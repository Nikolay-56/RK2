"""Задание 2"""
array = []
NUMBER = "1"

file = open("stdin.txt","r")

while NUMBER != "stop":
    for line in file:
        NUMBER = line
        array.append(NUMBER)
        array.sort()
file.close()

del array[-1]
array = [int(x) for x in array]

sum = array [0] + array [1]
sum = str(sum)

file = open("stdout.txt","w")
file.write(sum)
file.close()





