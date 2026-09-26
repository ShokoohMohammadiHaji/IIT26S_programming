print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")
minute_task_1 = int(input("A1_T1: "))
minute_task_2 = int(input("A1_T2: "))
minute_task_3 = int(input("A1_T3: "))
minute_task_4 = int(input("A1_T4: "))
minute_task_5 = int(input("A1_T5: "))
minute_task_6 = int(input("A1_T6: "))
minute_task_7 = int(input("A1_T7: "))
spent_time = (minute_task_1 + minute_task_2 + minute_task_3
              + minute_task_4 + minute_task_5 + minute_task_6 + minute_task_7)
print(f"\nIn total you spent {spent_time} minutes on programming.")
average_time = spent_time / 7
print(f"Average per task was {average_time:.2f} min and same rounded to the nearest integer {round(average_time)} min.") 