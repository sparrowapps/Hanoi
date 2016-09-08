class Piece:
	def __init__ (self, size):
		self.size = size

	def __str__ (self):
		return (self.size * 2 - 1) * "="

	def __gt__ (self, piece):
		return self.size > piece.size

	def __lt__ (self, piece):
		return self.size < piece.size

class Tower:
	def __init__ (self, height, pieces):
		self.height = height
		self.pieces = [Piece(i) for i in range(1, pieces + 1)]

	def __str__ (self):
		""" Return a string representation of the tower where the tower exists of | that are replaced by the string representation of a piece if there is a piece on that place in the tower. """
		halfwidth = self.height - 1
		stringtower = halfwidth * " " + "|" + halfwidth * " " + "\n"

		# Fill in with | if there is no piece
		for i in range(0, self.height - len(self.pieces)):
			stringtower += halfwidth * " " + "|" + halfwidth * " " + "\n"

		# Now add the string representations of the pieces
		for piece in self.pieces:
			stringpiece = str(piece)
			whitespace = halfwidth - int((len(stringpiece) - 1) / 2)
			stringtower += whitespace * " " + stringpiece + whitespace * " " + "\n"

		return stringtower
			
	def add_piece (self, piece):
		""" Add a piece to the tower only if the added piece is smaller than the top most piece """
		if len(self.pieces) == 0 or self.pieces[0] > piece:
			self.pieces.insert(0, piece)
			return True
		return False

	def remove_piece (self):
		""" Remove the top most piece of the tower"""
		if len(self.pieces) > 0:
			return self.pieces.pop(0)
		return False

class Hanoi:
	stepcount = 0
	
	def __init__ (self, pieces):
		height = pieces
		self.pieces = pieces
		self.first  = Tower(height, pieces)
		self.middle = Tower(height, 0)
		self.last   = Tower(height, 0)

	def __str__ (self):
		""" Print the towers next to eachother """
		hanoistring = str(self.first)
		hanoistring = self.add_tower_to_string(hanoistring, str(self.middle))
		hanoistring = self.add_tower_to_string(hanoistring, str(self.last))
		return hanoistring
		
	def add_tower_to_string (self, multilinestring, towerstring):
		""" Take a string that has a tower in it and add another tower to the string """
		lines = multilinestring.split("\n")		
		towerlines = towerstring.split("\n")

		if not len(towerlines) == len(lines):
			print("Can't add tower to string, strings are not of equel height")
			return False

		returnstring = ""
		
		for i in range(0, len(lines)):
			returnstring += lines[i] + "\t" +  towerlines[i] + "\n"

		# We added a \n too many, remove again
		return returnstring[:-2]

	def solve (self):
		""" Solve the problem """
		self.step(self.pieces, self.first, self.last, self.middle)

	def step (self, pieces, first, last, middle):
		""" Move pieces pieces from first to last via middle in a recursive way using 2 ^ n - 1 steps"""
		if (pieces == 1):
			self.swap(first, last) #Base case
			
			self.stepcount = self.stepcount + 1
			print("step count %d" % self.stepcount)
			print(self)
		else:
			self.step(pieces - 1, first, middle, last) 		# Solve for n-1
			self.step(1, first, last, middle) 				# Swap the biggest
			self.step(pieces - 1, middle, last, first)		# Bring them all to the last tower
		

	def swap (self, tower1, tower2):
		""" Swap piece from tower1 to tower2 """
		tower2.add_piece(tower1.remove_piece())

Hanoi(5).solve()
