# Import sys for accessing command line interface (CLI) arguments
import sys
# Import csv for parsing csv files
import csv
# Set filename to CSV file passed via CLI argument 
filename = sys.argv[1]
print("Input file: " + filename + "\n\n")

# Initialise fieldName and rows lists
fieldNames = []
fileContents = []

# Open contents of CSV file in read-only mode
with open(filename, "r") as csvFile:
    # Create new CSV object
    csvObject = csv.reader(csvFile)
    
    # Read first line as field names
    fieldNames = next(csvFile)
    print("Field names: " + fieldNames.replace("\"", "") + "\n")

    # Read rest of file as contents
    for row in csvObject:
        # If Severity is LOW/MED/HIGH/CRIT
        if (row[3] != "OK") and (row[3] != "INFO"):
            print(row[:5])
            fileContents.append(row[:5])
