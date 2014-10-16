import numpy
import copy

class Digit(object):
	MAX_ROWS = 3
	MAX_COLS = 3
	GLIF_VALUES = {" " : 0, "|" : 1, "_" : 2}
	ZERO  = numpy.matrix([[0,2,0], [1,0,1], [1,2,1]])
	ONE   = numpy.matrix([[0,0,0], [1,0,0], [1,0,0]])
	ONE_ALT   = numpy.matrix([[0,0,0], [0,0,1], [0,0,1]])
	TWO   = numpy.matrix([[0,2,0], [0,2,1], [1,2,0]])
	THREE = numpy.matrix([[0,2,0], [0,2,1], [0,2,1]])
	FOUR  = numpy.matrix([[0,0,0], [1,2,1], [0,0,1]])
	FIVE  = numpy.matrix([[0,2,0], [1,2,0], [0,2,1]])
	SIX   = numpy.matrix([[0,2,0], [1,2,0], [1,2,1]])
	SEVEN = numpy.matrix([[0,2,0], [0,0,1], [0,0,1]])
	EIGHT = numpy.matrix([[0,2,0], [1,2,1], [1,2,1]])
	NINE  = numpy.matrix([[0,2,0], [1,2,1], [0,2,1]])

	def __init__(self):
		self.pre_matrix = [[5,5,5], [5, 5,5], [5,5,5]]
		self.matrix = None
		self.curr_pos = (0 ,0)
		self.digit_value = None
		return

	def _inc_pos(self):
		if self.curr_pos[1] == self.MAX_COLS - 1:
			newX = self.curr_pos[0] + 1
			newY = 0
		else:
			newX = self.curr_pos[0]
			newY = self.curr_pos[1] + 1
		self.curr_pos = (newX, newY)
		return

	def add_glif(self, glif):
		if self.curr_pos[0] >= self.MAX_ROWS :
			raise IndexError("Digit's Matrix Coordiate Max Reached pos[0] " \
				+ str(self.curr_pos[0]) + " " + str(self.matrix))
		if self.curr_pos[1] >= self.MAX_COLS:
			raise IndexError("Digit's Matrix Coordiate Max Reached pos[1] " \
				+ str(self.curr_pos[1]))
		glif_value = self.GLIF_VALUES.get(glif)
		if glif_value == None:
			raise KeyError("Provided Glif has no Know Value")	
		self.pre_matrix[self.curr_pos[0]][self.curr_pos[1]] = glif_value
		self._inc_pos()
		return

	def determine_int_val(self):
		self.matrix = numpy.matrix(self.pre_matrix)
		self.determinate = numpy.linalg.det(self.matrix)
		value = None
		if (self.matrix == self.ZERO).all():
			value = 0
		elif (self.matrix == self.ONE).all() or (self.matrix == self.ONE_ALT).all():
			value = 1
		elif (self.matrix == self.TWO).all():
			value = 2
		elif (self.matrix == self.THREE).all():
			value = 3
		elif (self.matrix == self.FOUR).all():
			value = 4
		elif (self.matrix == self.FIVE).all():
			value = 5
		elif (self.matrix == self.SIX).all():
			value = 6
		elif (self.matrix == self.SEVEN).all():
			value = 7
		elif (self.matrix == self.EIGHT).all():
			value = 8
		elif (self.matrix == self.NINE).all():
			value = 9
		self.digit_value = value
		return value


class AccountNumber(object):
	LENGTH = 9

	def __init__(self):
		self.digits = self.init_digits()
		return

	def init_digits(self, digit_count = 9):
		digits = []
		digit_end = digit_count 
		for i in range(0, digit_end):
			digits.append(Digit())
		return digits

	def insert_digit(self, pos, digit):
		self.digits[pos] = copy.deepcopy(digit)
		return

	def set_digits(self, digits):
		self.digits = copy.deepcopy(digits)

	def check_broken_digits(self):
		broken = False
		if "?" in str(self):
			broken = True
		return broken

	def checksum(self):
		#((1*d1) + (2*d2) + ... + (9*d9)) mod 11 == 0
		return (((1 * self.digits[8].digit_value) + \
				(2 * self.digits[7].digit_value) + \
				(3 * self.digits[6].digit_value) + \
				(4 * self.digits[5].digit_value) + \
				(5 * self.digits[4].digit_value) + \
				(6 * self.digits[3].digit_value) + \
				(7 * self.digits[2].digit_value) + \
				(8 * self.digits[1].digit_value) + \
				(9 * self.digits[0].digit_value)) % 11 == 0 )
		#return True


	def validation_output(self):
		output = str(self)
		if self.check_broken_digits():
			output += " ILL"
		elif not self.checksum():
			output += " ERR"
		return output

	def __str__(self):
		out_string = ""
		for digit in self.digits:
			int_val = digit.determine_int_val()
			if int_val is not None:
				#out_string += (str(digit.determine_int_val()))
				out_string += (str(digit.digit_value))
			else:
				out_string += "?"
		return out_string



def init_digits(digit_count = 9):
	digits = []
	digit_end = digit_count 
	for i in range(0, digit_end):
		digits.append(Digit())
	return digits


if __name__ == "__main__":

	FILE_PATH = "AccountNumbers.txt"

	account_numbers = []

	digits = init_digits()

	with open(FILE_PATH) as in_file:
		for line_number, line in enumerate(in_file, start=1):
			for pos, glif in enumerate(line, start=1):
				#if pos == 1  and glif == "\n":
				if line_number % 4 == 0:
					account_number = AccountNumber()
					account_number.set_digits(digits)
					account_numbers.append(account_number)
					digits = init_digits()
					continue
				if pos >= 1 and pos <= 3:
					digit_index = 0
				elif pos >= 4 and pos <= 6:
					digit_index = 1
				elif pos >= 7 and pos <= 9:
					digit_index = 2
				elif pos >= 10 and pos <= 12:
					digit_index = 3
				elif pos >= 13 and pos <= 15:
					digit_index = 4
				elif pos >= 16 and pos <= 18:
					digit_index = 5
				elif pos >= 19 and pos <= 21:
					digit_index = 6
				elif pos >= 22 and pos <= 24:
					digit_index = 7
				elif pos >= 25 and pos <= 27:
					digit_index = 8
				elif pos >= 28 and glif is not "\n":
					continue
				try:
					digits[digit_index].add_glif(glif)
				except:
						print ("pos : " + str(pos) + " line_number: " + str(line_number) + " digit_index: " + str(digit_index))

	for account_number in account_numbers:
		#print account_number
		print account_number.validation_output()

	print "Done"
