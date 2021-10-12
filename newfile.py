def calcstuff(menge,kosten,menge2):
	x = kosten / menge * menge2
	print(f"Result: {x}")

if __name__ == "__main__":
	while True:
		try:	
			mengei = float(input("Menge "))
			kosteni = float(input("kosten "))
			menge2i = float(input("menge2 "))
		except ValueError:
			print("Smth went wrong")
			print(" ")
		else:
			calcstuff(mengei,kosteni,menge2i)