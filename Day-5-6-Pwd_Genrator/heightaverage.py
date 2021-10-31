
student_heights = map(int,input("Input a list of student heights. ").split())

total_height = 0
count  = 0
for i in student_heights:
    total_height += i
    count += 1

average_height = round(total_height/count)
print(f"Average height of students is {average_height}")
