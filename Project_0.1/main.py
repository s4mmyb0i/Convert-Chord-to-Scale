import subprocess  # NEED TO CODE FOR ERRORS AND ADD DOCSTRINGS

# HOW USE GIT FOR VERSION CONTROL?

if __name__ == "__main__":  # Code to change sheet_music.ly into a scale

	# these two lists are mutable based on the transposing key
	notes_flat = ['c\'', 'des\'', 'd\'', 'ees\'', 'e\'', 'f\'', 'ges\'', 'g\'', 'aes\'', 'a\'', 'bes\'', 'b\'']
	notes_sharp = ['c\'', 'cis\'', 'd\'', 'dis\'', 'e\'', 'f\'', 'fis\'', 'g\'', 'gis\'', 'a\'', 'ais\'', 'b\'']

	# for program to refer to (list for all key signatures)
	flat_keys = ['des', 'ees', 'f', 'ges', 'aes', 'bes', 'b']
	sharp_keys = ['c', 'cis', 'd', 'dis', 'e', 'fis', 'g', 'gis', 'a', 'b', 'ais']

	# for transposing
	key2transpose_val_flat = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b']
	key2transpose_val_sharp = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']

	# broken up dict for the relationship between chord symbols and scales; indices should match
	type_list = ['lydian', 'major', 'dorian', 'mixolydian', 'diminished']
	symbol_list = ['∆#11', '∆', '-', '7', 'o']

	# dict for converting capital chord letters to lilypond notes
	capital_lily = {
		'C': 'c',
		'C#': 'cis',
		'Db': 'des',
		'D': 'd',
		'D#': 'dis',
		'Eb': 'ees',
		'E': 'e',
		'F': 'f',
		'F#': 'fis',
		'Gb': 'ges',
		'G': 'g',
		'G#': 'gis',
		'Ab': 'aes',
		'A': 'a',
		'A#': 'ais',
		'Bb': 'bes',
		'B': 'b'
	}


	def reset_notes():
		"""
		Resets notes to original setting
		"""
		global notes_sharp, notes_flat
		notes_flat = ['c\'', 'des\'', 'd\'', 'ees\'', 'e\'', 'f\'', 'ges\'', 'g\'', 'aes\'', 'a\'', 'bes\'', 'b\'']
		notes_sharp = ['c\'', 'cis\'', 'd\'', 'dis\'', 'e\'', 'f\'', 'fis\'', 'g\'', 'gis\'', 'a\'', 'ais\'', 'b\'']


	def transpose_flat(key):
		acc = 0
		while acc < key2transpose_val_flat.index(key):
			first_element = notes_flat.pop(0)
			notes_flat.append(first_element)
			acc += 1


	def transpose_sharp(key):
		acc = 0
		while acc < key2transpose_val_sharp.index(key):
			first_element = notes_sharp.pop(0)
			notes_sharp.append(first_element)
			acc += 1


	def major(key):
		global scale
		scale_length = 0
		step_index = 0

		scale += '\n'

		if key in sharp_keys:
			transpose_sharp(key)
			while scale_length <= 6:
				while step_index <= 5:
					scale += notes_sharp[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_sharp[step_index]
				step_index += 2
				scale_length += 1

				while 5 <= step_index <= 12:
					scale += notes_sharp[step_index]
					step_index += 2
					scale_length += 1
			scale += '\n}'

		if key in flat_keys:
			transpose_flat(key)
			while scale_length <= 6:
				while step_index <= 5:
					scale += notes_flat[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_flat[step_index]
				step_index += 2
				scale_length += 1

				while 5 <= step_index <= 12:
					scale += notes_flat[step_index]
					step_index += 2
					scale_length += 1
			scale += '\n}'

	def whole_tone(key):
		global scale
		scale_length = 0
		step_index = 0

		scale += '\n'

		if key in sharp_keys:
			transpose_sharp(key)
			while scale_length <= 5:
				scale += notes_sharp[step_index]
				step_index += 2
				scale_length += 1
			scale += '\n}'

		if key in flat_keys:
			transpose_flat(key)
			while scale_length <= 5:
				scale += notes_flat[step_index]
				step_index += 2
				scale_length += 1
			scale += '\n}'


	def diminished(key):
		global scale
		scale_length = 0
		step_index = 0

		scale += '\n'

		if key in sharp_keys:
			transpose_sharp(key)
			while scale_length <= 7:
				scale += notes_sharp[step_index]
				step_index += 2
				scale += notes_sharp[step_index]
				step_index += 1
				scale_length += 2
			scale += '\n}'

		if key in flat_keys:
			transpose_flat(key)
			while scale_length <= 7:
				scale += notes_flat[step_index]
				step_index += 2
				scale += notes_flat[step_index]
				step_index += 1
				scale_length += 2
			scale += '\n}'


	def flat_9(key):
		global scale
		scale_length = 0
		step_index = 0

		scale += '\n'

		if key in sharp_keys:
			transpose_sharp(key)
			while scale_length <= 7:
				scale += notes_sharp[step_index]
				step_index += 1
				scale += notes_sharp[step_index]
				step_index += 2
				scale_length += 2
			scale += '\n}'

		if key in flat_keys:
			transpose_flat(key)
			while scale_length <= 7:
				scale += notes_flat[step_index]
				step_index += 1
				scale += notes_flat[step_index]
				step_index += 2
				scale_length += 2
			scale += '\n}'


	def mixolydian(key):
		global scale
		scale_length = 0
		step_index = 0

		scale += '\n'

		if key in sharp_keys:
			transpose_sharp(key)
			while scale_length <= 6:
				while step_index <= 5:
					scale += notes_sharp[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_sharp[step_index]
				step_index += 2
				scale_length += 1

				while 5 <= step_index <= 10:
					scale += notes_sharp[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_sharp[step_index]
				step_index += 2
				scale_length += 1
			scale += '\n}'

		if key in flat_keys:
			transpose_flat(key)
			while scale_length <= 6:

				while step_index <= 5:
					scale += notes_flat[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_flat[step_index]
				step_index += 2
				scale_length += 1

				while 5 <= step_index <= 10:
					scale += notes_flat[step_index]
					step_index += 2
					scale_length += 1
			scale += '\n}'


	def dorian(key):
		global scale
		scale_length = 0
		step_index = 0

		scale += '\n'

		if key in sharp_keys:
			transpose_sharp(key)
			while scale_length <= 6:
				while step_index <= 3:
					scale += notes_sharp[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_sharp[step_index]
				step_index += 2
				scale_length += 1

				while 3 <= step_index <= 10:
					scale += notes_sharp[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_sharp[step_index]
				step_index += 2
				scale_length += 1
			scale += '\n}'

		if key in flat_keys:
			transpose_flat(key)
			while scale_length <= 6:

				while step_index <= 3:
					scale += notes_flat[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_flat[step_index]
				step_index += 2
				scale_length += 1

				while 5 <= step_index <= 10:
					scale += notes_flat[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_flat[step_index]
				step_index += 2
				scale_length += 1
			scale += '\n}'


	def lydian(key):
		global scale
		scale_length = 0
		step_index = 0

		scale += '\n'

		if key in sharp_keys:
			transpose_sharp(key)
			while scale_length <= 6:
				while step_index <= 6:
					scale += notes_sharp[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_sharp[step_index]
				step_index += 2
				scale_length += 1

				while 6 <= step_index <= 11:
					scale += notes_sharp[step_index]
					step_index += 2
					scale_length += 1
			scale += '\n}'

		if key in flat_keys:
			transpose_flat(key)
			while scale_length <= 6:
				while step_index <= 6:
					scale += notes_flat[step_index]
					step_index += 2
					scale_length += 1

				step_index -= 1
				scale += notes_flat[step_index]
				step_index += 2
				scale_length += 1

				while 6 <= step_index <= 11:
					scale += notes_flat[step_index]
					step_index += 2
					scale_length += 1
			scale += '\n}'

	def syntax():
		global scale
		scale += '\n\\new Staff {'
		scale += '\n\omit Staff.TimeSignature'
		scale += '\n\omit Staff.BarLine'


	# calling functions
	scale = '\\version \"2.24.2\"\n'

	f_chord_progression = open('chord_progression.txt', 'r')

	for line in f_chord_progression.readlines():
		line_split = line.split()
		note_name = line_split[0]
		lilypond_note = capital_lily.get(note_name)
		for symbol in symbol_list:
			if symbol in line:
				syntax()
				func = globals()[(type_list[symbol_list.index(symbol)])]
				func(lilypond_note)
				reset_notes()
				break

	f_chord_progression.close()

	# code to run lilypond
	# Dr. Wolfe, please change the following filepath to where lilypond is located on your device
	lilypond_location = '/Users/sam/Documents/lilypond-2.24.2/bin/lilypond'
	f = open('sheet_music.ly', 'w')
	f.write(scale)
	f.close()

	#  convert sheet_music.ly into a pdf
	command = lilypond_location + ' sheet_music.ly'
	p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	for line in p.stdout.readlines():
		print(line)
	retval = p.wait()
