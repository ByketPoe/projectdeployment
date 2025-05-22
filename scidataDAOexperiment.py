# Science Data DAO
# Object for accessing, updating and deleting science data from database
# Author: Emma Farrell

import mysql.connector
import db_config as cfg

class SciDAO:
    conn = ""
    cursor = ""
    host = ""
    user = ""
    pw = ""
    db = ""

    def __init__(self):
        self.host = cfg.sql["host"]
        self.user = cfg.sql["user"]
        self.pw = cfg.sql["password"]
        self.db = cfg.sql["database"]
    
    def getcursor(self):
        self.conn = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.pw,
            database = self.db,
        )
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def closeAll(self):
        self.conn.close()
        self.cursor.close()

    def fetchAll(self, sqlstring):
        cursor = self.getcursor()
        cursor.execute(sqlstring)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray

    def fetchOne(self, sqlstring, values): # values is a tuple
        cursor = self.getcursor()
        cursor.execute(sqlstring, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def commitChange(self, changeitem, sqlstring, values, committype): # values is a tuple, commit type is a string (UPDATE, CREATE, DELETE)
        cursor = self.getcursor()
        cursor.execute(sqlstring, values)
        self.connection.commit()
        if committype.upper() == "CREATE":
            newid = cursor.lastrowid
            changeitem["id"] = newid
            self.closeAll()
            return changeitem
        else:
            self.closeAll()
            print(committype, "completed on item: ", changeitem)
    # get all collections          
    def getAllCollections(self):
        #TODO implement - formulate SQL query and call functions to execute

        return {"name":1, "collectiontypeid":1, "startdate":"2025-04-04 00:00:00", "enddate":"2025-06-04 00:00:00", "locationname":"Rockall", "measurement":"Temperature", "units":"Celsius"}
    # get all collection types 
    def getAllCollectionTypes(self):
        #TODO implement
        return {"id":1, "collectiontype":"time series"}
    # find by id
    def getDataByID(self, id):
        #TODO implement
        return {"id":1, "collectionname":"collection1", "datum":"2.2", "lat":"0", "long":"0", "datetime":"2025-06-04 00:00:00"}
    # create a collection
    def createCollection(self, collection):
        #TODO implement
        return collection
    # add data to collection
    def createData(self, colname, data):
        #TODO implement
        return {"id":1, "collectionname":"collection1", "datum":"2.2", "lat":"0", "long":"0", "datetime":"2025-06-04 00:00:00"}
    # update collection
    def updateCollection(self, collection):
        #TODO implement
        return {"name":"collection1", "collectiontypeid":1, "startdate":"2025-04-04 00:00:00", "enddate":"2025-06-04 00:00:00", "locationname":"Rockall", "measurement":"Temperature", "units":"Celsius"}
    # update data
    def updateData(self, colname, data):
        #TODO implement
        return {"id":1, "collectionname":"collection1", "datum":"2.2", "lat":"0", "long":"0", "datetime":"2025-06-04 00:00:00"}
    # delete a collection    
    def deleteCollection(self, collection):
        #TODO implement
        return True
    # delete data   
    def deleteData(self, id):
        #TODO implement
        return True
    def convertToDictionary(self, resultLine):
        attkeys=[""]
        dictOut = {}
        currentkey = 0
        for attrib in resultLine:
            dictOut[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return dictOut
        
sciDAO = SciDAO()

if __name__ == "__main__":
    collection = {"name":"collection2", "collectiontypeid":1, "startdate":"2025-04-04 00:00:00", "enddate":"2025-06-04 00:00:00", "locationname":"Rockall", "measurement":"Temperature", "units":"Celsius"} 
    data = {"id":2, "collectionname":"collection1", "datum":"2.2", "lat":"0", "long":"0", "datetime":"2025-06-04 00:00:00"}
    print ("test getallCollections")
    print (f"\t{sciDAO.getAllCollections()}")
    print ("test getallCollectionTypes")
    print (f"\t{sciDAO.getAllCollectionTypes()}")
    print ("test finddataById(1)")
    print (f"\t{sciDAO.getDataByID(1)}")
    print ("test create collection")
    print (f"\t{sciDAO.createCollection(collection)}")
    print ("test create data")
    print (f"\t{sciDAO.createCollection(data)}")
    print ("test update collection")
    print (f"\t{sciDAO.updateCollection(collection)}")
    print ("test update data")
    print (f"\t{sciDAO.updateData(collection, data)}")
    print ("test delete collection")
    print (f"\t{sciDAO.deleteCollection(1)}")
    print ("test delete data")
    print (f"\t{sciDAO.deleteData(1)}")