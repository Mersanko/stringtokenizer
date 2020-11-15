import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class GUI():
	def __init__(self,title):
		self.title = title
		self.window =Tk()
		self.inputVar = StringVar()
		self.outputVar =  StringVar()

		self.window.geometry('600x350')
		self.window.title(self.title)

		self.inputLabel = Label(self.window,text="Input Arithmetic Expressions",font=('Arial',14,'bold'))
		self.inputLabel.place(x=175,y=50)

		self.inputEntry = Entry(self.window,textvariable=self.inputVar,width=40)
		self.inputEntry.place(x=190,y=80)

		self.outputLabel = Label(self.window,text="Output",font=('Arial',14,'bold'))
		self.outputLabel.place(x=280,y=150)

		self.outputEntry = Entry(self.window,textvariable=self.outputVar,width=40)
		self.outputEntry.place(x=190,y=180)

		#button for displaying the output 
		self.buttonLexemize = Button(self.window,text="Lexemize",command=self.lexemize,height=1,width=10,bg="green2")
		self.buttonLexemize.place(x=200, y=120)

		#button for clearing the input and output entry
		self.buttonClear = Button(self.window,text="Clear",command=self.clear,height=1,width=10,bg="turquoise1")
		self.buttonClear.place(x=350, y=120)

		#button for closing the window
		self.buttonClose = Button(self.window,text="Close",command=self.exit,height=1,width=10,bg="red")
		self.buttonClose.place(x=275, y=220)

		self.window.mainloop()

	def lexemize(self):
		
		expressions = self.inputEntry.get()

		#list for Operation, Parentheses and Brackets.
		symbols = ["+","-","*","/","(",")","[","]"] 
		newExpresion = "" 

		'''Scan every character of the input expression, if the character is in the symbols list it will concatenate
		a string containing space in the left side, symbol/operation in between and another space in the right side 
		to the newExpresion which is also a string. Otherwise the character will be directly concatenated to newExpresion.
		This method will help to easily split/tokenized the input string because you can use the space as separator 
		argument or delimiter of the python split function''' 
		for expression in expressions:
			if expression in symbols:
				newExpresion+=" "+expression+" "
				
			else:
				newExpresion+=expression

		#splitting the string and initialized a list from it.   
		tokenizedStringList = newExpresion.split(" ")

		#removing the blank element in the list
		while("" in tokenizedStringList):
			tokenizedStringList.remove("")


		result = "{}".format(tokenizedStringList)


		self.outputEntry.delete(0,END)

		#inserting the result to the output entry
		self.outputEntry.insert(0,result)

		

	def clear(self):
		#clear the input and output entry
		self.inputEntry.delete(0,END)
		self.outputEntry.delete(0,END)
		
		

	def exit(self):
		#close the window	
		quit()


gui = GUI("Lexemizer")
