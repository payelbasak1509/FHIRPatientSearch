import sys, json, ndjson

class ResourceFinder:

	# getResourceByPatientID - function to find a relationship between the patient and resource based on ID 
	# Parameters:
	# resourceType: String - Name of the file to read
	# resourceReference: String - The element referencing the patient id
	# patId: String - patient Id
	def getResourceByPatientID(self, resourceType, resourceReference, patId):
		self.recordCount = 0
		# load Resource JSON records
		resourcePath = "..\\1uphealth json\\" + resourceType + ".ndjson"
		with open(resourcePath) as f:
			reader = ndjson.reader(f)
			for post in reader:
				json_object = json.loads(json.dumps(post, indent=4))
				patReference = json_object[resourceReference]["reference"].split("/")[1]
				if patReference == patId:
					self.recordCount = + self.recordCount + 1
	# getResourceByPatientorGroupID - function to find a relationship between the patient/group and resource based on ID 
	# Parameters:
	# resourceType: String - Name of the file to read
	# resourceReference: String - The element referencing the patient id
	# patId: String - patient Id
	# groupList: String - List of Group Ids
	def getResourceByPatientorGroupID(self, resourceType, resourceReference, patId, groupList):
		self.recordCount = 0
		# load Resource JSON records
		resourcePath = "..\\1uphealth json\\" + resourceType + ".ndjson"
		with open(resourcePath) as f:
			reader = ndjson.reader(f)
			for post in reader:
				json_object = json.loads(json.dumps(post, indent=4))
				reference = json_object[resourceReference]["reference"].split("/")[1]
				referenceType = json_object[resourceReference]["reference"].split("/")[0]
				if referenceType == "Patient":
					if reference == patId:
						self.recordCount = + self.recordCount + 1
				elif referenceType == "Group":
					if reference in groupList:
						self.recordCount = + self.recordCount + 1
	# getResourceByEntity - function to find a relationship between the patient and resource based on entity relationships 
	# Parameters:
	# resourceType: String - Name of the file to read
	# patId: String - patient Id
	def getResourceByEntity(self, resourceType, patId):
		self.recordCount = 0
		# load Resource JSON records
		resourcePath = "..\\1uphealth json\\" + resourceType + ".ndjson"
		with open(resourcePath) as f:
			reader = ndjson.reader(f)
			for post in reader:
				json_object = json.loads(json.dumps(post, indent=4))
				targets = json_object["target"]
				for eachTarget in targets:
					reference = eachTarget["reference"].split("/")[1]
					referenceType = eachTarget["reference"].split("/")[0]
					if referenceType == "Patient":
						if reference == patId:
							self.recordCount = + self.recordCount + 1
