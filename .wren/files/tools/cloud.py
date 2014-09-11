#!/usr/bin/python3

# This is the cloud updater, written as part of the FoggBlog
# blogging platform. All work is licensed under the GLPv3+. 

# Set limits on font size
small_font = 12
large_font = 60

# Set limits on colour
small_font = 12
large_font = 60

# Fetches data file
with open("cloud.txt", 'r') as file:
	# Nested list, formated [catagory name, frequency]
	data = [[line.split(" ")[0].strip(), int(line.split(" ")[1].strip())] for line in file]

# Establishes frequency range
least_freq = min([item[1] for item in data])
most_freq = max([item[1] for item in data])

# Amount to increase font by for each frequency tally
scale_factor = (large_font - small_font)/(most_freq - least_freq)

# Test output
output = open("test.html", "w")
for entry in data:
	# Calculates font size for each entry
	font_size = small_font+((entry[1]-least_freq)*scale_factor)
	# Writes catagory link to file
	output.write("<a href=\"blog/catagory/{0}\" style=\"font-size: {1}px;\">{0}</a>".format(entry[0], font_size))