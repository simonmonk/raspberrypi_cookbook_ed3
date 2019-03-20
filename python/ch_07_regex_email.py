import re

regex = '^[\w_\.+-]+@[\w_\.-]+\.[\w_-]+$'

while True:
	text = input("Enter an email address: ")
	if re.search(regex, text):
		print("valid")
	else:
		print("invalid")
