import sqlite3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import time
# Class with functions for SQL -> Data conversions
class Dbdata:
    def __init__(self, dbname):
        self.dbname = dbname
        
        self.tables = []
        self.data = {}

        self.searches = {}

        self.getAllTables()

    # Gets list of each table in DB
    def getAllTables(self):
        # Creates our connection
        db = sqlite3.connect(self.dbname)
        c = db.cursor()

        # Gets list of tables in db
        res = db.execute("select name from sqlite_master where type='table';")
        for name in res:
            self.tables.append(name[0])
        return

    # Defines function to extract data from a table in db
    def extract_from_table(self, tbname):
        db = sqlite3.connect(self.dbname)
        c = db.cursor()

        c.execute("select * from [" + tbname + "]")
        table = c.fetchall()
        
        self.data[tbname] = table
        return

    # Function to extract data from all tables in DB
    def extractAll(self):
        # Iterate through each table and fetch the data
        for table in self.tables:
            self.extract_from_table(table)
        return

    # String matches by levenshtein distance using fuzzy wuzzy
    def proto1sch(self, ss, limit=4, gettime=False): # Limit defaults 4 unless passed more, time defaults false -> Used for debugging
        
        # If the given string has already been a search term
        if(ss in self.searches.keys()):
            return(self.searches[ss])
    
        # Sets our return obj
        d = {}

        # Use time if time is true
        if(gettime):
            start_time = time.time()

        for table, data in self.data.items():
            d[table] = []

            # Iterate through the data vals and perform fuzzy string matching
            for i in range(len(data)):
                # Gets the weight comparison
                weight = fuzz.WRatio(ss, data[i])

                # If we are under limit always append
                if(len(d[table]) < limit):
                    d[table].append((data[i][0], data[i][1], data[i][2], weight))
                else:
                    # Get the current min weight
                    curmin = min(d[table], key=lambda x: x[3])
                    # If the current string has higher match weight then the minimum weight in the data table
                    if(weight > curmin[3]):
                        # Removes the current minimum
                        d[table].remove(curmin)
                        # Appends the new value with higher weight
                        d[table].append((data[i][0], data[i][1], data[i][2], weight))
        
        # Gets elapsed processing time if we want it
        if(gettime):
            elapsed_time = time.time() - start_time
            print(elapsed_time)

        # Return the results of the search
        self.searches[ss] = d
        return(d)
    
    # Explored alternative search fuzzmatch slightly quicker less accurate
    def proto2sch(self, ss, l=4, gettime=False):
        if(gettime):
            start_time = time.time()


        # Data  to retrun
        d = {}
        # Tracks already inserted strings
        insertedStrings = []
        # Iterate through our data for search
        for table, data in self.data.items():
            
            d[table] = []

            # Gets the word list converted to array to pass process
            wordList = self.genwordlist(data)
            
            res = process.extract(ss, wordList, limit=l) # (string, weight)
            
            # Iterate through the data and perform string matching
            for i in range(len(data)):
                # If our string matches to something in our result and we havent seen it already
                if(data[i][1] in (item[0] for item in res) and data[i][1] not in insertedStrings):
                    weight = 0

                    # Gets the weight of the obj from fuzzy calc
                    for t in res:
                        if(t[0] == data[i][1]):
                            weight = t[1]
                    # Puts in our data to return, and in our seen strings
                    insertedStrings.append(data[i][1])
                    d[table].append((data[i][0], data[i][1], data[i][2], weight))

        if(gettime):
            elapsed_time = time.time()-start_time
            print(elapsed_time)
        return(d)


    # Simple helper function takes the data tuple and converts to word list
    def genwordlist(self, dtup):
        # Resulting word list
        res = list(map(lambda x: x[1], dtup))
        return(res)

