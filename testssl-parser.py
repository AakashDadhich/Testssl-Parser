# Import sys for accessing command line interface (CLI) arguments
import sys
# Import csv for parsing csv files
import csv
# Set filename to CSV file passed via CLI argument 
filename = sys.argv[1]

# Initialise fieldName and rows lists
fieldNames = []
fileContents = []
issuesList = []

# Open contents of CSV file in read-only mode
with open(filename, "r") as csvFile:
    # Create new CSV object
    csvObject = csv.reader(csvFile)
    
    # Read first line as field names, keep and format first 5 columns
    fieldNames = next(csvFile)
    fieldNames = fieldNames.replace("\"", "")
    fieldNames = fieldNames.split(",", 5)
    fieldNames = fieldNames[:5]

    # Read rest of file as contents
    for row in csvObject:
        # If Severity is LOW/MED/HIGH/CRIT, store first five columns
        if (row[3] != "OK") and (row[3] != "INFO") and (row[3] != "FATAL"):
            fileContents.append(row[:5])
            # If issue type has not yet been stored, then store it in issuesList
            if (row[0] not in issuesList):
                issuesList.append(row[0])
                    
# Print affected IP:port by issue
# Iterate through list of unique issues
for issue in issuesList:
    print(issue)
    # Iterate through parsed CSV contents
    for row in fileContents:
        if issue in row:
            # Print IP:port - finding
            print("".join((row[1].split("/"))[:1]) + ":" + row[2] + " - " + row[4])
    print("\n")
    
# Print parsed info for debug
#print("Input file: " + filename + "\n\n")
#print("Field names: " + " | ".join(fieldNames))
#for line in fileContents:
#    print(line)
