# https://projecteuler.net/problem=22
import os

names = []
with open(os.path.join(os.path.dirname(__file__), "0022_names.txt"), "r") as file:
    names = file.read().replace("\"","").split(",")

names.sort()
total = 0
for index,name in enumerate(names):
    value = 0
    for char in name:
        # if name == "COLIN":
        #     print(f"{name} {ord(char)-ord("A")+1}")
        value += ord(char)-ord("A")+1

    # if name == "COLIN":
    #     print(f"{name} {value} {index}")

    value *= index + 1

    # if name == "COLIN":
    #     print(f"{name} {value} {index}")
    total += value
print(total)