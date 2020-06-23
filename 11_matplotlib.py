import matplotlib.pyplot as plt

#this will import the plotting function of matplotlib

#creating variables to graph

x = [1,2,3,4,5,6]
y = [12,23,34,45,56,67]

#plt.plot(x,y) #this compiles the x and y axis to show a graph

# I commented the above out so I didnt have to see it all the time


#plt.show() # this presents the grpah to be shown

x_tick = ['June','July','August','September','October','November'] #makes a list to be used as ticks

plt.xticks(x,x_tick) #applies the above list to the x-axis

#plt.plot(x,y) #puts it all together


#if you comment out the plt.show part between two different plots they are combined
# into one graph ------- interesting



#plt.show() #shows it to us

plt.bar(x,y) #applies a new type of graph to the project

plt.ylabel("Stuff on the y-axis") #puts a label on the graph but not 

plt.title("Other stuff up top")



plt.show() #shows the graph above
