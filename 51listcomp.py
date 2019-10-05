file = open('grades.txt')
grades = file.readline()
print(grades)
for i in range(len(grades)):
    grades[i] = grades[i].rstrip()
print(grades)