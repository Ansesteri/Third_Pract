N = int(input())
students = {}
marks = 3
for i in range(N):
    student = input().split()
    students[student[0]] = [int(i) for i in student[1:]]
    print(f'{student[0]} {sum(students[student[0]])/marks}0')