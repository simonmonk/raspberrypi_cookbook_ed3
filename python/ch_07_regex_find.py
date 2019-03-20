import re

text = "looking forward to finding the word for"
x = re.search("(^|\s)for($|\s)", text)

print(x.span())