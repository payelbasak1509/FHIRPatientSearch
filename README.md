# Patient Resource Search

Python application to count the number of occurences in an FHIR Resource file based on patient identification data 

## Installation

Download [python](https://www.python.org/downloads/)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ndjson.
```bash
pip install ndjson
```

Download the source files
```bash
git clone https://github.com/payelbasak1509/FHIRPatientSearch.git
```

Navigate to the src folder

Compile the Source
```bash
python -m compileall -f ./
```

## Usage

Search for a Patient's related Resource files based on patient's Id
```python
python GetPatientData.py --id 421c3eaf-f95c-47af-b8cd-f6cbcb192fad
```

Search for a Patient's related Resource files based on patient's name
```python
python GetPatientData.py --first-name Cleo27 --last-name Bode78
```

## Sample Output

```bash
C:\FHIRPatientSearch\src>python GetPatientData.py --id 421c3eaf-f95c-47af-b8cd-f6cbcb192fad
Patient Id:  421c3eaf-f95c-47af-b8cd-f6cbcb192fad
Patient Name:  Wava789   Greenholt190
RESOURCE_TYPE                                           COUNT
______________________________________________________________
AllergyIntolerance                                       0
CarePlan                                                 2
CareTeam                                                 2
Claim                                                    30
Condition                                                19
Device                                                   0
DiagnosticReport                                         80
DocumentReference                                        20
Encounter                                                20
ExplanationOfBenefit                                     20
Group                                                    1
ImagingStudy                                             0
Immunization                                             13
MedicationAdministration                                 3
MedicationRequest                                        10
Observation                                              632
Procedure                                                31
Provenance                                               1
SupplyDelivery                                           72
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
