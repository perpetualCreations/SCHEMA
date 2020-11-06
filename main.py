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
arguments.add_argument("--file", dest = "src_path", type = str, help = "Specify the path to retrieve the Markdown document.")
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
pass

index = 0

with open(parameters.src_path) as doc:
    try:
        doc.readlines(index)
        index += 1
    except EOFError:
        # export logic here
        pass
    pass
pass

remove("temp.md")
