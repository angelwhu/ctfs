from turtle import *
import os
path = '';
for line in open('misc20.txt','r'):
	path += line
print len(path);
direction = {'d':0,'w':90,'a':180,'s':270}

def go():
	x = 0;
	reset();
	speed("fastest");
	for i in path :
		#print x 
		x = x + 1
		if x == (len(path) - 1) :
			break
		if i == 'e':
			if isdown() :
				up()
			else:
				down()
		else :
			setheading(direction[i]);
			forward(3)

if __name__ == '__main__':
	go();
	raw_input();
