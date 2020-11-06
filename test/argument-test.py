"""
Testing argparse.
"""

import argparse

arguments = argparse.ArgumentParser()
arguments.add_argument("--parameter", dest = "something", action = "store_const", const = True)
parsed = arguments.parse_args()

if parsed.something is True:
    print("yay!")
else:
    print(parsed.something)
pass
