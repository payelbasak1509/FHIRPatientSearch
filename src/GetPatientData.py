#! python
import sys, json, ndjson, getopt
from Patient import Patient
from Resources import ResourceFinder
 
# Options
options = "h"
 
# Long options
long_options = ["help", "first-name=", "last-name=", "id="]

# variable declarations
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

# verify that provided arguments are as expected for the options
if ((patientId is not None) and ((patientFirstName is not None) or (patientLastName is not None))):
	print ("Invalid Argumaents. Please enter First Name and Last Name or ID")
	sys.exit()
elif ((patientId is None) and ((patientLastName is None) or (patientFirstName is None))):
	print ("Invalid Argumaents. Please enter both First Name and Last Name")
	sys.exit()
elif (patientId is not None):
	searchType = "Id"

# Find Patient details from Name or Id
patientObject = Patient(patientFirstName, patientLastName, patientId, searchType)
searchResult = patientObject.findPatient()

if searchResult == False:
	print ("Patient Not Found")
	sys.exit()
	
# get Patient's related data (groups, medications etc.)
patientObject.getPatientGroups()

print("Patient Id: ", patientObject.patId)
print("Patient Name: ", patientObject.fName, " ", patientObject.lName)
print("RESOURCE_TYPE\t\t\t\t\t\tCOUNT")
print("______________________________________________________________")

# Create an instance of the Resource Finder
finder = ResourceFinder()

finder.getResourceByPatientID("AllergyIntolerance", "patient", patientObject.patId)
print("AllergyIntolerance\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientID("CarePlan", "subject", patientObject.patId)
print("CarePlan\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientID("CareTeam", "subject", patientObject.patId)
print("CareTeam\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientID("Claim", "patient", patientObject.patId)
print("Claim\t\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientID("Condition", "subject", patientObject.patId)
print("Condition\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientID("Device", "patient", patientObject.patId)
print("Device\t\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientorGroupID("DiagnosticReport", "subject", patientObject.patId, patientObject.groupList)
print("DiagnosticReport\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientorGroupID("DocumentReference", "subject", patientObject.patId, patientObject.groupList)
print("DocumentReference\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientorGroupID("Encounter", "subject", patientObject.patId, patientObject.groupList)
print("Encounter\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientID("ExplanationOfBenefit", "patient", patientObject.patId)
print("ExplanationOfBenefit\t\t\t\t\t", finder.recordCount)

print("Group\t\t\t\t\t\t\t", len(patientObject.groupList))

finder.getResourceByPatientorGroupID("ImagingStudy", "subject", patientObject.patId, patientObject.groupList)
print("ImagingStudy\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientID("Immunization", "patient", patientObject.patId)
print("Immunization\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientorGroupID("MedicationAdministration", "subject", patientObject.patId, patientObject.groupList)
print("MedicationAdministration\t\t\t\t", finder.recordCount)

finder.getResourceByPatientorGroupID("MedicationRequest", "subject", patientObject.patId, patientObject.groupList)
print("MedicationRequest\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientorGroupID("Observation", "subject", patientObject.patId, patientObject.groupList)
print("Observation\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientorGroupID("Procedure", "subject", patientObject.patId, patientObject.groupList)
print("Procedure\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByEntity("Provenance", patientObject.patId)
print("Provenance\t\t\t\t\t\t", finder.recordCount)

finder.getResourceByPatientID("SupplyDelivery", "patient", patientObject.patId)
print("SupplyDelivery\t\t\t\t\t\t", finder.recordCount)