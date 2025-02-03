import stdio

stdio.write(f"First Assignment")
bob_salary = 20000
stdio.write(f"bob_salary:   {id(bob_salary)}\n")

stdio.write(f"Second Assignment\n")
tom_salary = 35000
stdio.write(f"bob_salary:   {id(bob_salary)}\n")
stdio.write(f"tom_salary:   {id(tom_salary)}\n")
stdio.write(f"Is Same Objects: {bob_salary is tom_salary}\n")

stdio.write(f"Bob gets a raise\n")
bob_salary = tom_salary
stdio.write(f"bob_salary:   {id(bob_salary)}\n")
stdio.write(f"tom_salary:   {id(tom_salary)}\n")
stdio.write(f"Is Same Objects: {bob_salary is tom_salary}\n")


stdio.write(f"Tom gets a raise\n")
tom_salary *= 1.2
stdio.write(f"bob_salary:   {id(bob_salary)}\n")
stdio.write(f"tom_salary:   {id(tom_salary)}\n")
stdio.write(f"Is Same Objects: {bob_salary is tom_salary}\n")

# This is total
total_salary = bob_salary + tom_salary
stdio.write(f"bob_salary:   {id(bob_salary)}\n")
stdio.write(f"tom_salary:   {id(tom_salary)}\n")
stdio.write(f"Is Same Objects: {bob_salary is tom_salary}\n")
stdio.write(f"total_salary: {id(total_salary)}\n")