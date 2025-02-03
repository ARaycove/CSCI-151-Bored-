import stdio
import sys
import practice_programs.hello_world
import practice_programs.practice_sum
import practice_programs.three_name

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

# Takes a variable amount of names from the command line and prints a greeting
if False:
    practice_programs.three_name.print_input_names()

# Adds two number
if True:
    practice_programs.practice_sum.print_sum() 