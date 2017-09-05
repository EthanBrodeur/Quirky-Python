def count_syllables(word):
	# below code from AbigailB on Stack Overflow
	count = 0 
	vowels = 'aeiouy'
	word = word.lower().strip(".,:;?!")
	if word[0] in vowels:
	    count +=1
	for index in range(1,len(word)):
	    if word[index] in vowels and word[index-1] not in vowels:
	        count +=1
	if word.endswith('e'):
	    count -= 1
	if word.endswith('le'):
	    count+=1
	if count == 0:
	    count +=1
	return count

	# TODO: ADD SOMETHING FOR NON "A-Z" phrases

def string_to_haiku(tweet):
	words = tweet.split()
	haiku = []
	index_start_of_line = 0
	result = create_haiku_line(words, index_start_of_line, 5)
	if result[0] == False:
		# no haiku was possible with this string....
		print("Failed at line 1!")
	else:
		index_start_of_line = result[2]
		haiku.append(result[1])

		result = create_haiku_line(words, index_start_of_line, 7)
		if result[0] == False:
			# no haiku was possible with this string....
			print("Failed at line 2")
		else:
			index_start_of_line = result[2]
			haiku.append(result[1])

			result = create_haiku_line(words, index_start_of_line, 5)
			if result[0] == False:
				# no haiku was possible with this string....
				print("Failed at line 3")
			else:
				index_start_of_line = result[2]
				haiku.append(result[1])
	return haiku

def create_haiku_line(words, cursor, num_syl):
	line = ""
	num_syl_line = 0
	index_start_of_line = cursor

	while num_syl_line < num_syl:
		if cursor > len(words):
			# no haiku possible
			# outside this func, check to see if index 0 of return tuple == false
			return [False]
		line += words[cursor] + " "
		num_syl_line += count_syllables(words[cursor])
		cursor += 1
		if num_syl_line == num_syl:
			# this line is done!
			index_start_of_line = cursor
			break
		if num_syl_line > num_syl:
			# that section of the tweet didn't meet haiku criteria for this line
			# so try reconstructing, starting at the next word in the tweet
			line = ""
			num_syl_line = 0
			index_start_of_line += 1
			cursor = index_start_of_line

	return [True, line, index_start_of_line]


my_string = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

my_string = "the quick brown fox jumped over the lazy tommy skyler is over there and she is working on her laptop what is paul doing he is reading a book doritos"
result = string_to_haiku(my_string)

if len(result) > 3:
	print('really weird error')

if len(result) < 3:
	print('looks like we didn\'t get a full haiku.')
else:
	for line in result:
		print(line)


