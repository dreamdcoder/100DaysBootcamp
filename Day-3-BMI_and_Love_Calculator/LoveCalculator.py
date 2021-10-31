name1 = input("Enter your name ").upper()
name2 = input("Enter your Crush's/Partner's name ").upper()

combined_name = name1 + name2

t_count = 0
l_count = 0
for i in combined_name:
    if "TRUE".__contains__(i):
        t_count += 1
    if "LOVE".__contains__(i):
        l_count += 1

score = int(str(t_count) + str(l_count))

print(f"Your score is {score}", end='')

if score < 10 or score > 90:
    print(", you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(", you are alright together.")
else :
    print(".")
