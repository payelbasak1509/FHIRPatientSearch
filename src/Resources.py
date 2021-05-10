import sys, json, ndjson

class ResourceFinder:

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
