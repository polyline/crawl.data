# -*- coding: utf-8 -*-

import requests
import json
import re

def read_response(res):
	print("Type: {}".format(type(res)))
	Jres = json.loads(res.text)
	Jdata = Jres['data']
	for com in Jdata:
		print(com['message'])
