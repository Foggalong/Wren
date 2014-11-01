#!/usr/bin/python3

# This is the updater for the Wren blogging platform.
# Before running this script please familiarise your-
# self with the instructions in the readme.md file.

from datetime import datetime
from math import floor
from os import getcwd, makedirs, path
from re import search, sub
from shutil import copy
from time import sleep


# Thes function allows for timeout when the Wren
# updater is run via the "Run In Terminal" command

def gerror(message):
    print("ERROR: {0}".format(message))
    sleep(3)
    exit(1)


# At various points it's needed to have a function
# that replaces all instances of a word in a file.
# The easy solution would be to os.call 'sed' but
# I wanted to avoid relying on outside programs.

def sed(find, replace, target):
    with open(target, "r") as file:
        lines = file.readlines()
    with open(target, "w") as file:
        for line in lines:
            file.write(sub(find, replace, line))


# Checks running from the Wren directory so that
# the relative locations of files can be known

if ".wren" not in getcwd():
    gerror("please run from the .Wren directory")
else:
    print("Updating blog...")


# Extracts the blog body from the input file. It's fixed
# so that the level of indentation doesn't need changing.

with open("blog-new.html", 'r') as file:
    record, HTMLcontent = False, []
    for line in file:
        if "<article>" in line:
            record = True
        elif "</article>" in line:
            record = False
        elif record is True:
            HTMLcontent.append(line)


# Strips out the HTML tags and white space in order
# to calculate the approximate reading time.

TXTcontent = []
for line in HTMLcontent:
    raw = ''
    record = True
    for i in line:
        if i == "<":
            record = False
        elif i == ">":
            record = True
        elif record is True:
            raw += i
    TXTcontent.append(raw.strip())
text = " ".join(TXTcontent)


# This calculates the approximate reading time for the blog.
# The calculation is based upon an average screen-reading
# rate of ~200 words per minute.

if len(text)/200 < 1:
    secs = int(float(len(text))*0.3)
    readtime = "~{0} seconds reading".format(secs)
else:
    mins = int(floor(len(text)/float(200)))
    secs = int(((len(text)/float(200))-mins)*60)
    readtime = "~{0} minutes {1} seconds reading".format(mins, secs)


print("Please enter the following data as prompted")
title = input("\nTitle:\n")
catagories = input("\nCatagories:\n").split(" ")
summary = input("\nSummary:\n")


# The time of the blogs creation is needed in a variety of
# formats, not all provide by the datetime module.

# YYYY-MM-DD
datesmll = str(datetime.date(datetime.now()))
# YYYY/MM/DD
filedate = sub(r"-", "/", datesmll)
# Day DD Mon YYYY HH:MM:SS
datelong = str(datetime.ctime(datetime.now()))
# Day, DD Mon YYYY HH:MM:SS TMZ
datelong = ", ".join(datelong.split(" ", 1)) + " GMT"


# Data used in URLs has to be devoid of any special characters
# that could cause problems. Because of that, characters not
# in the range a-z or 0-1 are removed from certain values.

def clean(string):
    tmp = list(string.lower().strip())
    tmp = [i for i in tmp if search("[^a-z0-9]", i) is None]
    return "".join(tmp)

urltitle = clean(title)
url = "http://fogg.me.uk/blog/" + filedate + "/" + urltitle

tmp = []
for item in catagories:
    item = clean(item)
    if len(item) != 0:
        tmp.append(item)
catagories = tmp


print("\nGIVEN INFORMATION")
print("Title:", title)
print("URL:", url)
print("Time:", datelong)
print("Reading time:", readtime)
print("Catagories:", catagories)
print("Summary:", summary, "\n")

q = 0
while q == 0:
    ans = input("Are you happy with the above? (y/n) ")
    if ans == "y":
        q = 1
        pass
    elif ans == "n":
        gerror("meta data rejected")
print("Meta data accepted\n")


# Copies the blog data to the template file and then moves
# it into place. The formatting for blog-template.html is
# set for the destination rather than its current location

dest = "../blog/{0}/{1}.html".format(filedate, urltitle)
if not path.exists(path.dirname(dest)):
    makedirs(path.dirname(dest))
copy("blog-template.html", dest)
sed("BLOGDATE", datesmll, dest)
sed("BLOGTITLE", title, dest)
sed("READINGTIME", readtime, dest)
sed("BLOGCONTENT", "".join(HTMLcontent), dest)


# When a new catagory is created it needs all the files
# associated with it creating too, along with the existing
# files that need to refrence it updating.

with open("catdat.csv", "r") as file:
    catdat = [line.strip() for line in file]
catdat.pop(0)
catnames = [line.split(",")[0] for line in catdat]
catcount = [int(line.split(",")[1]) for line in catdat]

newcat = []
for item in catagories:
    if item not in catnames:
        newcat.append(item)

for cat in newcat:
    copy("feed-template.xml", "../blog/feed/" + cat + ".xml")
    copy("cat-template.html", "../blog/cat/" + cat + ".html")
    sed("TEMPLATE", cat, "../blog/feed/" + cat + ".xml")
    sed("TEMPLATE", cat, "../blog/cat/" + cat + ".html")
    catnames.append(cat)
    catcount.append(0)
    print("Created", cat, "catagory")

for cat in catagories:
    pos = catnames.index(cat)
    count = catcount[pos] + 1
    catcount.pop(pos)
    catcount.insert(pos, count)

with open("catdat.csv", "w") as file:
    for x in range(0, len(catnames)-1):
        file.write("{0},{1}\n".format(catnames[x],catcount[x]))


# This inserts a single line of HTML which links to the new
# blog into each of the catagory lists which it falls into.

newline = '<li><a href="{0}">{1} - {2}</a></li>'
newline = newline.format(url, datesmll, title)

for cat in (catagories + ["all"]):
    with open("../blog/cat/" + cat + ".html", "r") as file:
        lines = [line for line in file]
    for line in lines:
        if "<!-- List Begins Here -->" in line:
            n = lines.index(line)
            lines.insert(n + 1, ' ' * 12 + newline + "\n")
    catfile = open("../blog/cat/" + cat + ".html", "w")
    catfile.truncate()
    for line in lines:
        catfile.write(line)
    catfile.close()
    print("Added blog to", cat, "catagory list")


# Inserts a the nessisary lines into the XML files so that
# the new blog shows up in the RSS feeds it alls into. Note
# that this process doesn't currently remove any blogs from
# the RSS file. This is recommended as it prevents the file
# from becoming too big. I'll do some research and see what
# others consider to be an acceptable cutoff point.

newlines = [
    "<item>",
    "    <title>" + title + "</title>",
    "    <link>" + url + "</link>",
    "    <guid>" + url + "</guid>",
    "    <pubDate>" + datelong + "</pubDate>",
    "    <description>" + summary + "</description>",
    "</item>\n"
]

for cat in (catagories + ["all"]):
    with open("../blog/feed/" + cat + ".xml", "r") as file:
        lines = [line for line in file]
    for line in lines:
        if "<!-- List Begins Here -->" in line:
            n = lines.index(line)
            for x in range(0, 7):
                lines.insert(n + x + 1, " " * 8 + newlines[x] + "\n")
    catfeed = open("../blog/feed/" + cat + ".xml", "w")
    catfeed.truncate()
    for line in lines:
        catfeed.write(line)
    catfeed.close()
    print("Added blog to", cat, "RSS feed")


# The main blogs page lists the 5 most recent blogs posted so
# adding this new one means also removing the least recent.
# IMPORTANT: this code currently just removes the least recent
# post without checking if 5 blogs have actually been posted
# yet. I'll try to correct this in future versions.

newlines = [
    "<article>",
    '    <h3><a href="{0}>{1}</a> - {2}</h3>'.format(url, title, datesmll),
    "    <p>" + summary + "</p>",
    "</article>\n",
    '<br class="small">\n'
]

with open("../blog/index.html", 'r') as file:
    lines = [line for line in file]
for line in lines:
    if "<!-- Recent Blogs Begin Here -->" in line:
        n = lines.index(line)
        for x in range(0, 4):
            lines.insert(n + x + 1, " " * 8 + newlines[x] + "\n")
    elif "<!-- Recent Blogs End Here -->" in line:
        n = lines.index(line)
        for x in range(1, 6):
            lines.pop(n-x)
blogfile = open("../blog/index.html", "w")
blogfile.truncate()
for line in lines:
    blogfile.write(line)
blogfile.close()
print("Updated the main blogs page")


# The following code will update the catagory word cloud. The
# design is inspired by that used by TagCrowd.com but isn't
# disimilar to the ones commonly used on Wordpress. Note that
# this code does not yet emulate the colouring aspect of the
# word clouds as this requires a more sophisticated algorithm.
# The unit used for font size is 'em'

smallsize = 1.0
largesize = 5.0
sizerange = largesize - smallsize
countrange = max(catcount)-min(catcount)

try:
    ratio = sizerange/countrange
    catsizes = [count * ratio for count in catcount]
except:
    ratio = 1

string = "        <p>"
for cat in catnames:
    style = "font-size: {0}em;".format(catsizes[catnames.index(cat)])
    string += '<a href="{0}" style="{1}">'.format(cat, style)
    string += cat + "</a> "

with open("../blog/cat/index.html", "r") as file:
    lines = [line for line in file]
for line in lines:
    if "<!-- Begining of tagcloud -->" in line:
        index = lines.index(line) + 1
        lines.pop(index)
        lines.insert(index, string)
cloudfile = open("../blog/cat/index.html", "w")
cloudfile.truncate()
for line in lines:
    cloudfile.write(line)
cloudfile.close()
print("Updated the catagory wordcloud")


print("Done!\n")
