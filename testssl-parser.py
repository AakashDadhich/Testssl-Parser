# Parse testssl.sh CSV output files into a user-friendly file that organises affected IPs by issue! 
# Works best for scanning many hosts into one CSV file. 

# Version Number: v1.0
# Author: Aakash Dadhich

# Usage: 
# python3 testssl-parser.py {path-to-file}.csv 

# Import sys for accessing command line interface (CLI) arguments
import sys
# Import csv for parsing CSV files
import csv
# Set filename to CSV file passed via CLI argument 
filename = sys.argv[1]

# Initialise lists
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
                    
# Create writable output file
outputFile = open("parsed-testssl.txt", "w")
outputFile.write("Parsed from " + filename + "\n\n")

# Iterate through list of unique issues
for issue in issuesList:
    outputFile.write(issue + "\n")
    # Iterate through parsed CSV contents
    for row in fileContents:
        if issue in row:
            # Store in format: "IP:port - finding"
            outputFile.write("\t" + "".join((row[1].split("/"))[:1]) + ":" + row[2] + " - " + row[4] + "\n")
    outputFile.write("\n")

# Close output file
outputFile.close()
# Print notification to console
print("Successfully parsed; output stored in parsed-testssl.txt")

# Print parsed info for debug

#print("Field names: " + " | ".join(fieldNames))

#for line in fileContents:
#    print(line)
