#!/usr/bin/env python

"""Run this script to have your mac speak out the steps of a seven minute workout"""

#Hi, I'm John

import sys, os
import time
import subprocess

voices = ['Daniel','Samantha']


# commands given to subprocess have to be a list of each keyword
# you don't include any spaces.
# example_command = ['say', '-v', 'Karen', 'Hello']
# subprocess.call(example_command)
# this will send the command to the terminal just as if you had typed:
# > say -v 'Karen' 'Hello'

# to use the timer for say, 10 seconds, do:
# time.sleep(10)

def say(s):
	a = time.time()
	subprocess.call(['say','-v','Samantha',s])
	b = time.time()
	return b-a
	
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

exercises = ('jumping jacks','wall sit','pushups','crunches',
			'chair step-ups','squats','tricep dips','plank',
			'high kneed running in place','lunges','pushups with rotation',
			'side plank','stop')

for i in range(0,len(exercises)):
	workout(exercises[i],exercises[i+1])

