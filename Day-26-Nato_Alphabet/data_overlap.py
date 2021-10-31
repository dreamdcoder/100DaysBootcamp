import pandas as pd

with open("file1.txt") as f1:
    f1_list = f1.readlines()
    f1_list = [int(number.strip()) for number in f1_list]

with open("file2.txt") as f2:
    f2_list = f2.readlines()
    f2_list = [int(number.strip()) for number in f2_list]


result = [number for number in f2_list if number in f1_list]
print(f"f1:{f1_list}")
print(f"f2:{f2_list}")
print(f"result{result}")