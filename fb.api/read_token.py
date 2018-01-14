import json

def read_token(filename):
	f = open(filename, "r")
	data = json.load(f)
	return data["access_token"]
