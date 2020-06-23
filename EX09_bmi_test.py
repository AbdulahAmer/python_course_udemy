measure = input("Would you prefer metric or imperial measurements? ")


metric = "metric"
imperial = "imperial"



if measure == metric.lower():
    height = float(input("What is the height of the subject in centimeters? "))
    weight = float(input("What is the weight of the subject in kilograms? "))
    bmi = (weight)/((height/100)**2)
    print("You have entered",str(height) + " centimeters and",str(weight)+" kilograms.")
    if bmi <= 18.5:
            print("BMI =",round(bmi,2))
            print("You are underweight.")
    elif (bmi <= 24.9) and (bmi > 18.5):
            print("BMI =",round(bmi,2))
            print("You are at a normal weight.")
    elif (bmi > 24.9) and (bmi <= 29.9):
            print("BMI =",round(bmi,2))
            print("You are overweight.")
    else:
            print("BMI =",round(bmi,2))
            print("You are obese.")
elif measure == imperial.lower():
    height = float(input("What is the height of the subject in inches? "))
    weight = float(input("What is the weight of the subject in pounds? "))
    bmi = ((weight)/((height)**2))*703
    print("You have entered",str(height) + " inches and",str(weight)+" pounds.")
    if bmi <= 18.5:
            print("BMI =",round(bmi,2))
            print("You are underweight.")
    elif (bmi <= 24.9) and (bmi > 18.5):
            print("BMI =",round(bmi,2))
            print("You are at a normal weight.")
    elif (bmi > 24.9) and (bmi <= 29.9):
            print("BMI =",bmi)
            print("You are overweight.")
    else:
            print("BMI =",round(bmi,2))
            print("You are obese.")
else:
    print("Unknown entry. Please try again")
    
    
