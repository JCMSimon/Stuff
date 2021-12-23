# 10 x 10 Grid
import time
from os import system
import random

class COGL:
	def __init__(self):
		self.xd = int(input("X: "))
		self.yd = int(input("Y: "))
		self.makeGrid()
		self.printGrid()

	def makeGrid(self):
		self.states = " ","#"
		self.Grid = [[random.choice(self.states) for x in range(0,self.xd)] for y in range(0,self.yd)]
		#for x in range(self.xd):
		#	for y in range(self.yd):
		#		self.Grid[y][x] == random.choice(self.states)

	def printGrid(self):
		while True:
			self.parseGrid()

			system("cls")
			for Row in self.Grid:
				print("".join(Row))
			#~16 fps
			#time.sleep(0.06)
			
			#~60 fps
			#time.sleep(0.016)
			
			#~why fps
			#time.sleep(0.0016)

			#5 fps
			time.sleep(0.250)

	def parseGrid(self):
		self.CellScore = 0
		for x in range(self.xd):
			for y in range(self.yd):
				try:
					if self.Grid[y - 1][x - 1] == "#":
						self.CellScore +=1
				except IndexError:
					self.Grid[y][x] = " "
				try:
					if self.Grid[y + 1][x + 1] == "#":
						self.CellScore +=1
				except IndexError:
					self.Grid[y][x] = " "
				try:
					if self.Grid[y + 1][x - 1] == "#":
						self.CellScore +=1
				except IndexError:
					self.Grid[y][x] = " "
				try:
					if self.Grid[y - 1][x + 1] == "#":
						self.CellScore +=1
				except IndexError:
					self.Grid[y][x] = " "
				try:
					if self.Grid[y][x - 1] == "#":
						self.CellScore +=1
				except IndexError:
					self.Grid[y][x] = " "
				try:
					if self.Grid[y][x + 1] == "#":
						self.CellScore +=1
				except IndexError:
					self.Grid[y][x] = " "
				try:
					if self.Grid[y + 1][x] == "#":
						self.CellScore +=1
				except IndexError:
					self.Grid[y][x] = " "
				try:
					if self.Grid[y - 1][x] == "#":
						self.CellScore +=1
				except IndexError:
					self.Grid[y][x] = " "
				if self.CellScore < 2 and self.Grid[y][x] == "#":
					self.Grid[y][x] = " "
				if self.CellScore > 3 and self.Grid[y][x] == "#":
					self.Grid[y][x] = " "
				if self.CellScore == 3 and self.Grid[y][x] == " ":
					self.Grid[y][x] = "#"
				self.CellScore = 0

if __name__ == '__main__':
	Test = COGL()









