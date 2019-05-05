# Michael Macari
# Charge Master Engine

# import os
# import csv
# import cms

# mycms = cms.chargeMaster()

from fuzzywuzzy import fuzz
from fuzzywuzzy import process


#print(fuzz.ratio("INSLN", "INSULIN LISPRO 100U/ML 3ML"))
#print(fuzz.partial_ratio("INSLN", "INSULIN LISPRO 100U/ML 3ML"))
#print(fuzz.token_sort_ratio("INSLN", "INSULIN LISPRO 100U/ML 3ML"))



#print(fuzz.token_set_ratio("INSLN", "INSULIN LISPRO 100U/ML 3ML"))



# Possibly use set ratio and partial ratio together on data strings
# Or just match all 4

wordList = ["Hello I am a dog", "Hello I am an insulin dog", "dont ttlll me what to and to not do", "Taco salad is delicious", "insulin baby girld amn afsyee"]

#print(process.extract("insulin injection", wordList))

print(fuzz.ratio("insulin injection", "sc computerized tomography injection asp ganglion cyst"))
print(fuzz.partial_ratio("insulin injection", "sc computerized tomography injection asp ganglion cyst"))
print(fuzz.token_sort_ratio("insulin injection", "sc computerized tomography injection asp ganglion cyst"))
print(fuzz.token_set_ratio("insulin injection", "sc computerized tomography injection asp ganglion cyst"))


# Process is using WRatio
print(fuzz.WRatio("insulin injection", "sc computerized tomography injection asp ganglion cyst"))