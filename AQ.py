def digital_reduction(number):
	output = 0
	if number > 9:
		number_string = str(number)
		for numeral in number_string:
			output += int(numeral)
	else:
		output = number
	return output

def anglossic_qabbala(term):
	aq = 0
	for char in term:		
		add = gematria.get(char)
		aq += add
	return aq

gematria = {
	'0':0,
	'1':1,
	'2':2,
	'3':3,
	'4':4,
	'5':5,
	'6':6,
	'7':7,
	'8':8,
	'9':9,
	'A':10,
	'B':11,
	'C':12,
	'D':13,
	'E':14,
	'F':15,
	'G':16,
	'H':17,
	'I':18,
	'J':19,
	'K':20,
	'L':21,
	'M':22,
	'N':23,
	'O':24,
	'P':25,
	'Q':26,
	'R':27,
	'S':28,
	'T':29,
	'U':30,
	'V':31,
	'W':32,
	'X':33,
	'Y':34,
	'Z':35
}

done = False

while not done:

	alnum_term = False

	while not alnum_term:

		print("Enter alphanumeric term, or ! to quit")
		term = input()
		term = term.replace(' ','')
		term = term.upper()
		if term == "!":
			done = True						
		elif term.isalnum():
			alnum_term = True			
		else:
			print("Term must be alphanumeric")
			print()

	if not done:
		#AQ
		aq = anglossic_qabbala(term)
		print("AQ = " + str(aq))

		#DR
		dr = digital_reduction(aq)
		while len(str(dr)) > 1:
			dr = digital_reduction(dr)
		print("DR = " + str(dr))

		print()