student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key, value in student_grades.items():
    print(key)
    print(value)
    if value > 90 and value <= 100:
        student_grades[key] = "Outstanding"
    elif value > 80 and value <= 90:
        student_grades[key] = "Exceeds Expectations" 
    elif value > 70 and value <= 80:
        student_grades[key] = "Acceptable" 