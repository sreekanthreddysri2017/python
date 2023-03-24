from collections import namedtuple

n, Student, total = int(input()), namedtuple("Student", input().split()), 0

for _ in range(n):
    student = Student._make(input().split())
    total += int(student.MARKS)

print(total / n)