# Michael Macari
# Charge Master Engine

import cms
import processdb

# Creates a new class obj to convert our CMS -> SQL
newdb = cms.CMS2SQL("mydb")

# Reader for SQL, pass db name: Autodetects tables internally
newread = processdb.Dbdata("mydb.sq3")

# Function to extract all the data from each table in SQL
newread.extractAll()

try:
    while(True):
        print("\nEnter term or press Ctrl-C to exit: ")
        userIn = input().lower()

        # Performs our search function on the user input phrase
        search = newread.proto1sch(userIn, limit=2)
        # If nothing could be matched
        if(not search):
            print("No results")
        
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

# CTRL-C Keyboard interrupt to end program
except KeyboardInterrupt:
    exit()
