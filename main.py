# Michael Macari
# Charge Master Engine

# import os
# import csv
# import cms

# mycms = cms.chargeMaster()

import cms
import processdb

# Creates a new class obj to convert our CMS -> SQL
#newdb = cms.CMS2SQL("mydb")

# Reader for SQL, pass db name: Autodetects tables internally
newread = processdb.Dbdata("mydb.sq3")

# Function to extract all the data from each table in SQL
newread.extractAll()

# Creates our search function
search = newread.proto1sch("insulin injection", limit=2, gettime=True)

print('')

# Iterates through the search results to display data
for hos, res in search.items():
    print(hos)
    for proc in res:
        p = ''
        if(proc[2] == '0' or proc[2] == ''):
            p = "Price Not Listed"
        else:
            p = "$" + proc[2]

        print("    " + proc[1] + " | " + p)
    print('')



#print(fuzz.ratio("INSLN", "INSULIN LISPRO 100U/ML 3ML"))
#print(fuzz.partial_ratio("INSLN", "INSULIN LISPRO 100U/ML 3ML"))
#print(fuzz.token_sort_ratio("INSLN", "INSULIN LISPRO 100U/ML 3ML"))



#print(fuzz.token_set_ratio("INSLN", "INSULIN LISPRO 100U/ML 3ML"))



# Possibly use set ratio and partial ratio together on data strings
# Or just match all 4

# wordList = ["Hello I am a dog", "Hello I am an insulin dog", "dont ttlll me what to and to not do", "Taco salad is delicious", "insulin baby girld amn afsyee"]

# #print(process.extract("insulin injection", wordList))

# print(fuzz.ratio("insulin injection", "sc computerized tomography injection asp ganglion cyst"))
# print(fuzz.partial_ratio("insulin injection", "sc computerized tomography injection asp ganglion cyst"))
# print(fuzz.token_sort_ratio("insulin injection", "sc computerized tomography injection asp ganglion cyst"))
# print(fuzz.token_set_ratio("insulin injection", "sc computerized tomography injection asp ganglion cyst"))


# # Process is using WRatio
# print(fuzz.WRatio("insulin injection", "sc computerized tomography injection asp ganglion cyst"))