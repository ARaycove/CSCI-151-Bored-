import stdio
import sys

quizzes = 25/100
assignments = 35/100
exams = 40/100
total_grade = quizzes + assignments + exams

attendance_policy = "Attendance is expected, all classes must be attended"
assignments_per_week = 1.5 # 1 or 2 assignments per week
quizzes_grade_policy = "Lowest 4 quiz grade will be dropped"
late_work_policy = "There are no exceptions for making up quizzes"
all_policies = [attendance_policy,quizzes_grade_policy,late_work_policy]
all_policies = "\n".join(all_policies)

stdio.write(all_policies)
stdio.write("\n")