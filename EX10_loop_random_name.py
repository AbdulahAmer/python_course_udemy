people = []
import random
while len(people) < 8:
    person = input("You do not yet have 8 names. Enter a name: ")
    people.append(person)
    print("That is", str(len(people)),"people.")

num = random.randint(0,8)
print("We have randomly chosen", people[num],"to be our lucky winner.")
