data_valid = False

while data_valid == False:
    total_classes = (input("Type the number of total classes: "))
    try:
        total_classes = int(total_classes)
    except:
        print("Invalid input. Whole numbers only.")
        continue
    if total_classes <= 0 or total_classes > 20:
        print("The total number of classes has to be between 1 and 20.")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    absences = (input("Type the number of absences: "))
    try:
        absences = int(absences)
    except:
        print("Invalid input. Whole numbers only.")
        continue
    if absences < 0 or absences > total_classes:
        print("The total number of absences can't be less than 0 or greater than the total number of classes.")
        continue
    else:
        data_valid = True


data_valid = False

while data_valid == False:
    grade1 = (input("Type the grade of the first test: "))
    try:
        grade1 = float(grade1)
    except:
        print("Invalid input. Numbers only. Decimals as a dot only.")
        continue
    
    if grade1 < 0 or grade1 > 10:
        print("Grades should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = (input("Type the grade of the second test: "))
    try:
        grade2 = float(grade2)
    except:
        print("Invalid input. Numbers only. Decimals as a dot only.")
        continue
    if grade2 < 0 or grade2 > 10:
        print("Grades should be between 0 and 10")
        continue
    else:
        data_valid = True
    


avg_grade = (grade1+grade2)/2
attendance = (total_classes - absences)/total_classes




if avg_grade >=6 and (attendance >= 0.8):
        print("The student was approved with an average score of",str(avg_grade),"and an attendance rate of",str(100*(attendance)),"% for the year")
elif avg_grade < 6 and attendance < 0.8:
        print("The student has failed due an average grade lower than 6.0 and an attendance rate lower than 80%.")
elif attendance >= 0.8:
    print("The student has failed due to an average grade lower than 6.0.")
else:
    print("The student has failed due an attendance rate lower than 80%.")
