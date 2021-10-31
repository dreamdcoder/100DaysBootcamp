
student_score = list(map(int,input("Input a list of student heights. ").split()))

max_index = 0

for i in range(1, len(student_score)):
    if student_score[max_index] < student_score[i]:
        max_index = i


print(f"Highest score is {student_score[max_index]}")
