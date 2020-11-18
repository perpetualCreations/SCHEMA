"""
Project SCHEMA
Convert Markdown documentation into HTML, with a minimal, dark theme.

main module.
"""

import argparse
from urllib.request import urlretrieve
from os import remove

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

if parameters.fetch is True:
    urlretrieve("https://dreamerslegacy.xyz/css/main.css", "main.css")
    urlretrieve("https://dreamerslegacy.xyz/css/schema.css", "schema.css")
    print("Retrieved CSS documents successfully.")
else:
    print("--fetchcss was not specified, not retrieving CSS documents.")
pass

if parameters.src_url is not None:
    urlretrieve(parameters.src_url, "temp.md")
    parameters.src_path = "temp.md"
else:
    if parameters.src_path is None:
        raise FileNotFoundError("Missing source Markdown document! Please specify one through parameters --url or --file!")
    pass
pass

if parameters.name is None:
    parameters.name = "(Project Name Not Specified)"
pass

if parameters.author is None:
    parameters.author = "Unknown"
pass

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

if parameters.nav is not None:
    product += '''
        <div class = "topnav">
            <a href = "/index.html">Back</a>
        </div>'''
pass

product += '''
        <div class = "schema">'''

with open(parameters.src_path) as doc:
    index = 0
    try:
        while True:
            doc.readline(index)
            index += 1
        pass
    except EOFError:
        # export logic here
        pass
    pass
pass

remove("temp.md")
