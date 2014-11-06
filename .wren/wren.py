#!/usr/bin/python3

# This is the updater for the Wren blogging platform.
# Before running this script please familiarise your-
# self with the instructions in the readme.md file.

from datetime import datetime
from math import floor
from os import getcwd, makedirs, path, walk
from re import search, sub
from shutil import copy
from time import sleep


# These functions allow for timeout when the Wren
# updater is run via the "Run In Terminal" command

def sucess(message):
    print(message + "\n")
    sleep(3)
    exit(0)


def gerror(message):
    print("ERROR: {0}".format(message))
    sleep(3)
    exit(1)


# At various points it's needed to have a function
# that replaces all instances of a word in a file.
# The easy solution would be to os.call 'sed' but
# I wanted to avoid relying on outside programs.

def sed(find, replace, target):
    with open(target, "r", encoding='utf-8') as file:
        lines = file.readlines()
    with open(target, "w", encoding='utf-8') as file:
        for line in lines:
            file.write(sub(find, replace, line))


def supsed(find, replace):
    for root, dirs, files in walk("../", topdown=False):
        for name in files:
            target = path.join(root, name)
            if (".git" in target) or ("images" in target):
                pass
            else:
                sed(find, replace, target)


# Checks running from the .wren directory so that the
# relative locations of files can be known.

if ".wren" not in getcwd():
    gerror("please run from the .Wren directory")


# If the Wren has not been run before the following code
# will run. This sets up all the files with any variables
# that are user modified. WARNING: that this code does not
# currently check if the URL is correctly formatted, nor
# does it check if it actually exists.

if not path.isfile("catdat.csv"):
    print("Setting up Wren...")

    blogger = input("What is your full name? ")
    supsed("BLOGGER", blogger)

    blogurl = input("What is your website url? ")
    supsed("BLOGURL", blogurl)

    # Wren can integrate Disqus as a comments system if
    # the user so wants. In future versions I'm going to
    # have a look around for alternative systems.
    q = 0
    while q == 0:
        ans = input("Do you wish to use Disqus for comments? (y/n) ")
        if ans == "y":
            print("If you don't have a Disqus account go to")
            print("https://disqus.com/profile/signup/ now!")
            shortname = input("What is your Disqus shortname? ")
            sed("DSHORTNAME", shortname, "../php/comments.php")
            q = 1
            pass
        elif ans == "n":
            with open("../php/comments.php", "w+") as file:
                file.write('<br class="small">\n')
            q = 1
            pass

    with open("catdat.csv", "w+") as file:
        file.write("Category,Count")

    sucess("Setup complete!")


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
text = " ".join(TXTcontent).split(" ")


# This calculates the approximate reading time for the blog.
# The calculation is based upon an average screen-reading
# rate of ~200 words per minute.

if len(text)/200 < 1:
    secs = int(float(len(text))*0.3)
    readtime = "~{0} seconds".format(secs)
else:
    mins = int(floor(len(text)/float(200)))
    secs = int(((len(text)/float(200))-mins)*60)
    readtime = "~{0} minutes {1} seconds".format(mins, secs)


print("Please enter the following data as prompted")
title = input("\nTitle:\n")
categories = input("\nCategories:\n").split(" ")
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
url = "http://BLOGURL/blog/" + filedate + "/" + urltitle

tmp = []
for item in categories:
    item = clean(item)
    if len(item) != 0 and item not in tmp:
        tmp.append(item)
categories = tmp


print("\nGIVEN INFORMATION")
print("Title:", title)
print("URL:", url)
print("Time:", datelong)
print("Reading time:", readtime)
print("Categories:", categories)
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


# When a new category is created it needs all the files
# associated with it creating too, along with the existing
# files that need to refrence it updating.

with open("catdat.csv", "r") as file:
    catdat = [line.strip() for line in file]
catdat.pop(0)
catnames = [line.split(",")[0] for line in catdat]
catcount = [int(line.split(",")[1]) for line in catdat]

newcat = []
for item in categories:
    if item not in catnames:
        newcat.append(item)

for cat in newcat:
    copy("feed-template.xml", "../blog/feed/" + cat + ".xml")
    copy("cat-template.html", "../blog/cat/" + cat + ".html")
    sed("TEMPLATE", cat, "../blog/feed/" + cat + ".xml")
    sed("TEMPLATE", cat, "../blog/cat/" + cat + ".html")
    catnames.append(cat)
    catcount.append(0)
    print("Created", cat, "category")

for cat in categories:
    pos = catnames.index(cat)
    newcount = catcount[pos] + 1
    catcount.pop(pos)
    catcount.insert(pos, newcount)

combined = sorted(list(zip(catnames, catcount)))
catnames = [name for (name, count) in combined]
catcount = [count for (name, count) in combined]

with open("catdat.csv", "w") as file:
    file.write("Category,Count\n")
    for x in range(0, len(catnames)):
        file.write("{0},{1}\n".format(catnames[x], catcount[x]))


# This inserts a single line of HTML which links to the new
# blog into each of the category lists which it falls into.

newline = '<li><a href="{0}">{1} : {2}</a></li>'
newline = newline.format(url, datesmll, title)

for cat in (categories + ["all"]):
    with open("../blog/cat/" + cat + ".html", "r") as file:
        lines = [line for line in file]
    for line in lines:
        if "<!-- List Begins Here -->" in line:
            n = lines.index(line)
            lines.insert(n + 1, ' ' * 12 + newline + "\n")
    catfile = open("../blog/cat/" + cat + ".html", "w+")
    for line in lines:
        catfile.write(line)
    catfile.close()
    print("Added blog to", cat, "category list")


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

for cat in (categories + ["all"]):
    with open("../blog/feed/" + cat + ".xml", "r") as file:
        lines, items, record = [], 0, True
        for line in file:
            if "<item>" in line:
                items += 1
            if "<!-- List Ends Here -->" in line:
                record, items = True, 0
            if items > 24:
                record = False
            if record is True:
                lines.append(line)
    for line in lines:
        if "<!-- List Begins Here -->" in line:
            n = lines.index(line)
            for x in range(0, len(newlines)):
                lines.insert(n + x + 1, " " * 8 + newlines[x] + "\n")
    catfeed = open("../blog/feed/" + cat + ".xml", "w+")
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
    '    <h4>  <div style="float: right;">' + datesmll + '</div></h4>',
    '    <h3><a href="{0}">{1}</a></h3>'.format(url, title),
    "    <p>" + summary + "</p>",
    "</article>\n",
    '<br class="small">\n'
]

with open("../blog/index.html", 'r') as file:
    lines, recent, record = [], 0, True
    for line in file:
        if '<br class="small">' in line:
            recent += 1
        if '<!-- Recent Blogs End Here -->' in line:
            record, recent = True, 0
        if recent > 4:
            record = False
        if record is True:
            lines.append(line)

for line in lines:
    if "<!-- Recent Blogs Begin Here -->" in line:
        n = lines.index(line)
        for x in range(0, len(newlines)):
            lines.insert(n + x + 1, " " * 8 + newlines[x] + "\n")
blogfile = open("../blog/index.html", "w+")
for line in lines:
    blogfile.write(line)
blogfile.close()
print("Updated the main blogs page")


# The following code will update the category word cloud. The
# design is inspired by that used by TagCrowd.com but isn't
# disimilar to the ones commonly used on Wordpress. Note that
# this code does not yet emulate the colouring aspect of the
# word clouds as this requires a more sophisticated algorithm.
# The unit used for font size is 'em'

smallsize = 1.0
largesize = 5.0
sizerange = largesize - smallsize

try:
    countrange = max(catcount)-min(catcount)
    ratio = sizerange/countrange
except:
    ratio = 1

catsizes = []
for count in catcount:
    size = smallsize + (count - 1) * ratio
    catsizes.append("{0:.2f}".format(size))

string = "        <p>"
for cat in catnames:
    style = "font-size: {0}em;".format(catsizes[catnames.index(cat)])
    string += '<a href="{0}" style="{1}">'.format(cat, style)
    string += cat + "</a> "
string += "</p>\n"

with open("../blog/cat/index.html", "r") as file:
    lines = [line for line in file]
for line in lines:
    if "<!-- Begining of tagcloud -->" in line:
        index = lines.index(line) + 1
        lines.pop(index)
        lines.insert(index, string)
cloudfile = open("../blog/cat/index.html", "w+")
for line in lines:
    cloudfile.write(line)
cloudfile.close()
print("Updated the category wordcloud")


sucess("Done!")
