def calculate_tot(marks):
    return sum(marks)
def calculate_percentage(marks):
    return sum(marks)/len(marks)
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
