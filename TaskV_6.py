N = int(input())
students = []
marks = 3
for _ in range(N):
    student = input().split()
    student[1:] = [int(i) for i in student[1:]]
    student.insert(0, -sum(student[1:]) / marks)
    students.append(student)
print('-' * 20)
students.sort()
for student in students:
    print(
        student[1],
        ' '.join(str(mark) for mark in student[2:]),
        f'{-student[0]:.2f}'
    )