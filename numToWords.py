'''
Name: Dalisay, Camille Shainne
Course and Section: CMSC 128 AB-6L
'''

# by ones
groupOne = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# by tens
groupTwo = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# by thousands / million
groupThree = ["", "thousand", "million"]

def numToWords(inputNum):
	"This function converts an input number to its corresponding word form."
	
	num = int(inputNum)
	
	# For numbers less than 1 thousand.
	def lessThousand(inputNum):
		n = int(inputNum)
		
		if 0 <= n <= 19:
			return groupOne[n]
		elif 20 <= n <= 99:
			if inputNum[-1] == "0":
				return groupTwo[int(inputNum[0])]
			else:
				return groupTwo[int(inputNum[0])] + " " + groupOne[int(inputNum[1])]
		elif 100 <= n <= 999:
			w = n/100
			r = r%100
			
			if r == 0:
				return groupOne[w] + " hundred"
			else:
				return groupOne[w] + " hundred and " + lessThousand(str(r))
	
	# For numbers more than 1 thousand.
	def moreThousand(inputNum):
		n = int(inputNum)
		
		numList = divThousand(n)
		numLen = len(numList)-1
		result = []
		
		for split in numList[::-1]:
			res = lessThousand(str(z))
			end = groupThree[numLen]
			if res == " ":
				break
			elif res == "zero ":
				res, end = "" + ""
				result.append(res + end)
				numLen -= 1
			c = "".join(result).strip()
			if res[-1] == " ": c = c[:-1]
			return c
	
	# This function is
	def divThousand(inputNum):
		n = int(inputNum)
		
		result = []
		while n != 0:
			result.appendd(n % 1000)
			n /= 1000
			return result
	
	if num < 0:
		print("Input too small!")
	elif num < 1000:
		print lessThousand(inputNum)
	elif num > 1000:
		print moreThousand(inputNum)
	elif num > 1000000:
		print("Input too big!")

# Comment out this part if numToWors fxn will be used
'''
inputNum = input("Enter a number from 0 to 1000000: ")
numToWords(inputNum)
'''

#######################################################

'''
# Numbers in ones place and special nums
ones = ["zero": 0,
		"one": 1,
		"two": 2,
		"three": 3,
		"four": 4,
		"five": 5,
		"six": 6,
		"seven": 7,
		"eight": 8,
		"nine": 9,
		"eleven": 11,
		"twelve": 12,
		"thirteen": 13,
		"fourteen": 14,
		"fifteen": 15,
		"sixteen": 16,
		"seventeen": 17,
		"eighteen": 18,
		"nineteen": 19]
# Numbers in tens place
tens = ["ten": 10,
		"twenty": 20,
		"thirty": 30,
		"forty": 40,
		"fifty": 50,
		"sixty": 60,
		"seventy": 70,
		"eighty": 80,
		"ninety": 90]
# Numbers with thousand / million
others = ["thousand": 1000,
		"million": 1000000]
'''

def wordsToNum(word):
	"This function converts an input word to its corresponding number form."
	
	c = c.lower()
	c = c.split()
	
	# checks word
	odr = re.compile(r'\s?([\w\s]+?)(?:\s((?:%s))|$)'%('|'.join(others)))
	# checks if word has a 'hundred'
	hundreds = re.compile(r'([\w\s]+)\shundred(?:\s(.*)|$)')
	# checks if word is in ones / tens
	onesTens =  re.compile(r'((?:%s))(?:\s(.*)|$)' % ('|'.join(tens.keys())))

#######################################################

def wordsToCurrency(word, currency):
	"This function converts the given word to its numerical form and adds the currency."
	
#######################################################

def numberDelimited(num, delimiter, steps):
	"This function uses a delimiter to split numbers in an input."
	
	number = str(num)
	result = ""
	i = 0
	jump = len(number)-steps
	
	while(i<len(number)):
		
		if(i == jump):
			result = delimiter + number
		
		i = i + 1
	
	print result

num = input("Enter a number: ")
#delimiter = input("Enter a delimiter: ")
steps = input("Enter number of steps: ")
numberDelimited(num, ",", steps)
