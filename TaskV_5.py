from distutils.archive_util import make_archive


N = int(input())
students = {}
marks = 3
marks2 = [0] * marks

for _ in range(N):
    student = input().split()
    last_name = student[0]
    students[student[0]] = [int(i) for i in student[1:]]
    for i in range(marks):
        marks2[i] += students[last_name][i]

print('-' * 20)
avg_marks = (str('%.2f' % (marks2[i]/N)) for i in range(marks))
print(' '.join(avg_marks))