#!/usr/bin/python3

# Importing Modules
from sys import argv
import os

# Standardised error
def error(message):
	print("ERROR: %s" % message)
	exit()


# Initial error checks

# Check for usage error
try:
	script, file_name = argv
	print("Updating...")
except:
	error("must have exactly one argument")

# Checks file exists, moves it to a list
try:
	with open(file_name, 'r+') as file:
		target = [line.strip() for line in file]
except:
	error("file does not exist")
print("File read to list")


# Meta Validation

# Information finder
information, errors = [], []
for line in target:
	if "BLOG INFORMATION DATA" in line:
		information.append(line)
	elif len(information) != 0:
		if len(information) < 5:
			information.append(line)
if len(information) == 0:
	error("no blog information found")

# Title information checker
if (":> " in information[1] and len(information[1].split(":> ")) == 2):
	try:	
		blog_title = information[1].split(":> ")[1].split(" -->")[0].replace("-->","")
	except:
		error("invalid title given")
else:
	error("invalid title given")

# Date information checker
if (":> " in information[2] and len(information[2].split(":> ")) == 2):
	try:	
		blog_date = information[2].split(":> ")[1].split(" -->")[0]
	except:
		error("invalid date given")
else:
	error("invalid date given")

# Catagories information checker
if (":> " in information[3] and len(information[3].split(":> ")) == 2):
	try:	
		blog_catagories = information[3].split(":> ")[1].split(" -->")[0].split(", ")
		list_files = os.listdir("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/")
		non_catagories, known_catagories, new_catagories = ["all", "template"], [], [] 
		for entry in list_files:
			if entry in non_catagories:
				pass
			else:
				known_catagories.append(entry)
		for entry in blog_catagories:
			if entry not in known_catagories:
				new_catagories.append(entry)
	except:
		error("invalid catagories given")
else:
	error("invalid catagories given")

# Summary information checker
if (":> " in information[4] and len(information[4].split(":> ")) == 2):
	try:	
		blog_summary = information[4].split(":> ")[1].split(" -->")[0]
	except:
		error("invalid summary given")
else:
	error("invalid summary given")

# Correct information checker
print("Passed data error check")
print("\nGIVEN INFORMATION")
print("Title:",blog_title)
print("Date:",blog_date)
print("Catagories:",blog_catagories)
print("Summary:",blog_summary,"\n")
q = 0
while q == 0:
	ans = input("Are you happy with the above? (y/n) ")
	if ans == "y":
		q = 1
		pass
	elif ans == "n":
		error("blog data rejected")
	else:
		pass
print("Blog data accepted")



# Managing new catagories

for entry in new_catagories:
	# Creating New Lists
	entry_list = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/"+entry, 'w')
	entry_list.write(open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/template").read())
	entry_list.close()
	with open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/"+entry, 'r+') as file:
		new_list = [line for line in file]
	for line in new_list:
		if "[template]" in line:
			old_line, n = line, new_list.index(line)
			new_list.pop(n)
			new_list.insert(n, old_line.replace("[template]", entry))
	entry_list = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/"+entry, 'w')
	entry_list.truncate()
	for line in new_list:
		entry_list.write(line)
	entry_list.close()
	print("Created %s catagory" % entry)

# Adding to word cloud - untested
for entry in blog_catagories:
    with open("//home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/cloud.txt", 'r') as file:
        cat_list = [line for line in file]
    cat_list.append(entry+"\n")
    cloud_file = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/cloud.txt", 'w')
    for line in cat_list:
        cloud_file.write(line)
    cloud_file.close()
    print("Added %s catagory to word cloud file" % entry)


# Adding Blog to Catagory Lists
for entry in (blog_catagories+["all"]):
	with open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/"+entry, 'r+') as file:
		file_list = [line for line in file]
	for line in file_list:
		if "<!-- List Begins Here -->" in line:
			n = file_list.index(line)
			file_list.insert(n+1, '			<li><a href="../'+blog_date+'_'+blog_title.replace(' ','')+'">'+blog_date+'     '+blog_title+'</a></li>\n')
	entry_list = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/"+entry, 'w')
	entry_list.truncate()
	for line in file_list:
		entry_list.write(line)
	entry_list.close()
	print("Added blog to %s catagory list" % entry)


# Adding blog to Recent Blogs page
with open("/home/josh/Programs/Web/HTML/fogg.me.uk/blog", 'r+') as file:
	file_list = [line for line in file]
for line in file_list:
	if "<!-- Recent Blogs Begin Here -->" in line:
		n = file_list.index(line)
		file_list.insert(n+1, '		<article>\n')
		file_list.insert(n+2, '			<h3> <a href="blogs/'+blog_date+'_'+blog_title.replace(' ','')+'">'+blog_title+'</a> - '+blog_date+'</h3>\n')
		file_list.insert(n+3, '			<p>'+blog_summary+'</p>\n')
		file_list.insert(n+4, '		</article>\n')
		file_list.insert(n+5, '\n')
		file_list.insert(n+6, '		<br class="small">\n')
		file_list.insert(n+7, '\n')
entry_list = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blog", 'w')
entry_list.truncate()
for line in file_list:
	entry_list.write(line)
entry_list.close()
print("Added blog to recent blogs page")


# Removing the least recent blog from Recent Blogs page
with open("/home/josh/Programs/Web/HTML/fogg.me.uk/blog", 'r+') as file:
	file_list = [line for line in file]
for line in file_list:
	if "<!-- Recent Blogs End Here -->" in line:
		n = file_list.index(line)
		for x in range(1, 8):
			file_list.pop(n-x)
entry_list = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blog", 'w')
entry_list.truncate()
for line in file_list:
	entry_list.write(line)
entry_list.close()
print("Removed least recent blog from recent blogs page")


# Program is finished!
print("Done!\n")
