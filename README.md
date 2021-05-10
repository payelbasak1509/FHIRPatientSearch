# 1upHealth coding assessment

Python application to count the number of occurences in an FHIR Resource file based on patient identification data 

## Installation

Download [python](https://www.python.org/downloads/)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ndjson.
```bash
pip install ndjson
```

Download the source files
```bash
git clone https://github.com/payelbasak1509/1uphealthcode.git
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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
