import pandas as pd
from enum import Enum

FILE_PATH = "scores.csv"

GPA_OUTPUT = "{:.2f}"
AVERAGE_GPA_OUTPUT = "\nThe class GPA is {:5,.2f}"

class Grade(Enum):
    A = 4
    B = 3
    C = 2
    D = 1
    F = 0

def letter_from_grade(grade):
    if grade >= 90:
        return Grade.A
    elif grade >= 80:
        return Grade.B
    elif grade >= 70:
        return Grade.C
    elif grade >= 60:
        return Grade.D
    else:
        return Grade.F

def task2():
    csv_file = pd.read_csv(FILE_PATH, header=0, index_col=0)
    df = pd.DataFrame(csv_file)

    grades_map = df.applymap(lambda score: letter_from_grade(score).value)
    students_means = grades_map.mean()
    class_mean = students_means.mean()

    outputable_students_means = students_means.map(GPA_OUTPUT.format)

    print(outputable_students_means.to_string())
    print(AVERAGE_GPA_OUTPUT.format(class_mean))

task2()
