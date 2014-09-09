# GitHub Pages (web-only)

It's possible to use Wren without a server, a domain name, or even a permanent computer. All you need is a GitHub account! It's incredibly easy to set up and is what I recommend to people who want a simple and easy blog which they can update anywhere with an internet connection.

## Installation

![](http://i.imgur.com/40hikBU.png)

Go to the [Wren repo](https://github.com/Foggalong/wren) and click the fork button in the top right corner. This will create a copy of the Wren repository in your GitHub account.

![](http://i.imgur.com/esotigJ.png)

Wait until the forking screen has finished and you will be automatically redirected to your new repo. From here click on the settings icon in the right hand bar.

![](http://i.imgur.com/nRHKQYL.png)

In the settings menu you need to rename your repository. Change the name from ```wren``` to ```YOUR_GITHUB_NAME_HERE.github.io``` - I've given mine as an example. Then click the rename button.

Now it's just a waiting game. GitHub say it should take between 10 and 20 minutes for your web page to generate. When it has you'll be able to see it by going to http://YOUR_GITHUB_NAME_HERE.github.io


## Setting Up

Because you're using the web-only version of Wren all the setting up of your blog will be done through the editing of GitHub files. If you've never used GitHub before this may seem a little daunting but I'll guide you through every step of the way.

### Clean up the repo

![](http://i.imgur.com/uKljblF.png)

First off there are a few files you can delete because they are not needed in the web-only version. In your GitHub pages repo go to the .wren folder and delete the following files by clicking on them and then clicking the trashcan in the top right.

* install
* readme
* upgrade

Then go to the updater folder and delete every file except the updater.html file. For this one click the little pencil edit button. 

![](http://i.imgur.com/jMrALKI.png)

In the file click in the title box shown above. This is the name of the file, and its location.


![](http://i.imgur.com/KumfbP9.png)

Press the backspace key until the word updater has been completely removed. This moves the file within your GitHub repo, specifically moving it to the .wren folder. If something goes wrong just refresh the page and start again.

![](http://i.imgur.com/eWbyq2U.png)

Once that's done scroll to the bottom of the page and click "Commit Changes". Go back to the main repository as we are now done with the .wren folder.


### Personalise the config file

This is the nerve center of all the easy cusomisations that can be made to your website. 

Outside of that, all changes to the blog layout are made by changing the files themselves. There's no specific tutorial on this but have a play around and you should be able to pick it up pretty easily. If you have any problems feel free to message me and I'll try and help you out.

## Updating the Blog

As this is the web-only version of Wren unsurprisingly the updating will all be done through a web page, and copying outputs into GitHub. It's a little tedious so I'll see if I can't make it simpler in future versions. 

## Upgrading

The only major limitation of the  web-only version of Wren is that it does not currently support upgrading. This means that every time Wren gets a new feature you won't be able to use it unless you start your blog again and manually transfer the files over. I recognise that this is less than ideal so I'll do my best to fix this in later releases. If you know how to you're welcome to manually merge in changes from upstream Wren but this isn't supported.