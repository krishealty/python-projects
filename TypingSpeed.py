from time import *
import random as r

  
  



def mistake(partest, usertest):
	error = 0
	for i in range(len(partest)):
		try:
			if partest[i] != usertest[i]:
				error = error + 1
		except:
				error = error + 1 	
		return error

def speed_time(time_e, time_s, userinput):
	time_delay = time_e - time_s
	time_R = round(time_delay, 2) 
	speed = len(userinput)/ time_R
	return round(speed)

test = ['Hi, this typing speed program is made by Krish Lalwani and it can calculate your typing speed untill 150 words.' , 'Just type what your are told to write and also this program is without GUI and hence is easily usable.']

test1 = r.choice(test)

print('		******Typing Speed calculator******\n') 
print(test1)
print()
time_1 = time()
testinput = input('Enter:  ') 
time_2 = time()

print ('Speed:  ', speed_time(time_1, time_2, testinput), ' Words per second.')
print('Errors: ', mistake(test1, testinput))



