"""
Project SCHEMA
Convert Markdown documentation into HTML, with a minimal, dark theme.

main module.

TODO modularize and cleanup
"""

# imports
import argparse
from urllib.request import urlretrieve
from os import remove

# arguments
# TODO add more for further automatic formatting and auxiliary options
arguments = argparse.ArgumentParser(description = "Convert Markdown into HTML documentation, featuring a minimal, dark theme.")
arguments.add_argument("--fetchcss", dest = "fetch", action = "store_const", const = True, help = "Specify this flag if you want the CSS documents required for rendering the HTML document. This requires an Internet connection.")
arguments.add_argument("--url", dest = "src_url", type = str, help = "Specify the URL to retrieve the Markdown document. This requires an Internet connection.")
arguments.add_argument("--file", dest = "src_path", type = str, help = "Specify the path to retrieve the Markdown document. This requires a local copy.")
arguments.add_argument("--name", dest = "name", type = str, help = "Specify the project name.")
arguments.add_argument("--author", dest = "author", type = str, help = "Specify the author of the project. There can only be ONE.")
arguments.add_argument("--icon", dest = "icon", type = str, help = "Specify path to project icon image, this will be rescaled to a 64x64 pixels when the page is displayed.")
arguments.add_argument("--showbadges", dest = "showbadges", action = "store_const", const = True, help = "Specify this flag if you want to transfer badges. Supported badge types include Shields.io (WIP) and ForTheBadge.")
arguments.add_argument("--navback", dest = "nav", action = "store_const", const = True, help = "Specify this flag if you want to have a navigation bar on the top of the page to return to index.html.")
parameters = arguments.parse_args()

# if --fetchcss is specified, get CSS documents for rendering the page
if parameters.fetch is True:
    urlretrieve("https://dreamerslegacy.xyz/css/main.css", "main.css")
    urlretrieve("https://dreamerslegacy.xyz/css/schema.css", "schema.css")
    print("Retrieved CSS documents successfully.")
else:
    print("--fetchcss was not specified, not retrieving CSS documents.")
pass

# if --url is specified, get Markdown document from specified URL
if parameters.src_url is not None:
    urlretrieve(parameters.src_url, "temp.md")
    parameters.src_path = "temp.md"
else:
    if parameters.src_path is None:
        raise FileNotFoundError("Missing source Markdown document! Please specify one through parameters --url or --file!")
    pass
pass

# if --name is not specified, use this as project name
if parameters.name is None:
    parameters.name = "(Project Name Not Specified)"
pass

# if --author is not specified, use this as author name
if parameters.author is None:
    parameters.author = "Unknown"
pass

# base template including head for output document, product stores the document
product = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Documentation for """ + parameters.name + '''.">
        <meta name="author" content="''' + parameters.author + '''">
        <title>''' + parameters.name + ''' Documentation</title>
        <link rel="preload" href="main.css" as="style">
        <link rel="preload" href="schema.css" as="style">'''

# if --icon is specified, include image preload, this marginally accelerates page render times
if parameters.icon is not None:
    product += '''<link rel="preload" href="''' + parameters.icon + '''" as="image">'''
pass

product += '''
        <link rel="icon" href="favicon.ico">
        <link rel="stylesheet" type="text/css" href="main.css">
        <link rel="stylesheet" type="text/css" href="schema.css">
        <style>
			img {
 				 width: 100%;
				}
        </style>
    </head>
    <body>'''

# if --navback is specified, add a navigation bar leading back to index.html
if parameters.nav is not None:
    product += '''
        <div class = "topnav">
            <a href = "/index.html">Back</a>
        </div>'''
pass

# define page contents with div tag
product += '''
        <div class = "schema">'''

# if --icon is specified, add image tag for icon
if parameters.icon is not None:
    product += '''
            <img src="''' + parameters.icon + '''" class = "project-icons">'''
pass

# parse the document
with open(parameters.src_path) as doc:
    index = 0 # index of current parsed line
    in_code_quote = False # whether the parsed line is currently in a code quote
    dump = "" # paragraph text is dumped here until a newline is detected, when then it is emptied into a tag, and this variable reset
    try:
        while True:
            if index == 0 and all(x in "=" for x in doc.readline(index + 1)) is True: # header 1 conversion, checks for = symbol in next line
                product += '''
            <h1>''' + doc.readline(index) + "</h1>"
                index += 1
            elif index == 0 and all(x in "-" for x in doc.readline(index + 1)) is True: # header 2 conversion, checks for - symbol in next line
                product += '''
            <h2>''' + doc.readline(index) + "</h2>"
                index += 1
            elif doc.readline(index)[:6].count("#") != 0 and in_code_quote is False: # header conversion, checks for 6 or less hashtags at the start of a line, which is syntax for a header in Markdown, will not trigger if in code-quote
                if doc.readline(index)[doc.readline(index)[:6].count("#"):][:1] == " ": # check if there is a whitespace after the hashtags, remove if there is, send output to variable named contents
                    contents = doc.readline(index)[doc.readline(index)[:6].count("#"):].lstrip(" ")
                else:
                    contents = doc.readline(index)[doc.readline(index)[:6].count("#"):]
                pass
                product += '''
            <h''' + str(doc.readline(index)[:6].count("#")) + ">" + contents + "</h" + str(doc.readline(index)[:6].count("#")) + ">" # apply contents into a header tag, size is based off of number of hashtags
            elif [] in doc.readline(index):
                pass
            elif doc.readline(index) == "" and dump != "": # if empty line and paragraph dump is not empty, empty paragraph dump into tag
                product += '''
            <p>''' + dump + "</p>"
                dump = ""
            else: # if all clauses fail, parse as paragraph
                if dump == "" and doc.readline(index) != "": # if there's already paragraph text in dump, add a whitespace before appending
                    dump += doc.readline(index)
                elif dump != "" and doc.readline(index) != "":
                    dump += " " + doc.readline(index)
                else: # skip line, no syntax was able to be parsed, this occurs if dump was empty and parser parsed an empty line
                    pass
                pass
            pass
            index += 1
        pass
    except EOFError:
        # export logic here
        pass
    pass
pass

remove("temp.md")
