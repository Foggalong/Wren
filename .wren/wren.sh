#!/bin/bash

# This is Wren, a super simple, open source blogging platform written
# in bash. This script manages the writing and addition of new blogs.

# Copyright (C) 2014
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

version="0.2-alpha"

function gerror() {
    echo -e "$1"
    sleep 3
    exit 1
}


# Creating New Blog
# -----------------

# Writer
echo -e \
    "Please write your blog below, using HTML for\n"
    "\rformatting and adding 'EOF' as the last line.\n"
while [ "$line" != "EOF" ]; do
    read -p "> " line
    if [ "$line" == "EOF" ]; then
        break
    else
        blog_body+="$line\n"
    fi
done

# Reading length - using 250 WPM
blog_length=$(($(echo "$blog_body" | wc -w) / 250))

echo "Enter each piece of meta-info as prompted"

# Blog title
while true; do
    read -p "\nGive a post title:\n" answer
    if [ "$answer" == "" ]; then
        echo -e "Please enter a title"
    else
        blog_title="$answer"
        break
    fi
done

# Blog date
blog_date=$(date +%F)      # 2014-06-17
blog_date_long=$(date +%c) # Tue, 17 Jun 2014 13:20:00
# Notes, RSS asks for 'Tue, ...' but %c gives no ','

# Blog catagories
echo -e \
    "\nList the catagories this post falls into,\n"
    "\rseperating each by using a space."
read -p "" answer
blog_catagories=($answer)

# Blog summary
while true; do
    read -p "\nGive a brief summary of the post:\n" answer
    if [ "$answer" == "" ]; then
        echo -e "Please enter a summary"
    else
        blog_summary="$answer"
        break
    fi
done

# Correct information checker
echo -e \
    "\nGIVEN INFORMATION\n"
    "\rTitle: $blog_title\n"
    "\rDate: $blog_date\n"
    "\rCatagories:"
for catagory in "${blog_catagories[@]}"; do
    echo -e "    * $catagory"
done
echo -e "Summary: $blog_summary\n"
while true; do
    read -p "Are you happy with the above? " answer
    case $answer in
        [Yy]* ) echo -e "Blog data rejected"; break;;
        [Nn]* ) echo -e "Blog data accepted"; exit;;
        * ) echo "Please answer [Y/y]es or [N/n]o.";;
    esac
done


# Writing blog to file
# --------------------

# Creating tmp file
cp "blog_template.html" "blog.tmp"

# Adds meta 
sed -i "s/BLOG_TITLE_GOES_HERE/$blog_title/g" blog.tmp
sed -i "s/BLOG_DATE_GOES_HERE/$blog_date/g" blog.tmp
sed -i "s/BLOG_BODY_GOES_HERE/$blog_body/g" blog.tmp

# Checks reading time
if [ "$blog_length" -lt 4 ]; then
    sed -i "/READING_TIME_GOES_HERE/d" blog.tmp
else
    sed -i "s/READING_TIME_GOES_HERE/~$blog_length minutes/g" blog.tmp
fi

# Moving into position
blog_location="$(date +%Y)/$(date +%m)/$(date +%d)/$(echo $blog_title | sed "s/[^a-zA-Z0-9]//g")"
mv "blog.tmp" "../blogs/$blog_location"


# Managing Catagories
# -------------------
    
for catagory in "${blog_catagories[@]}"; do
    # Adding to cloud
    echo "$catagory" >> cloud.txt

    # Existence Dependent Additions
    if [ -f "../blogs/Catagories/$catagory" ]; then
        # Catagory found
        identifier="\t\t\t<!-- List Begins Here -->\n"
        xtraHTML="\t\t\t<li><a href=\"..\/$blog_location\">$blog_date - $blog_title<\/a><\/li>\/g"
        sed -i "s/$identifier/$identifier$xtraHTML" "../blogs/Catagories/$catagory"
        # sed -i "THING WITH RSSS"            
    else
        # Catagory Not Found 
        cp "blog_template.html" "catagory.tmp"
        sed -i "s/CATAGORY_NAME_GOES_HERE/$catagory/g" catagory.tmp
        sed -i "s/BLOG_TITLE_GOES_HERE/$blog_title/g" catagory.tmp
        sed -i "s/BLOG_DATE_GOES_HERE/$blog_date/g" catagory.tmp
        # Handling feeds
        cp "rss_template.xml" "catagory.xml"
        sed -i "s/CATAGORY_NAME_GOES_HERE/$catagory/g" catagory.tmp
        sed -i "s/BLOG_TITLE_GOES_HERE/$blog_title/g" blog.tmp
        sed -i "s/FULL_BLOG_DATE_GOES_HERE/$blog_date_long/g" catagory.tmp
        sed -i "s/BLOG_LOCATION_GOES_HERE/$blog_location/g" catagory.tmp
        sed -i "s/BLOG_SUMMARY_GOES_HERE/$blog_summary/g" catagory.tmp
    fi
done

# Adding to general catagory files
# add to catagory_all and rss_all files