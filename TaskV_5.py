N = int(input())
students = {}
marks = 3
output = []
for _ in range(N):
    student = input().split()
    last_name = ""
    students[student[0]] = [int(i) for i in student[1:]]
    avg_mark = sum(students[student[0]]) / marks
    output.append('%s %.2f' % (last_name, avg_mark))
print('-' * 20)
print(''.join(output))