#!/usr/bin/env python

"""Run this script to have your mac speak out the steps of a 15 minute workout"""

import sys, os
import time
import subprocess

# Selected voices to choose from
voices = ['Daniel','Samantha']

# Define function that speaks the input and accounts for the time it takes to do so
def say(s):
	a = time.time()
	subprocess.call(['say','-v','Samantha',s])
	b = time.time()
	return b-a

# Define function that speaks each exercise and the one following it, along with time remaining
# Last time through the loop has slightly altered text
# t enables accounting for time taken to speak text
# Each exercise is done for one minute
def workout(name1,name2):
	t = say('Begin %s' % name1)
	time.sleep(15)
	t = say('45 seconds to go')
	time.sleep(15-t)
	t = say('30 seconds')
	time.sleep(15-t)
	t = say('15 seconds')
	time.sleep(5-t)
	if name2 == 'stop':
		t = say('10 seconds.')
	else:
		t = say('10 seconds. %s coming up next.' % name2)
	time.sleep(5-t)
	t = say('5')
	time.sleep(1-t)
	t = say('4')
	time.sleep(1-t)
	t = say('3')
	time.sleep(1-t)
	t = say('2')
	time.sleep(1-t)
	t = say('1')
	time.sleep(1-t)
	if name2 != 'stop':
		t = say('Begin 10 second rest')
		time.sleep(5-t)
		t = say('5')
		time.sleep(1-t)
		t = say('4')
		time.sleep(1-t)
		t = say('3')
		time.sleep(1-t)
		t = say('2')
		time.sleep(1-t)
		t = say('1')
		time.sleep(1-t)
	else:
		t = say('Workout complete. Good job!')

# Define tuple of exercises ('stop' listed at end to enable alternate speech during last exercise)
exercises = ('jumping jacks','wall sit','pushups','crunches',
		'chair step-ups','squats','tricep dips','plank',
		'high kneed running in place','lunges','pushups with rotation',
		'side plank','stop')

# Run workout function for each exercise, inputting current and next exercise
for i in range(0,len(exercises)):
	workout(exercises[i],exercises[i+1])

