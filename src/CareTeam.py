import sys, json, ndjson

class CareTeam:

	def __init__(self, patId):
		self.recordCount = 0
		# load Patient JSON records
		with open('..\\1uphealth json\CareTeam.ndjson') as f:
			reader = ndjson.reader(f)
			for post in reader:
				json_object = json.loads(json.dumps(post, indent=4))
				patReference = json_object["subject"]["reference"].split("/")[1]
				if patReference == patId:
					self.recordCount = + self.recordCount + 1