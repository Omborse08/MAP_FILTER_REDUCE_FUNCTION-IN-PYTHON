from functools import reduce
def grades(x):
    if x >= 90:
        return "A"
    elif x >= 75:
        return "B"
    elif x >= 60:
        return "C"
    elif x >= 40:
        return "D"
    else:
        return "F"


marks = [45, 67, 89, 38, 90, 74, 50, 32]

num1 = list(map(grades,marks))
print(f"Students Grades: {num1}")

num2 = list(filter(lambda z: z > 40,marks))
print(f"Passed Students: {num2}")

num3 = reduce(lambda x, y: (x + y),num2)
m = num3 / len(num2)
print(f"Total Avg Is: {m:.2f} ")