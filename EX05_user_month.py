months = ("January","February","March","April","May","June","July","August","September ","October","November","December")
birthday = input("Using the format DD-MM-YYYY, what is the user's birthday?: ")
usermon = birthday[3:5]
print("You were born in " + months[int(usermon)-1] +".")
