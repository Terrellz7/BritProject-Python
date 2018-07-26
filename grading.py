count = 0
grades = []
letNumGrades = []
while int(count) < 5:
    print("Enter grade", count+1, ":")
    grades.append(int(input()))
    count += 1

pos = 1
for i in grades:
    if(i < 0) or (i > 100):
        letNumGrades.append([grades[pos-1], "Invalid Value"])
    elif(i >= 80) and (i <= 100):
        letNumGrades.append([grades[pos-1], "A"])
    elif(i >= 50) and (i < 80):
        letNumGrades.append([grades[pos-1], "B"])
    else:
        letNumGrades.append([grades[pos-1], "F"])
    pos += 1

print(letNumGrades)

