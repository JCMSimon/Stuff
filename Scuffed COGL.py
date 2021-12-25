# This may display weirdly due to emoji stuff. 
#Also as the name says its kinda scuffed and cluttered 
import time
from os import system
import random
import threading
class COGL:
	def __init__(self):
		self.xd = int(input("X: "))
		self.yd = int(input("Y: "))
		self.makeGrid()
		self.timeout = 0.250
		Gameloop = threading.Thread(target=self.printGrid)
		Gameloop.setDaemon(True)
		Input = threading.Thread(target=self.getInput)
		self.Thing = 2
		system("cls")
		Input.start()
		Gameloop.start()

	def getInput(self):
		while True:
			Command = input().split()
			if len(Command) > 0:
				if Command[0] == "set":
					try:
						xPos = int(Command[1])
						yPos = int(Command[2])
						state = bool(Command[3])
					except ValueError:
						self.Thing += 1
						pass
					except IndexError:
						self.Thing += 1
						pass
					else:
						if state:
							self.Grid[yPos - 1][xPos - 1] = "⬜"
							self.Thing += 1
						elif not state:
							self.Grid[yPos - 1][xPos - 1] = "⬛"
							self.Thing += 1
						else: 
							self.Thing += 1
							pass
			else:
				self.Thing += 1

	
	def makeGrid(self):
		self.states = "⬛","⬜" 
		self.Grid = [[random.choice(self.states) for x in range(0,self.xd)] for y in range(0,self.yd)]
		#for x in range(self.xd):
		#	for y in range(self.yd):
		#		self.Grid[y][x] == random.choice(self.states)

	def printGrid(self):
		print("\033[?25l")
		while True:
			self.parseGrid()
			print("\033[F"*(self.yd+self.Thing))
			text = ""
			for Row in self.Grid:
				text = text + "".join(Row) + "\n"
			print(text)
				#print("".join(Row))
			#~16 fps
			#time.sleep(0.06)
		
			#~60 fps
			#time.sleep(0.016)
		
			#~why fps
			#time.sleep(0.0016)

			#5 fps
			time.sleep(0.250)
			
			
			#time.sleep(self.timeout)

	def parseGrid(self):
		self.CellScore = 0
		for x in range(self.xd):
			for y in range(self.yd):
				try:
					if self.Grid[y - 1][x - 1] == "⬜":
						self.CellScore +=1
				except IndexError:
					pass
				try:
					if self.Grid[y + 1][x + 1] == "⬜":
						self.CellScore +=1
				except IndexError:
					pass
				try:
					if self.Grid[y + 1][x - 1] == "⬜":
						self.CellScore +=1
				except IndexError:
					pass
				try:
					if self.Grid[y - 1][x + 1] == "⬜":
						self.CellScore +=1
				except IndexError:
					pass
				try:
					if self.Grid[y][x - 1] == "⬜":
						self.CellScore +=1
				except IndexError:
					pass
				try:
					if self.Grid[y][x + 1] == "⬜":
						self.CellScore +=1
				except IndexError:
					pass
				try:
					if self.Grid[y + 1][x] == "⬜":
						self.CellScore +=1
				except IndexError:
					pass
				try:
					if self.Grid[y - 1][x] == "⬜":
						self.CellScore +=1
				except IndexError:
					pass

#The Mistake im doing here is that im going cell by cell instead of assigning a Score first,and than changing states. But you know what? idc kekw

				if self.CellScore < 2 and self.Grid[y][x] == "⬜":
					self.Grid[y][x] = "⬛"
				if self.CellScore > 3 and self.Grid[y][x] == "⬜":
					self.Grid[y][x] = "⬛"
				if self.CellScore == 3 and self.Grid[y][x] == "⬛":
					self.Grid[y][x] = "⬜"
				self.CellScore = 0

if __name__ == '__main__':
	Test = COGL()









