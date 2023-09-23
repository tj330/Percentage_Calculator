sub = int(input("Enter the total number of subjects: "))
max_mark = int(input("Enter the maximum mark for an individual subject: "))
sum = 0

for i in range (0, sub):
    mark = int(input(f"Enter the mark you scored for subject {i+1}: "))
    sum += mark

total_mark = sub*max_mark
calc = int((sum/total_mark) * 100) 
print(f"Your percentage is {calc}")
