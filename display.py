import re
import json

with open('yachts.json') as f:
	yachts = f.readlines()

re.replace("^[0-9]", "")