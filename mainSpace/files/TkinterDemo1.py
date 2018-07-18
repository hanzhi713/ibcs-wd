from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import sys

#number of point
Number = 1024
#init frequency value
frequency = 1
#set the recur depth
sys.setrecursionlimit(1000000)

def draw_sin():
	'''raw a circle of sin'''
	#generate the time base
	t = np.arange(1,Number,1)
	#generate the signal
	y = np.sin(2*np.pi*frequency*t/Number)
	plt.plot(t,y)
	plt.grid(True)
	plt.text(900,0.75,'Frequency is '+str(frequency))
	plt.show()

def frequency_plus():
	'''function of add the frequency and plot the signal'''
	#notice:frequency is a global variable
	global frequency
	frequency = frequency + 1
	#clear a figure window
	plt.clf()
	draw_sin()

def my_button(root,label_text,button_text,button_func):
	'''function of creat label and button'''
	#label details
	label = Label(root)
	label['text'] = label_text
	label.pack()
	#label details
	button = Button(root)
	button['text'] = button_text
	button['command'] = button_func
	button.pack()

def main():
	'''main function'''
	root = Tk(className = 'DrawSin')
	#draw button function
	my_button(root,'Draw sin','click to Draw',draw_sin)
	#frequency plus function
	my_button(root,'Freq Plus','click to Plus',frequency_plus)
	root.mainloop()

if __name__ == "__main__":
	main()