#!/usr/bin/python
#/usr/bin/env python
#
import math
random.seed()

#
#This script will do channel selection based on interference. It approximates a
#Nash equilibrium via simulated annealing. It will always find an good approximation to 
#a Nash equilibrium in polynomial time, but it probably won't achieve Pareto optimality
#very often.


n = 5 #Number of users. Eventually will get this from base station via number_users()
max = 4 #Number of channels available. Eventually will get this from base station via get_channels()
z = [0] * n #This will hold the channel assignment solution
T = 100 #Initial temperature. 100 was chosen emperically.
i = 0
iterations = 12 #A formula for getting this number should be derived emperically
total_interference = 2 #Interference of all users. Eventually will get this from clients via get_interference()

while (i < iterations):
	c = random.randrange(1,max) #pick a random channel that's open
	u = random.randrange(1,n) #pick a random user
	change_channel(u, c) #assign that channel to that user (change_channel() not implemented yet)
	new_total_interference = get_interference() #get_interference() not implemented yet
	delta_I = total_interference - new_total_interference
	if (delta_I > 0):
		z = current_channel_assignment() #not implemented yet
		total_interference = new_total_interference
	else
		p = rand(1,0)
		if (p < exp(-(delta_I)/T)):
			z = current_channel_assignment
			total_interference = new_total_interference
	T = T*0.8 #Decrease temperature. 0.8 was chosen emperically.
	i = i + 1
print z

