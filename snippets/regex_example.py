#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# this example demonstrates how to use regular
# expressions in python
import re

# Step 1: compile a regular expression and assign it to a variable
pattern = re.compile("CTRL[0-9]*")

# Step 2: use the `.match' method on the pattern to match the
# regex against a string
# `None' is returned if no match was found, otherwise a
# `match' object is returned
# this, the following line of code can be used in an `if' clause
print(pattern.match("CTRL1"))  # this should match
print(pattern.match("CTR"))  # this should not match
