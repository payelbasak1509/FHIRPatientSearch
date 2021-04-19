import sys, json, ndjson

class Patient:
	def __init__(self, fName, lName, patId, sType):
		self.fName = fName
		self.lName = lName
		self.patId = patId
		self.sType = sType
	
	def findPatient(self):
		# load Patient JSON records
		with open('..\\1uphealth json\Patient.ndjson') as f:
			reader = ndjson.reader(f)
			for post in reader:
				json_object = json.loads(json.dumps(post, indent=4))
				if self.sType == "Id":
					identifiers = json_object["identifier"]
					for eachIdentifier in identifiers:
						for eachElement in eachIdentifier:
							if eachElement == "type":
								temp_object = json.loads(json.dumps(eachIdentifier[eachElement]))
								if temp_object["coding"][0]["code"] == "MR":
									if eachIdentifier["value"] == self.patId:
										self.fName = json_object["name"][0]["given"][0]
										self.lName = json_object["name"][0]["family"]
										return True;
				else:
					if (json_object["name"][0]["given"][0] == self.fName and json_object["name"][0]["family"] == self.lName):
						self.patId = json_object["id"]
						return True
		return False