import random

import pandas as pd

students = ['Nandini','Ranveer','Anvi','Rajveer','Arya','Aradhya']

score_dict={name:random.randint(1,100) for name in students}

passed_students ={key:value for key,value in score_dict.items() if  value > 65}

# print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence.split()
words_dict = {word:len(word) for word in words_list}

# print(words_dict)

def temp_to_Fahrenheit(temp_c):
    return (temp_c * 9/5) + 32

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

Fahrenheit_dict ={key:temp_to_Fahrenheit(value) for key,value in weather_c.items()}
print(Fahrenheit_dict)

