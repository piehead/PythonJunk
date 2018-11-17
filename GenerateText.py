# GenerateText.py
import random
import datetime
now = datetime.datetime.now()

while True:
	try:
		charlen = int(input("Please enter the length you desire: "))
		break
	except:
		print("Invalid input. Please try again.")
charstr = ""
count = 0
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", \
		"T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", \
		"s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8" ,"9", "0", "!", "?"]

		
while count < charlen:
	ran = random.randrange(len(alphabet))
	charstr += alphabet[ran]
	count += 1
	
file = open("Text.txt", "a+")
file.write("<%d-%d-%d | %d-%d-%d>:\t" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
file.write(charstr)
file.write("\n")

file.close()