#! python
import sys, json, ndjson, getopt
from Patient import Patient
from AllergyIntolerance import AllergyIntolerance
from CarePlan import CarePlan
 
# Options
options = "h"
 
# Long options
long_options = ["help", "first-name=", "last-name=", "id="]

#variable declarations
patientFirstName = None
patientLastName = None
patientId = None
searchType = "Name"

try:
	# Parsing argument
	arguments, values = getopt.getopt(sys.argv[1:], options, long_options)

	# checking each argument
	for currentArgument, currentValue in arguments:
		if currentArgument in ("-h", "--help"):
			print ("See README.md for usage")
			sys.exit()

		elif currentArgument in ("--first-name"):
			patientFirstName = currentValue

		elif currentArgument in ("--last-name"):
			patientLastName = currentValue

		elif currentArgument in ("--id"):
			patientId = currentValue

except getopt.error as err:
	# output error, and return with an error code
	print (str(err))
	
if ((patientId is not None) and ((patientFirstName is not None) or (patientLastName is not None))):
	print ("Invalid Argumaents. Please enter First Name and Last Name or ID")
	sys.exit()
elif ((patientId is None) and ((patientLastName is None) or (patientFirstName is None))):
	print ("Invalid Argumaents. Please enter both First Name and Last Name")
	sys.exit()
elif (patientId is not None):
	searchType = "Id"

patientObject = Patient(patientFirstName, patientLastName, patientId, searchType)
searchResult = patientObject.findPatient()

if searchResult == False:
	print ("Patient Not Found")
	sys.exit()

print("Patient Id: ", patientObject.patId)
print("Patient Name: ", patientObject.fName, " ", patientObject.lName)
print("RESOURCE_TYPE\t\t\t\t\t\tCOUNT")
print("______________________________________________________________")

allergies = AllergyIntolerance(patientObject.patId)
print("AllergyIntolerance\t\t\t\t\t", allergies.recordCount)

carePlans = CarePlan(patientObject.patId)
print("CarePlan\t\t\t\t\t\t", carePlans.recordCount)

