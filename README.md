# IntenseEmojiGenerator

Simple python script for creating **intense** emoji out of normal, *boring* png file

### Requirements:

* Python3 installed
* You need to have emoji _png_ file with transparent background

### Basic usage:

Standard:
``python3 app.py -f FILE_NAME``

Different size: ``python3 app.py -f FILE_NAME -s 200``

### What the hell is this -s flag?

Look at the following picture:

![Pretty explainatory image not loaded](resources/explainatory-image.png?raw=true "Title")

In that case `a` and `b` are height and width of the original image you want to upload.
`x` and `y` however are the values that are always being summed to the value you put after
the `-s` argument.

**TLDR:** s = x+y

## Things to do:

Well, I'd like to create a web-app version and deploy it on github, so you don't need to clone 
the repo at all...
