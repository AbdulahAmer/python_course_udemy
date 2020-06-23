import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0
case_errors = 0

print("This will help you type faster. You have to type any word you want five times. Case does not matter.")
word = input("Please enter the word and prepare to begin: ")

while len(times) < 5:
    start = t.time()
    wd = input('Type the word: ')
    end = t.time()
    time_elapsed = end-start

    times.append(time_elapsed)

    if word.lower() != wd.lower():
        mistakes += 1
    elif (word != wd) and (word.lower() == wd.lower()): #this shows what happens when case sensitive
        case_errors +=1

print("You made", str(mistakes) + " mistake(s).")
print("You made", str(case_errors),"case error(s).")
print("Let's see your evolution")

data = {"Case Errors":case_errors,"Mistakes":mistakes}
t.sleep(3)

x = [1,2,3,4,5]
y = times

x_tick = ["1","2","3","4","5"]
plt.xticks(x,x_tick)
plt.ylabel("Time in seconds")
plt.xlabel("# of attempts")
plt.title("Your Typing Prowess.")

plt.plot(x,y)
plt.show()


# graph below shows what type and how many mistakes
y = x
y_tick = ["1","2","3","4","5"]
plt.bar(list(data.keys()),list(data.values()))
plt.yticks(y,y_tick)
plt.title("Amount of mistakes.")
plt.ylabel("Amount")
plt.xlabel("Different Types of Errors")
plt.show()
