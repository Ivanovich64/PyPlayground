import re

def validateDiff(num):
	if re.match("^(0|1|2|3|4|5|10000)$",num):
		return num
	else:
		print("[!] That's an invalid option, you retard.")
		return validateDiff(input("Try Again\n > "))
