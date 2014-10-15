import numpy

class Digit(object):
	MAX_ROWS = 3
	MAX_COLS = 3
	GLIF_VALUES = {" " : 0, "|" : 1, "_" : 2}
	ZERO  = numpy.matrix([[0,2,0], [1,0,1], [1,2,1]])
	ONE   = numpy.matrix([[0,0,0], [1,0,0], [1,0,0]])
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
		print self.curr_pos
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
		print self.matrix
		print self.determinate
		if (self.matrix == self.ZERO).all():
			print 0
		elif (self.matrix == self.ONE).all():
			print 1
		elif (self.matrix == self.TWO).all():
			print 2
		elif (self.matrix == self.THREE).all():
			print 3
		elif (self.matrix == self.FOUR).all():
			print 4
		elif (self.matrix == self.FIVE).all():
			print 5
		elif (self.matrix == self.SIX).all():
			print 6
		elif (self.matrix == self.SEVEN).all():
			print 7
		elif (self.matrix == self.EIGHT).all():
			print 8
		elif (self.matrix == self.NINE).all():
			print 9

def init_digits(digit_count = 9):
	digits = []
	digit_end = digit_count 
	for i in range(0, digit_end):
		digits.append(Digit())
	return digits

if __name__ == "__main__":

	FILE_PATH = "AccountNumbers.txt"

	digits = init_digits()

	in_file = open(FILE_PATH)

	with open(FILE_PATH) as in_file:
		for line_number, line in enumerate(in_file, start=1):
			for pos, glif in enumerate(line, start=1):
				if pos == 1  and glif == "\n":
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

	for digit in digits:
		digit.determine_int_val()


	print "Done"
