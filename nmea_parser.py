FILE_PATH = 'NMEA_raw_string.txt'
OUTPUT_FILE = 'NMEA_parsed_string.txt'

# create the output file
o = open(OUTPUT_FILE, 'w+')
with open(FILE_PATH) as f:
	b = ""
	while True:
		
		# read through the raw text character by character
		c = f.read(1)
		
		# stop if we've reached the end of the file
		if not c:
			break

		# if the current character is a '$'
		# then we've reached the next nmea row
		if c == '$':
			# remove any spaces or new lines
			b = b.replace('\n', '').replace(' ', '')
			# write buffer to file
			o.write('$' + b + '\n')
			# reset the string buffer
			b = ""
		
		# otherwise add the character to the current row buffer
		else:
				b = b + c