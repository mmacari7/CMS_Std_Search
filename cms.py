# Michael Macari
# Worker functions

import os
import csv
import string
import sqlite3

class CMS2SQL:
    def __init__(self, dbname):
        # List of codes and medical abbreviations to try to aid the matching search engine
        self.medcodes = {
            "ct" : "computerized tomography", "w" : "with", "wo" : "without", "wrkstaton" : "workstation", "wrkstato" : "workstation",
            "upr" : "upper", "ext": "extremity", "us": "ultrasound", "opth": "ophthalmic", "er": "emergency room", "inj": "injection"
        }

        # Sets the database name and appends file type
        self.dbname = dbname + '.sq3'

        # Calls the first function to process the CSV in data directory
        self.getData()
        
    # Function that returns dictionary of files to process
    def getData(self):
        # Gets the directory where our data sits
        dataDir = os.path.abspath("data")

        # Get all files with CSV extension
        datafiles = {}
        for file in os.listdir(dataDir):
            if(file.endswith(".csv")):
                fullFile = os.path.join(dataDir, file)
                file = file.replace('_', ' ')[:-10]
                datafiles[file] = fullFile

        # Calls the process CSV files function
        self.processCSV(datafiles)
        return

    # Function to process the CSV files and attempt to standardize the data
    def processCSV(self, fileobj):
        for k,v in fileobj.items():
            
            # Dictionary to store description and prices, passed to generate the SQL db
            # Key also passed as hospital name for sql db
            csvfile = open(v)
            csvreader = csv.reader(csvfile, delimiter=',')

            # Sets our data dictionary which will be written to the sql
            d = {"procedure": [], "price": []}

            for row in csvreader:
                # Skips the column titles
                if(row[0] == 'Description'):
                    continue

                # Strips the punctuation from the string
                splitstring = row[0].lower().translate(str.maketrans('', '', string.punctuation)).split()
                
                # Strips $ from price
                if('$' in row[1]):
                    pstrip = row[1].replace('$', '')
                else:
                    pstrip = row[1]

                # Strip cents from price anything after .00 including .
                if('.' in pstrip):
                    pstrip = pstrip[:-4]
                
                # Strip the comma
                pstrip = pstrip.translate(str.maketrans('', '', string.punctuation))

                newstring = ''

                # Checks if we can simplify the string even futher from the medcodes
                for word in splitstring:
                    if(word in self.medcodes):
                        newstring += self.medcodes[word] + ' '
                    else:
                        newstring += word + ' '
                
                # Strips the last bit of whitespace
                newstring = newstring.strip()
                
                d["procedure"].append(newstring)
                d["price"].append(pstrip)
            
            print("Processed " + k + " CMS CSV")
            # Calls the function to write the data to sql
            self.write_to_sql(k, d)

        return
    
    # Function to write the data to the SQL in a table
    def write_to_sql(self, tbname, data):
        print(tbname, len(data["procedure"]))
        
        db = sqlite3.connect(self.dbname)




        return

# Pass test as the DB name
mycms = CMS2SQL("test")
